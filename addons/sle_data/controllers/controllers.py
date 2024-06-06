# -*- coding: utf-8 -*-
# from odoo import http


# class SleData(http.Controller):
#     @http.route('/sle_data/sle_data', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sle_data/sle_data/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sle_data.listing', {
#             'root': '/sle_data/sle_data',
#             'objects': http.request.env['sle_data.sle_data'].search([]),
#         })

#     @http.route('/sle_data/sle_data/objects/<model("sle_data.sle_data"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sle_data.object', {
#             'object': obj
#         })

