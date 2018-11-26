# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Customer(models.Model):
	_name = 'feed.customer'
	"""docstring for Customer"""
    _inherit = ['res.partner']

    customer_previous_orders = fields.One2many('feed.order','customer_id')


class Meal(models.Model):

	_name = feed.meal
	_inherit = ['lunch.product']

	meal_category = fields.Char(related= lunch.product.category)


	"""docstring for Meal"models.Modelf 

	_na__init__(self, arg):
		super(Meal,models.Model._

		_na_init__()
		self.arg = arg
		

		

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