# Copyright 2021 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    image = fields.Binary(
        string="Image",
        attachment=True,
        compute="_compute_image",
    )

    def _compute_image(self):
        purchase_request = (
            self.purchase_request_purchase_order_line_rel.purchase_request_line_id
        )
        if purchase_request.image:
            self.image = purchase_request.image
