# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class membership_views(models.Model):
#     _name = 'membership_views.membership_views'
#     _description = 'membership_views.membership_views'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
