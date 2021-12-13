# Copyright 2021 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Add Image Column in Purchase Order Line",
    "version": "14.0.1.0.0",
    "category": "Purchase",
    "website": "https://www.quartile.co",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["web", "purchase", "purchase_request"],
    "data": [
        "views/purchase_order_line_views.xml",
        "views/purchase_request_views.xml",
    ],
}
