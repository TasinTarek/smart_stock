# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class smart_web_job(models.Model):
#     _name = 'smart_web_job.smart_web_job'
#     _description = 'smart_web_job.smart_web_job'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
