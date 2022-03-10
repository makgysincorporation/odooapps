{
    'name': 'Stock Picking Backdate',
    'version': '14.0.1.0.0',
    'category': 'Extra Tools',
    'author': 'Makgys Incorporation Pvt. Ltd.',
    'summary': 'assigning backdate to picking',
    'depends': [
        'stock','account'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/change_to_backdate_wiz.xml',
        'views/stock_picking_backdate_action.xml'
    ],
    'license': 'OPL-1',
    'images': ['static/description/Banner.png'],
    'price': 60.0,
    'currency': 'EUR',
    'application': False,
    'installable': True,
    'auto_install': False,
}
