# Copyright 2021 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    images = fields.Many2many(
        string="Image",
        attachment=True,
        compute="_compute_image",
        help="This field refs purchase request line's image. This field not editable.",
    )

    @api.depends("product_id")
    def _compute_image(self):
        for line in self:
            images = (req_line.image_ids for req_line in line.purchase_request_lines if req_line.image_ids)
            for image in images:
                line.images = image if image else False
