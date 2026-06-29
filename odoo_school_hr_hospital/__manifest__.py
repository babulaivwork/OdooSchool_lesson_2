{
    'name': 'Odoo School HR Hospital',
    'author': 'Odoo School Student',
    'website': 'https://odoo.school/',
    'category': 'Customizations',
    'version': '19.0.1.0.0',
    'license': 'OPL-1',
    'summary': 'Educational hospital module for Odoo School',
    'description': """
Educational module for managing doctors, patients, disease types, and patient visits.
""",

    'depends': [
        'base'
    ],

    'external_dependencies': {
        'python': []
    },

    'data': [
        'security/ir.model.access.csv',
        'data/disease_data.xml',
        'views/menu_views.xml',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/disease_views.xml',
        'views/visit_views.xml',
    ],

    'demo': [
        'demo/doctor_demo.xml',
        'demo/patient_demo.xml',
    ],

    'images': ['static/description/icon.png'],

    'installable': True,
    'application': False,
    'auto_install': False,
}
