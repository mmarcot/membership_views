# -*- coding: utf-8 -*-
# from odoo import http


# class MembershipViews(http.Controller):
#     @http.route('/membership_views/membership_views/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/membership_views/membership_views/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('membership_views.listing', {
#             'root': '/membership_views/membership_views',
#             'objects': http.request.env['membership_views.membership_views'].search([]),
#         })

#     @http.route('/membership_views/membership_views/objects/<model("membership_views.membership_views"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('membership_views.object', {
#             'object': obj
#         })
