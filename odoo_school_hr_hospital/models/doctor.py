import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class OdooSchoolHrHospitalDoctor(models.Model):
    _name = 'odoo.school.hr.hospital.doctor'
    _description = 'Doctor'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(default=True)
    specialty = fields.Char(string='Specialty')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    notes = fields.Text(string='Notes')

    visit_ids = fields.One2many(
        comodel_name='odoo.school.hr.hospital.visit',
        inverse_name='doctor_id',
        string='Visits',
    )
