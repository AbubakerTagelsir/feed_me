# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class feed_me(models.Model):
class FeedOrder(models.Model):

    _inherit = ['sale.order']
    
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


