# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class Customer(models.Model):
# 	_name = 'feed.customer'
# 	_inherit = ['res.partner']
# 	customer_previous_orders = fields.One2many('sale.order','customer_id')

# class Meal(models.Model):
# 	_name = 'feed.meal'
# 	# _inherit = ['lunch.product']
# 	# meal_category = fields.Char(related= lunch.product.category)


class Restaurant(models.Model):
	_inherit = 'res.company'
	active = fields.Boolean("Status", default=True)	

	def toggle_active(self):
		self.active = not self.active


# class feed_me(models.Model):
class Order(models.Model):
	_inherit = 'sale.order'
	restaurant_id = fields.Many2one('res.company', "Restaurant")
	# customer_id = fields.Many2one('feed.customer', "Reference")
	# order_location=fields.Text(string='Location',)

# 	# selected_meal_items
# 	resturant_meal_id = fields.Many2one('feed.restaurant.meal')
# 	meal_preparation_time=fields.Float(related="resturant_meal_id.meal_preparation_time")
# 	meal_quantity=fields.Integer("Quantity")
# 	delivery = fields.Many2one('feed.delivery')


# 	@api.multi
# 	@api.onchange('resturant_meal_id')
# 	def _get_total_order_price(self): 
# 	    print(self)   
# 	    total = 0.00
# 	    for i in self:
# 	        for meal in i.resturant_meal_id:
# 	            total += meal.price * meal.meal_quantity
# 	        i.total_order_price = total


# 	total_order_time = fields.Float("Total Order time", compute="_get_the_order_time")

# 	@api.multi
# 	@api.onchange('resturant_meal_id')
# 	def _get_total_order_time(self): 
# 	    print(self)   
# 	    total_time = 0.00
# 	    for i in self:
# 	        for meal in i.resturant_meal_id:
# 	            total_time += meal.meal_preparation_time * meal.meal_quantity
# 	        i.total_order_time = total_time


# class Restaurant(models.Model):
# 	_inherit = 'res.company'
# 	description = fields.Text()
# 	name = fields.Char()
# 	restaurant_pic = fields.Binary("Image" , attachment=True)
# 	location = fields.Text()
# 	menu = fields.One2many('feed.restaurant.meal', 'restaurant_id','Menu')
# 	current_orders = fields.One2many('sale.order', 'restaurant_id','Order')
# 	#odoo hr schedule
# 	active_from = fields.Datetime()
# 	active_to = fields.Datetime()
# 	active = fields.Boolean(compute="is_active_now")
# 	sections = fields.One2many('feed.restaurant.section','restaurant_id')

# 	def is_active_now(self):
# 		time = fields.datetime.now()
# 		self.active = time >= self.active_from and time <= self.active_to

# class RestaurantSection(models.Model):
# 	_name = 'feed.restaurant.section'
# 	name = fields.Char()
# 	restaurant_id = fields.Many2one('res.company')
# 	#capacity
	

# class Delivery(models.Model):
# 	_name = 'feed.delivery'
# 	delivery_man_name = fields.Char()
# 	delivery_man_phone = fields.Integer()
# 	delivery_man_location = fields.Text()
# 	delivery_man_status = fields.Selection(
#         string='Status',
#         selection=[('active', 'Active'), ('unactive', 'Unactive')],
# 	    default = 'Unactive')
# 	current_orders = fields.One2many('sale.order', 'delivery')
		
	
	


# class RestaurantMeal(models.Model):
# 	_name = 'feed.restaurant.meal'
# 	_inherit = 'feed.meal'
# 	description = fields.Text()
# 	name = fields.Char()
# 	restaurant_id = fields.Many2one('res.company')
# 	meal_preparation_time = fields.Float()
# 	price = fields.Float()
# 	#add categories of food??


	





