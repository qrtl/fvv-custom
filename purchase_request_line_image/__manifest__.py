# Copyright 2021 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)
{
    "name": "Purchase Request Line Image",
    "version": "14.0.1.0.0",
    "category": "Purchase",
    "website": "https://www.quartile.co/",
    "author": "Quartile Limited",
    "license": "LGPL-3",
    "installable": True,
    "depends": ["purchase_request", "web_widget_open_tab"],
    "data": [
        "security/ir.model.access.csv",
        "views/item_image_views.xml",
        "views/purchase_order_views.xml",
        "views/purchase_request_line_views.xml",
        "views/purchase_request_views.xml",
    ],
}
