# Copyright 2021-2022 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    item_image_count = fields.Integer(
        "Image Count", compute="_compute_item_image_count"
    )

    def _compute_item_image_count(self):
        for line in self:
            if not line.purchase_request_lines:
                line.item_image_count = 0
                continue
            request_lines = line.purchase_request_lines
            line.item_image_count = len(request_lines.mapped("item_image_ids"))

    def action_get_item_image_view(self):
        self.ensure_one()
        res = self.env["ir.actions.act_window"]._for_xml_id(
            "purchase_request_line_image.action_item_image"
        )
        request_lines = self.purchase_request_lines
        res["domain"] = [("request_line_ids", "in", request_lines.ids)]
        if request_lines:
            res["context"] = {
                "default_name": request_lines[0].name,
                "default_product_id": request_lines[0].product_id.id
                if request_lines[0].product_id
                else False,
                "default_request_line_ids": [(4, request_lines[0].id)],
            }
        return res
