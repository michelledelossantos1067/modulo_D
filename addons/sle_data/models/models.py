# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sle_data(models.Model):
    _name = 'sle_data.sle_data'
    _description = 'Informaciôn de empleados'

    nombres = fields.Char(string="Nombres")
    apellidos = fields.Char(string="Apellidos")
    empresa = fields.Char(string="Empresa")
    id_empleado = fields.Char(String="Id_Empleado")

