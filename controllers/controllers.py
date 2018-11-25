# -*- coding: utf-8 -*-
from odoo import http

# class FeedMe(http.Controller):
#     @http.route('/feed_me/feed_me/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/feed_me/feed_me/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('feed_me.listing', {
#             'root': '/feed_me/feed_me',
#             'objects': http.request.env['feed_me.feed_me'].search([]),
#         })

#     @http.route('/feed_me/feed_me/objects/<model("feed_me.feed_me"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('feed_me.object', {
#             'object': obj
#         })