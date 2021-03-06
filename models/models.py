# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
# class Customer(models.Model):
# 	_name = 'feed.customer'
# 	_inherit = ['res.partner']
# 	customer_previous_orders = fields.One2many('sale.order','customer_id')

class Meal(models.Model):
	_inherit = 'product.template'
	restaurant_id = fields.Many2one('res.company')
	
	def add_to_cart(self):
		cart_id = self.env['feed.cart'].search([('user_id','=', self.env.user.id)])
		meals = cart_id.meals.search([
			('meal_id','=',self.id),
			('cart_id','=', cart_id.id)
			])
		
		if len(meals.ids) > 0:
			for meal in meals:
				meal.qty += 1
		else:
			self.env['feed.cart.meal'].create({
	                'meal_id':self.id,
	                'qty':1,
	                'price_unit':self.lst_price,
	                'cart_id':cart_id.id,
               })


class Customer(models.Model):
	_inherit = 'res.partner'
	# cart_lines = fields.One2many('feed.cart', 'customer_id')


class Restaurant(models.Model):
	_inherit = 'res.company'
	active = fields.Boolean("Status", default=True)	
	resource_calendar_id = fields.Many2one(help="Restaurant's working schedule.")
	assigned_orders = fields.One2many('sale.order','restaurant_id')

	def toggle_active(self):
		current_day = datetime.date.today().weekday()
		print("----------------------------------------------")
		print("----------------------------------------------")
		print("----------------------------------------------")
		print(current_day)
		self.active = not self.active


class Order(models.Model):
	_inherit = 'sale.order'
	restaurant_id = fields.Many2one('res.company', "Restaurant")
	order_state = fields.Selection(
		selection=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', "Accepted"),
		 ('ontheway', "On the way"),('rejected', "Rejected"),
		 ('delivered', "Delivered"), ('canceled', "Canceled")],
        default='draft')
	current_user = fields.Many2one('res.users','Current User', default=lambda self: self._uid)
	delivery_id = fields.Many2one('feed.delivery')
	preparation_time = fields.Float()
	rejection_reason = fields.Text('Order Rejected because')

	@api.onchange('order_state')
	def test(self):
		print("----------------------------------------------")
		print("----------------------------------------------")
		print("----------------------------------------------")
		print(self.current_user.id)
	def submit_order(self):
	    self.order_state = 'submitted'    

	def accept_order_by_restaurant(self):
	    self.order_state = 'accepted'
	    #TODO calculate the time needed by restaurant

	def accept_order_by_delivery(self):
	    self.order_state = 'ontheway'
	    #TODO calculate the time needed by dlivery

	def reject_order(self):
	    self.order_state = 'rejected'


	def cancel_order(self):
	    self.order_state = 'canceled'

	def deliver_order(self):
	    self.order_state = 'delivered'


# 	#odoo hr schedule
# 	active_from = fields.Datetime()
# 	active_to = fields.Datetime()
# 	active = fields.Boolean(compute="is_active_now")
# 	sections = fields.One2many('feed.restaurant.section','restaurant_id')

# 	def is_active_now(self):
# 		time = fields.datetime.now()
# 		self.active = time >= self.active_from and time <= self.active_to

class Claim(models.Model):
	_name = 'feed.claim'
	name = fields.Char(compute="_get_name")
	claim_type = fields.Selection(
				selection=[('restaurant', 'Restaurant'), ('delivery', 'Delivery'), ('other', "Other")]
				)
	restaurant_id = fields.Many2one('res.company')
	delivery_id = fields.Many2one('feed.delivery')
	description= fields.Text(help="Write your claim here")


	@api.one
	def _get_name(self):
		self.name = "CL00" + str(self.id)


		
class Delivery(models.Model):
	_name = 'feed.delivery'
	name = fields.Char(compute="_get_name")
	driver_name = fields.Char()
	phone = fields.Char()
	current_location = fields.Text()
	delivery_status = fields.Selection(
        string='Status',
        selection=[('active', 'Active'), ('inactive', 'Inactive')],
	    default = 'Unactive')
	current_orders = fields.One2many('sale.order', 'delivery_id')

	@api.one
	def _get_name(self):
		self.name = "00"+str(self.id)+self.driver_name



class CartMeal(models.Model):
	_name = 'feed.cart.meal'
	meal_id = fields.Many2one('product.template')
	qty = fields.Integer()
	cart_id = fields.Many2one('feed.cart')




class Cart(models.Model):
	_name = 'feed.cart'
	name = fields.Char(compute="_get_name")
	user_id = fields.Many2one('res.users')
	meals = fields.One2many('feed.cart.meal', 'cart_id')
	total_price = fields.Float(compute="get_meals_total_price")

	def _get_name(self):
		self.name = "My Cart"

	@api.onchange('meals')
	def get_meals_total_price(self):
		total = 0
		for meal in self.meals:
			total += meal.qty * meal.meal_id.list_price

		self.total_price = total

	def confirm_order(self):
		orders = {}
		for meal in self.meals:
			restaurant = meal.meal_id.restaurant_id
			if restaurant in orders.keys():
				orders[restaurant].append({'meal':meal.meal_id.id,'qty':meal.qty})
			else:
				orders[restaurant] = [{'meal':meal.meal_id.id,'qty':meal.qty}]
		print(orders)

		for order in orders:
			new_order = self.env['sale.order'].create({
	                'restaurant_id':order.id,
	                'partner_id': self.env.user.partner_id.id,
               })
			for line in orders[order]:
				self.env['sale.order.line'].create({
					'product_id':line["meal"],
					'product_uom_qty':line["qty"],
					'order_id':new_order.id,
					})




class User(models.Model):
	_inherit = 'res.users'
	cart_id = fields.Many2one('feed.cart')
	@api.model 
	def create(self, vals):
		new_user = super(User,self).create(vals)
		new_user.cart_id = self.env['feed.cart'].create({
			'user_id': new_user.id,
			}).id
		return new_user

	






