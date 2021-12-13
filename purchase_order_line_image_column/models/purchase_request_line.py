# Copyright 2021 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class PurchaseRequestLine(models.Model):
    _inherit = "purchase.request.line"

    image_ids = fields.Many2many(
        comodel_name="ir.attachment",
        relation="purchase_request_line_ir_attachment_rel",
        column1="purchase_request_line_id",
        column2="attachment_id",
        attachment=True,
        string="Attachments",
    )
