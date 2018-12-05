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



# class feed_me(models.Model):
class Order(models.Model):
	_inherit = 'sale.order'
	restaurant_id = fields.Many2one('res.company', "Restaurant")
	order_state = fields.Selection(
		selection=[('draft', 'Draft'), ('submitted', 'Submitted'), ('accepted', "Accepted"), ('delivered', "Delivered"), ('canceled', "Canceled")],
        default='draft')



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
		
	
	




	





