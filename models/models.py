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

		

class Order(models.Model):

    _inherit = ['sale.order']
    _namev= feed.order
    customer_id = fields.Many2one('feed.customer', "Reference")
    resturant_id = fields.Many2one('feed.resturant', "Reference")
    
    order_location=fields.text(string='Location',)

    # selected_meal_items
    resturantMeal_id = fields.Many2one('feed.resturant.meal')
    meal_price = fields.float(related="feed.resturant.meal.price")
    meal_perparation_time=fields.float(related="feed.resturant.meal.meal_perpartion_time")
    meal_quantity=fields.Integer("Quantity")
   

    total_order_price = fields.Float("Total Order Price", compute="_get_the_order_price")


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
	menu = fields.One2many('feed.resturant.meal', 'menu_id','Menu')
	order_id = fields.One2many('feed.order', 'resturant_id','Order')
	order_preparation_time = fields.Float(compute="get_preparation_time")
	active_from = fields.Datetime()
	active_to = fields.Datetime()
	active = fields.Boolean(compute="is_active_now")
	
	#add categories of food??
	class FeedDelivery(models.model):
		_name = 'feed.delivery'
	delivery_man_name = fields.Char()
	delivery_man_phone = fields.Integer()
 	delivery_man_location = fields.Text()
	delivery_man_status = fields.Selection(
        string='Status',
        selection=[('active', 'Active'), ('unactive', 'Unactive')],
	    default = 'Unactive')
	delivery_man_history= fields.char(related="feed.order.order_id")
		
	
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


	





