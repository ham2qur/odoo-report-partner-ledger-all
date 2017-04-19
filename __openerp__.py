# -*- coding: utf-8 -*-
{
    'name': "wtm_custom",

    'summary': """
        Odoo customized module for odoo partner ledger all accounts""",

    'description': """
        Customizations Details:
    """,

    'author': "ham2qur",
    'website': "http://www.uok-ubit.blogspot.com",

    'category': 'account',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}