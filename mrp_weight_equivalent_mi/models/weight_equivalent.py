# -*- coding: utf-8 -*-


from odoo import api, fields, models


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    total_weight_fg = fields.Float(string='Finished Goods (KG)', compute='_compute_total_weight_fg', help="Total Weight of Finished Goods (In KG)", store=True)
    total_weight_com = fields.Float(string='Component (KG)', compute='_compute_total_weight_com', help="Total Weight of Component Goods (In KG)", store=True)
    total_weight_bp = fields.Float(string='By Product (KG)', compute='_compute_total_weight_bp', help="Total Weight of By Product Goods (In KG)", store=True)
    total_weight_finished = fields.Float(string='Total Weight (KG)', compute='_compute_total_weight', help="Total Weight of By Product and Finished Goods (In KG)", store=True)
    


    @api.depends('product_id', 'state')
    def _compute_total_weight_fg(self):
        """
        Calculate the total weight Finished Products Weight
        """
        for record in self:
            if record.state in ['to_close','done']:
                record.total_weight_fg = record.product_qty * record.product_id.weight



    @api.depends('move_byproduct_ids', 'state')
    def _compute_total_weight_bp(self):
        """
        Calculate the total weight sum adding Finished Products Weight
        """
        for record in self:
            if record.state in ['to_close','done']:
                total_weight = 0.0
                for line in record.move_byproduct_ids:
                    total_weight += line.weight_equivalent
                record.total_weight_bp = total_weight

    

    @api.depends('move_raw_ids', 'state')
    def _compute_total_weight_com(self):
        """
        Calculate the total weight sum adding Component Products Weight
        """
        for record in self:
            if record.state in ['to_close','done']:
                total_weight = 0.0
                for line in record.move_raw_ids:
                    total_weight += line.weight_equivalent
                record.total_weight_com = total_weight

    @api.depends('total_weight_bp', 'total_weight_fg')
    def _compute_total_weight(self):
        """
        Calculate the total weight Finished Products and By Product
        """
        for record in self:
            if record.state in ['to_close','done']:
                record.total_weight_finished = record.total_weight_bp + record.total_weight_fg
class StockMoveInherit(models.Model):
    _inherit = "stock.move"

    weight_equivalent = fields.Float(string='Weight(KG)', compute='_compute_weight', store=True)

       

    @api.depends('quantity_done','product_id')
    def _compute_weight (self):
        for record in self:
            if record.product_id.weight :
                record.weight_equivalent = record.quantity_done * record.product_id.weight
            else : 
                record.weight_equivalent = 0 



