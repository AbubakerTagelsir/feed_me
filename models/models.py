# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Customer(models.Model):
	_name = 'feed.customer'
	_inherit = ['res.partner']
	customer_previous_orders = fields.One2many('feed.order','customer_id')
	print("----------------------customer --------------------")

class Meal(models.Model):
	_name = 'feed.meal'
	# _inherit = ['lunch.product']
	# meal_category = fields.Char(related= lunch.product.category)

	print("----------------------meal --------------------")

		

# class feed_me(models.Model):
class Order(models.Model):
	_name = 'feed.order'
	_inherit = ['sale.order']
	customer_id = fields.Many2one('feed.customer', "Reference")
	resturant_id = fields.Many2one('feed.resturant', "Reference")
	res_meal_id = fields.Many2one('feed.resturant.meal', "Reference")
	order_location=fields.Text(string='Location',)

	# selected_meal_items
	resturantMeal_id = fields.Many2one('feed.resturant.meal')
	meal_price = fields.Float(related="res_meal_id.price")
	meal_perparation_time=fields.Float(related="res_meal_id.meal_preparation_time")
	meal_quantity=fields.Integer("Quantity")


	total_order_price = fields.Float("Total Order Price", compute="_get_the_order_price")
	print("----------------------order --------------------")


	@api.multi
	@api.onchange('resturantMeal_id')
	def _get_total_order_price(self): 
	    print(self)   
	    total = 0.00
	    for i in self:
	        for meal in i.resturantMeal_id:
	            total += meal.meal_price * meal.meal_quantity
	        i.total_order_price = total


	total_order_time = fields.Float("Total Order time", compute="_get_the_order_time")

	@api.multi
	@api.onchange('resturantMeal_id')
	def _get_total_order_time(self): 
	    print(self)   
	    total_time = 0.00
	    for i in self:
	        for meal in i.resturantMeal_id:
	            total_time += meal.meal_perparation_time * meal.meal_quantity
	        i.total_order_time = total_time


class Resturant(models.Model):
	_name = 'feed.resturant'
	description = fields.Text()
	name = fields.Char()
	location = fields.Text()
	menu = fields.One2many('feed.resturant.meal', 'resturant_id','Menu')
	order_id = fields.One2many('feed.order', 'resturant_id','Order')
	order_preparation_time = fields.Float(compute="get_preparation_time")
	active_from = fields.Datetime()
	active_to = fields.Datetime()
	active = fields.Boolean(compute="is_active_now")
	#add categories of food??
	print("----------------------resturant --------------------")

	def is_active_now(self):
		time = fields.datetime.now()
		self.active = time >= self.active_from and time <= self.active_to


	def get_preparation_time(self):
		total = 0
		for order in self:
			total+= order.ResturantMeal_id.meal_preparation_time

		self.order_preparation_time = total


class ResturantMeal(models.Model):
	_name = 'feed.resturant.meal'
	_inherit = 'feed.meal'
	description = fields.Text()
	name = fields.Char()
	resturant_id = fields.Many2one('feed.resturant')
	meal_preparation_time = fields.Float()
	price = fields.Float()
	#add categories of food??

	print("----------------------ResturantMeal --------------------")

	





