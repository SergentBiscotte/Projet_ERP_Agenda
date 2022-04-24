from odoo.exceptions import ValidationError
from odoo import models, fields, api, _


class HospitalAppointment(models.Model):
    _name = 'erpprojet.appointment'
    _description = 'Appointments'
    _order = "id desc"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Appointment Reference', required=True, copy=False, readonly=True,
                       default=lambda self: _('New'))
    patient_id = fields.Many2one("erpprojet.patient", string='Patient Name', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], related='patient_id.gender')
    tel = fields.Char(string='tel', related='patient_id.tel')
    email = fields.Char(string='Email', related='patient_id.email')
    age = fields.Integer(string='Age', related='patient_id.age')
    description = fields.Text()
    note = fields.Text()
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Canceled')
    ], default='draft', required=True, tracking=True)
    appointment_date = fields.Datetime(string='Appointment Date', default=fields.datetime.now(), tracking=True)
    checkup_date = fields.Datetime(string='Checkup Date', required=True, tracking=True)
    appointed_doctor_id = fields.Many2one("erpprojet.doctor", string="Doctor name", required=True)
    prescription_medical_test_ids = fields.Many2many("erpprojet.medicaltest", "medical_test_ids",
                                                     string="Medical tests")

    @api.constrains('appointment_date', 'checkup_date')
    def _check_date_validation(self):
        for record in self:
            if record.checkup_date < record.appointment_date:
                raise ValidationError('Checkup date should not be previous date.')

    # changing the status
    def action_status_draft(self):
        self.status = 'draft'

    def action_status_confirm(self):
        self.status = 'confirm'

    def action_status_done(self):
        self.status = 'done'

    def action_status_cancel(self):
        self.status = 'cancel'

    @api.model
    def create(self, vals):
        if not vals['description']:
            vals['description'] = "Enter the description here"
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('erpprojet.appointment') or _('New')

        res = super(HospitalAppointment, self).create(vals)
        return res

    @api.onchange('patient_id')
    def _change_appointment_note(self):
        if self.patient_id:
            if not self.note:
                self.note = "New appointment"
        else:
            self.note = ""
