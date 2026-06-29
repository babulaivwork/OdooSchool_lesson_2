import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class OdooSchoolHrHospitalPatient(models.Model):
    _name = 'odoo.school.hr.hospital.patient'
    _description = 'Patient'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(default=True)
    description = fields.Text(string='Description')
    birth_date = fields.Date(string='Birth Date')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    address = fields.Char(string='Address')
    notes = fields.Text(string='Notes')
    doctor_id = fields.Many2one(
        comodel_name='odoo.school.hr.hospital.doctor',
        string='Attending Doctor',
    )

    visit_ids = fields.One2many(
        comodel_name='odoo.school.hr.hospital.visit',
        inverse_name='patient_id',
        string='Visits',
    )
