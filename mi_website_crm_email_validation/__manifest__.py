# -*- coding: utf-8 -*-


{
    'name': 'Website CRM Email Validation',
    'category': 'Website',
    'summary': 'This module allows email validation in website crm form.',
    'description': """
    User can only submit the form with correct email validation 
""",
    'author': "Makgys Incorporation Pvt. Ltd.",
    'version': '13.0.1.0',
    'depends': ['website','website_crm'],
     'images' :  ['static/description/Banner.png'],
    'license': 'AGPL-3',

    'data': [
        'views/website_crm_email_template.xml',
    ],
    'installable': True,
    'auto_install': False,
}