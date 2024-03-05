from odoo import tools
from odoo import fields, models, api, _

class SaleChannel(models.Model):
    _name = 'sale.channel'

    name = fields.Char(string="Name")
    code = fields.Char(string="Code", default=lambda self: _('New'))
    warehouse_id = fields.Many2one(comodel_name="stock.warehouse")
    journal_id = fields.Many2one(comodel_name="account.journal")


    #  creo el codigo con su secuencia
    @api.model
    def create(self, vals):
        if vals.get('code', _('New')) == _('New'):
            vals['code'] = self.env['ir.sequence'].next_by_code(
                'sale.channel') or _('New')
        res = super(SaleChannel, self).create(vals)
        return res