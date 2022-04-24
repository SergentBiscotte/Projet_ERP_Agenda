from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class HospitalPatient(models.Model):
    _name = 'erpprojet.patient'
    _description = 'Hospital Patient'
    _order = 'id desc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Patient Name', required=True, tracking=True)
    address = fields.Char(string='Address', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], default="male", tracking=True)
    tel = fields.Char(string='tel', required=True, tracking=True)
    age = fields.Integer(string='Age', required=True, tracking=True)
    email = fields.Char(string='Email', tracking=True)
    patient_appointment_ids = fields.One2many('erpprojet.appointment', 'patient_id', string="Appointment Count",
                                              readonly=True)
    total_appointments = fields.Integer(string='No. of appointments', compute='_compute_appointments')

    # check if the patient is already exists based on the patient name and phone number
    @api.constrains('name', 'tel')
    def _check_patient_exists(self):
        for record in self:
            patient = self.env['erpprojet.patient'].search(
                [('name', '=', record.name), ('tel', '=', record.tel), ('id', '!=', record.id)])
            if patient:
                raise ValidationError(f'Patient {record.name} already exists')

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            valid_email = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
                                   record.email)
            if valid_email is None:
                raise ValidationError('Entrer un email valide')

    @api.constrains('age')
    def _check_patient_age(self):
        for record in self:
            if record.age <= 0:
                raise ValidationError('Age incorrecte')

    # compute appointments of individual patient
    def _compute_appointments(self):
        for record in self:
            record.total_appointments = self.env['erpprojet.appointment'].search_count(
                [('patient_id', '=', record.id)])
