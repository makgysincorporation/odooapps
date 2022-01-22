# -*- coding: utf-8 -*-


{
    'name': 'Website CRM Email Validation',
    'category': 'Website',
    'summary': 'This module allows email validation in website crm form.',
    'description': """
    User can only submit the form with correct email validation 
""",
    'author': "Makgys Incorporation Pvt. Ltd.",
     'license':  'Other proprietary',
    'price': 30.00,
    'currency': 'EUR',
    'version': '13.0.1.0',
    'depends': ['website','website_crm'],
    # 'qweb': ['static/src/xml/website_crm_email_message.xml'],
     'images' :  ['static/description/Banner.png'],
    'data': [
        'views/website_crm_email_template.xml',
    ],
    'installable': True,
    'auto_install': False,
}