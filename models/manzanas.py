from odoo import models, fields

class Manzanas(models.Model):
    _name = 'baseodoo.manzanas'
    codigo = fields.Integer('Codigo', required=True)
    marca = fields.Char('Marca', required=True)
    modelo = fields.Char('Familia', required=True)
    precio = fields.Integer('Precio', required=True)