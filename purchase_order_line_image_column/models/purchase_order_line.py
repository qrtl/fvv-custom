# Copyright 2021 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    request_line_image_ids = fields.Many2many(
        "purchase.request.line",
        compute="_compute_request_line_image_ids",
        help="This field refs purchase request line's image. This field not editable.",
    )

    @api.depends("product_id")
    def _compute_request_line_image_ids(self):
        for line in self:
            images = (req_line.image_ids for req_line in line.purchase_request_lines if req_line.image_ids)
            for image in images:
                line.images = image if image else False
