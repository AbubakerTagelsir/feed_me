# -*- coding: utf-8 -*-
from odoo import http

# class ResDemo(http.Controller):
#     @http.route('/res_demo/res_demo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/res_demo/res_demo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('res_demo.listing', {
#             'root': '/res_demo/res_demo',
#             'objects': http.request.env['res_demo.res_demo'].search([]),
#         })

#     @http.route('/res_demo/res_demo/objects/<model("res_demo.res_demo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('res_demo.object', {
#             'object': obj
#         })