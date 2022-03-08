
{
    'name': 'Partner Ledger Bill Reference',
    'summary': 'Adds bill reference View in Partner Ledger',
    'description': '''
This module provide extra field bill reference in in partner ledger's move lines ''',
    'author': 'Makgys Incorporation Pvt. Ltd.',
    'version': '13.0.1.0.0',
    'category': 'Accounting/Accounting',
    'depends': [
        'dynamic_accounts_report'
    ],
    'data': [
    ],
    'qweb': [
        'static/src/xml/partner_ledger_bill_ref.xml',
    ],
     'license': 'OPL-1',
    'images': ['static/description/Banner.png'],
    'price': 13.0,
    'currency': 'EUR',
    'installable': True,
    'application': False,
}
