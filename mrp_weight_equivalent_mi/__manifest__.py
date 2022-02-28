
{
    'name': 'Mrp Weight In Equivalent',
    'summary': 'Adds Weight Equivalent of Products unit in mrp order',
    'description': '''
This module offers individual kg weight,total kg weight equivalent of product unit in manufacture order finished product,component product line,
    by product product line ''',
    'author': 'Makgys Incorporation Pvt Ltd',
    'version': '14.0.1.0.0',
    'category': 'Manufacturing',
    'depends': [
        'mrp',
    ],
    'data': [
        'views/weight_equivalent_view.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'OPL-1',
    'images': [
        'static/description/Banner.png'
    ],
    'price': 15.0,
    'currency': 'EUR',
}
