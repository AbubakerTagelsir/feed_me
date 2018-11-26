# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class feed_me(models.Model):
#     _name = 'feed_me.feed_me'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Resturant(models.Model):
	_name = 'feed.resturant'
	description = fields.Text()
	name = fields.Char()
	location = fields.Text()
	menu = fields.One2many('feed.resturant.meal', 'menu_id','Menu')
	order_id = fields.One2many('feed.order', 'resturant_id','Order')
	order_preparation_time = fields.Float(compute="get_preparation_time")
	active_from = fields.Datetime()
	active_to = fields.Datetime()
	active = fields.Boolean(compute="is_active_now")
	
	#add categories of food??


	
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


	





