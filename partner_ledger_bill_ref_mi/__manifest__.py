
{
    'name': 'Partner Ledger Reference',
    'summary': 'Adds reference field in Partner Ledger',
    'description': '''
This module provide extra field reference in in partner ledger's move lines ''',
    'author': 'Makgys Incorporation Pvt. Ltd.',
    'version': '15.0.1.0.0',
    'category': 'Accounting/Accounting',
    'depends': [
        'dynamic_accounts_report'
    ],
    'data': [
    ],
    'assets': {
        'web.assets_qweb': [
            'partner_ledger_smart_ref/static/src/xml/partner_ledger_smart_ref.xml',
        ],
    },
     'license': 'OPL-1',
    'images': ['static/description/Banner.png'],
    'price': 13.0,
    'currency': 'EUR',
    'installable': True,
    'application': False,
}
