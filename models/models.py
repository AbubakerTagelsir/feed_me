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


	





