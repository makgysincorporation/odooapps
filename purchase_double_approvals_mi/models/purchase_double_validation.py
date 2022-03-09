# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)


class ApprovalCategoryInherit(models.Model):
    _inherit = 'approval.category'

    approval_type = fields.Selection(selection_add=[('initial_purchase', 'Create Initial RFQ\'s')])

    @api.onchange('approval_type')
    def _onchange_approval_type(self):
        if self.approval_type == 'initial_purchase':
            self.has_product = 'required'
            self.has_quantity = 'required'

class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'

    state = fields.Selection(selection_add=[('initial_approve', 'Initial Approve')])


    def button_send_to_approver(self, force=False):
        self.write({'state': 'to approve', 'date_approve': fields.Datetime.now()})
        return {}

    def button_cancel_request(self):
        self.write({'state': 'cancel'})

    def button_confirm(self):
        for order in self:
            if order.state not in ['draft', 'sent']:
                continue
            order._add_supplier_to_product()
            # Deal with double validation process
            if order.company_id.po_double_validation == 'one_step'\
                    or (order.company_id.po_double_validation == 'two_step'\
                        and order.amount_total < self.env.company.currency_id._convert(
                            order.company_id.po_double_validation_amount, order.currency_id, order.company_id, order.date_order or fields.Date.today()))\
                    or order.user_has_groups('purchase.group_purchase_manager'):
                order.button_approve()
            else:
                order.write({'state': 'initial_approve'})
            if order.partner_id not in order.message_partner_ids:
                order.message_subscribe([order.partner_id.id])
        return True
