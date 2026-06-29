import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class OdooSchoolHrHospitalDisease(models.Model):
    _name = 'odoo.school.hr.hospital.disease'
    _description = 'Disease'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(default=True)
    description = fields.Text(string='Description')
    code = fields.Char(string='Code')

    visit_ids = fields.One2many(
        comodel_name='odoo.school.hr.hospital.visit',
        inverse_name='disease_id',
        string='Visits',
    )
