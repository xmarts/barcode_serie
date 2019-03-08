# -*- coding: utf-8 -*-
{
    'name': "Barcode Series",

    'summary': """This module creates a bar code by means of a serial number.""",

    'description' : 
    """
        This module creates a bar code by means of a serial number from 
        each product selected with the option of unique serial number.
    """,

    'author': "Xmarts",
    'website': "https://www.xmarts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/barcode_report.xml',
        'reports/layout.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application' : True,
    'installable' : True
}
