{
    'name': 'Odoo School HR Hospital',
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
        'views/odoo_school_hr_hospital_menu_views.xml',
        'views/odoo_school_hr_hospital_doctor_views.xml',
        'views/odoo_school_hr_hospital_patient_views.xml',
        'views/odoo_school_hr_hospital_disease_views.xml',
        'views/odoo_school_hr_hospital_visit_views.xml',
    ],

    'demo': [
    ],

    'images': ['static/description/icon.png'],

    'installable': True,
    'application': False,
    'auto_install': False,
}
