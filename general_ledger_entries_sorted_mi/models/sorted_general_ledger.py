# -*- coding: utf-8 -*-


from odoo import api, fields, models,_


class GeneralViewInherit(models.TransientModel):
    _inherit = 'account.general.ledger'

    def _get_report_values(self, data):
        res = super(GeneralViewInherit,self)._get_report_values(data)
        for acc in res['Accounts']:
            acc['move_lines'].sort(key=lambda l:l['ldate']) 
        return res