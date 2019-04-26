# -*- coding: utf-8 -*-

from odoo import models, fields, api

class caja(models.Model):
	_inherit = 'product.product'

	caja=fields.Char(string='Caja de zapato')
	color=fields.Char(string='Color')

class caja(models.Model):
	_inherit = 'product.template'

	caja=fields.Char(string='Caja de zapato')
	color=fields.Char(string='Color')




