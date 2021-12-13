# Copyright 2021 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

from odoo import fields, models


class ItemImage(models.Model):
    _name = "item.image"
    _description = "Item Image"
    _order = "sequence, id"

    name = fields.Char("Name", required=True)
    product_id = fields.Many2one("product.product", "Product")
    sequence = fields.Integer(default=10, index=True)
    image_1920 = fields.Image(
        "Image", max_width=1920, max_height=1920, required=True, attachment=True
    )
    image_128 = fields.Image(
        "Small Image", related="image_1920", max_width=128, max_height=128, store=True
    )
    request_line_ids = fields.Many2many(
        "purchase.request.line", string="Request Lines", ondelete="cascade"
    )
