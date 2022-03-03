# -*- coding: utf-8 -*-


from odoo import api, fields, models,_


class GeneralViewInherit(models.TransientModel):
    _inherit = 'account.general.ledger'

    def _get_report_values(self, data):
        res = super(GeneralViewInherit,self)._get_report_values(data)
        for acc in res['Accounts']:
            
            acc['move_lines'].sort(key=lambda l:l['ldate'])
            balance = 0.0
            # Recompute balance again after sorting datewise
            for i, line in enumerate(acc['move_lines']):
                balance += round(line['debit'], 2) - round(line['credit'], 2)
                acc['move_lines'][i]['balance'] = balance

        return res