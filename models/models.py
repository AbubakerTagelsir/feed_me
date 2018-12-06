# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class Customer(models.Model):
# 	_name = 'feed.customer'
# 	_inherit = ['res.partner']
# 	customer_previous_orders = fields.One2many('sale.order','customer_id')

class Meal(models.Model):
	_inherit = 'product.template'
	restaurant_id = fields.Many2one('res.company')


class Restaurant(models.Model):
	_inherit = 'res.company'
	active = fields.Boolean("Status", default=True)	
	resource_calendar_id = fields.Many2one(help="Restaurant's working schedule.")

	def toggle_active(self):
		self.active = not self.active


class Order(models.Model):
	_inherit = 'sale.order'
	restaurant_id = fields.Many2one('res.company', "Restaurant")
	order_state = fields.Selection(
		selection=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', "Accepted"), ('delivered', "Delivered"), ('canceled', "Canceled")],
        default='draft')
	current_user = fields.Many2one('res.users','Current User', default=lambda self: self._uid)
	delivery_id = fields.Many2one('feed.delivery')

	@api.onchange('order_state')
	def test(self):
		print("----------------------------------------------")
		print("----------------------------------------------")
		print("----------------------------------------------")
		print(self.current_user.id)
	def submit_order(self):
	    self.order_state = 'submitted'

	def accept_order(self):
	    self.order_state = 'accepted'

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

	




	





