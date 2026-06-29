{
    'name': 'Oddo School Library',
    'author': 'Odoo School Student',
    'website': 'https://odoo.school/',
    'category': 'Customizations',
    'version': '19.0.1.0.0',
    'license': 'OPL-1',

    'depends': [
        'base'
    ],

    'external_dependencies': {
        'python': []
    },

    'data': [
        'security/ir.model.access.csv',
        'views/odoo_school_library_menu.xml',
        'views/odoo_school_library_book_views.xml',
    ],

    'demo': [
        'demo/res_partner_demo.xml',
        'demo/odoo.school.library.book.csv',
    ],

    'images': ['static/description/icon.png'],

    'installable': True,
    'application': False,
    'auto_install': False,
}