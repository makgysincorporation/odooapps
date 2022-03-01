
{
    'name': 'Ledger View In Partner',
    'summary': 'Adds smart button to view general ledger from contact',
    'description': '''
This module provide smart clickable button in partner through which general ledger can be viewed directly ''',
    'author': 'Makgys Incorporation Pvt Ltd',
    'version': '15.0.1.0.0',
    'author': "Makgys Incorporation Pvt. Ltd.",
    'category': 'Accounting/Accounting',
    'depends': [
        'dynamic_accounts_report'
    ],
    'data': [
        'views/partner_smart_button_view.xml',
    ],
    'assets': {
       
        'web.assets_backend': [
            'partner_ledger_smart_view/static/src/js/partner_smart_button.js',
            
        ],
        
    },
    'license': 'OPL-1',
    'images': ['static/description/Banner.png'],
    'price': 35.0,
    'currency': 'EUR',
    'installable': True,
    'application': False,
}
