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
        for line in self:
            for request_line in line.purchase_request_lines:
                if request_line.image:
                    line.image = request_line.image
                if not request_line.image:
                    continue
