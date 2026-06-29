import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class OdooSchoolHrHospitalVisit(models.Model):
    _name = 'odoo.school.hr.hospital.visit'
    _description = 'Patient Visit'

    name = fields.Char(string='Name', required=True, default='New Visit')
    active = fields.Boolean(default=True)
    result = fields.Text(string='Result')
    description = fields.Text(string='Description')
    patient_id = fields.Many2one(
        comodel_name='odoo.school.hr.hospital.patient',
        string='Patient',
        required=True,
    )
    doctor_id = fields.Many2one(
        comodel_name='odoo.school.hr.hospital.doctor',
        string='Doctor',
        required=True,
    )
    disease_id = fields.Many2one(
        comodel_name='odoo.school.hr.hospital.disease',
        string='Disease',
    )
    visit_date = fields.Datetime(
        string='Visit Date',
        default=fields.Datetime.now,
        required=True,
    )
