# -*- coding: utf-8 -*-
from odoo import http

# class BarcodeSerie(http.Controller):
#     @http.route('/barcode_serie/barcode_serie/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/barcode_serie/barcode_serie/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('barcode_serie.listing', {
#             'root': '/barcode_serie/barcode_serie',
#             'objects': http.request.env['barcode_serie.barcode_serie'].search([]),
#         })

#     @http.route('/barcode_serie/barcode_serie/objects/<model("barcode_serie.barcode_serie"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('barcode_serie.object', {
#             'object': obj
#         })