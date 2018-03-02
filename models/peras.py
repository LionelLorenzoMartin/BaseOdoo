from odoo import models, fields

class Peras(models.Model):
    _name = 'BaseOdoo.peras'
    codigo = fields.Integer('Codigo', required=True)
    marca = fields.Char('Marca', required=True)
    modelo = fields.Char('Familia', required=True)
    precio = fields.Integer('Precio', required=True)