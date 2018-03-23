# -*- coding: utf-8 -*-
from odoo import http

# class Kuaidi100(http.Controller):
#     @http.route('/kuaidi100/kuaidi100/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kuaidi100/kuaidi100/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kuaidi100.listing', {
#             'root': '/kuaidi100/kuaidi100',
#             'objects': http.request.env['kuaidi100.kuaidi100'].search([]),
#         })

#     @http.route('/kuaidi100/kuaidi100/objects/<model("kuaidi100.kuaidi100"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kuaidi100.object', {
#             'object': obj
#         })