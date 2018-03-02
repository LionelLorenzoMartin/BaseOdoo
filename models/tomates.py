from odoo import models, fields

class Tomates(models.Model):
    _name = 'BaseOdoo.tomates'
    codigo = fields.Integer('Codigo', required=True)
    marca = fields.Char('Marca', required=True)
    modelo = fields.Char('Familia', required=True)
    precio = fields.Integer('Precio', required=True)