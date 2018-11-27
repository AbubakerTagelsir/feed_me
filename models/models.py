# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Order(models.Model):
	_inherit = 'sale.order'
	restaurant_id = fields.Many2one('res.company', "Restaurant")


class Delivery(models.Model):
	_name = 'res.delivery'
	name = fields.Char("Delivery")
	phone = fields.Char("Mobile")
	email = fields.Char("Email")