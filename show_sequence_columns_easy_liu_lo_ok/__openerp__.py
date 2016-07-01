{
    'name': 'Dynamic ListView Advance v9. (You can save 20% when you pay by Paypal)',
    'summary': 'Change The Odoo List view On the fly without any technical knowledge. (You can save 20% when you pay by Paypal)',
    'version': '1.0',
    'category': 'Web',
    'description': """

    """,
    'author': "Hanel Software Solution",
    'website': 'http://www.hanelsoft.vn/',
    'depends': ['web'],
    'data': ['templates.xml',
             'security/show_fields_security.xml',
             'security/ir.model.access.csv'],
    'price': 199.99,
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    'application': False,
    'qweb': ['static/src/xml/listview_button_view.xml'],
    'images': [
        'static/description/1.jpg',
        'static/description/2.jpg',
        'static/description/3.jpg',
    ],
}
