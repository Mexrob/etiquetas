# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class etiquetas(models.Model): 
    _name = 'ej.etiquetas'
    patient_id = fields.Many2one('medical.patient', 'Paciente', required=True)

    consultations_id = fields.Many2one('product.product', 'Estudio', required=True)

    Fecha = fields.Datetime(string='Fecha', required=True)
 
