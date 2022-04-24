# -*- coding: utf-8 -*-

from odoo import api, models


class PatientReport(models.AbstractModel):
    _name = 'report.erpprojet.report_patient_card'
    _description = 'Patient Report'

    @api.model
    def _get_report_values(self, docids, data=None):

        docs = self.env['erpprojet.patient'].browse(docids)
        appointments = self.env['erpprojet.appointment'].search([("name", "=", docids)])
        appointment_list = []
        for appointment in appointments:
            values = {
                "checkup_date": appointment.checkup_date,
                "status": appointment.status,
                "appointed_doctor_id": appointment.appointed_doctor_id.name,
            }
            appointment_list.append(values)
        return {
            'doc_model': 'erpprojet.patient',
            'data': data,
            'docs': docs,
            'appointment_list': appointment_list,
        }
