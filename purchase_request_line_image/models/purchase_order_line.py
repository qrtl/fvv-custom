# Copyright 2021 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    # item_image_ids = fields.Many2many("item.image", string="Item Images", copy=True)
    item_image_count = fields.Integer("Image Count", compute="_compute_item_image_count")

    def _compute_item_image_count(self):
        for line in self:
            if line.purchase_request_lines:
                request_lines = line.purchase_request_lines
                line.item_image_count = len(request_lines.mapped("item_image_ids"))

    def action_get_item_image_view(self):
        self.ensure_one()
        res = self.env["ir.actions.act_window"]._for_xml_id("purchase_request_line_image.action_item_image")
        if self.purchase_request_lines:
            res["domain"] = [("request_line_ids", "in", self.purchase_request_lines.ids)]
            request_line = self.purchase_request_lines[0]
            res["context"] = {
                "default_name": request_line.name,
                "default_product_id": request_line.product_id.id if request_line.product_id else False,
                "default_request_line_ids": [(4, request_line.id)],
            }
        # else:
        #     res["domain"] = [("purchase_line_ids", "in", self.id)]
        #     res["context"] = {
        #         "default_name": self.name,
        #         "default_purchase_line_ids": [(4, self.id)],
        #     }
        return res
