{
    "name": "Dynamic Invoice Email",
    "author": "Muhammad Usman Hussain",
    "License": "LGPL-3",
    "version": "1.0",
    "summary": 'generate barcode for product',
    'description': """
This module offers the basic functionalities to generate barcode for product.
    """,
    'category': 'Inventory',
    'depends': ['account', 'mail'],
    'data': [
        'views/res_partner_views.xml',
        'data/email_templates.xml',
    ],
    'installable': True,
    'application': False,

}
