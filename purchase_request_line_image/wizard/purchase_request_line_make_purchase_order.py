# Copyright 2021 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

from odoo import _, api, models

class PurchaseRequestLineMakePurchaseOrder(models.TransientModel):
    _inherit = "purchase.request.line.make.purchase.order"

    # @api.model
    # def _prepare_purchase_order_line(self, po, item):
    #     vals = super()._prepare_purchase_order_line(po, item)
    #     if item.line_id.item_image_ids:
    #         vals["item_image_ids"] = [(6, 0, item.line_id.item_image_ids.ids)]
    #     return vals
