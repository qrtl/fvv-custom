# Copyright 2021 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    image = fields.Binary(
        string="Image",
        attachment=True,
        compute="_compute_image",
        help="This field refs purchase request line's image. This field not editable.",
    )

    @api.depends("product_id")
    def _compute_image(self):
        for line in self:
            line.image = False
            for request_line in line.purchase_request_lines:
                if request_line.image:
                    line.image = request_line.image
