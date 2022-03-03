# -*- coding: utf-8 -*-
{
    'name': "Approvals Purchase Requester",

    'summary': """
        Adds Extra layer of validation in purchase request
        """,

    'description': """
        This module adds extra layer of workflow in stage where approval of purchase order will have to go through it
    """,

    'author': "Makgys Incorporation Pvt. Ltd.",

    'category': 'Purchase',
    'version': '14.0.1.0.0',

    'depends': ['base','approvals','purchase'],
    
    'data': [
        'data/approval_data.xml',
        'data/approvals_security.xml',
        'views/initial_approval_view.xml',
    ],
    'license': 'OPL-1',
    'images': ['static/description/Banner.png'],
    'price': 25.0,
    'currency': 'EUR',
    'installable': True,
    'application': False,
   
}
