# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class erpprojet(http.Controller):

    @http.route('/patient_webform', type='http', auth='user', website=True)
    def patient_webform(self, **kw):
        return http.request.render('erpprojet.create_patient', {})

    @http.route('/create/webpatient', type="http", auth="user", website=True)
    def create_webpatient(self, **kw):
        # print("\nData Received.....", kw)
        request.env['erpprojet.patient'].sudo().create(kw)
        return request.render("erpprojet.patient_thanks", {})

    # route affichant toutes les informations d'un patient
    @http.route('/patient_view', type='http', auth='public', website=True)
    def view_patient_web(self, **kw):
        patients = request.env['erpprojet.patient'].sudo().search([])
        # print("\nData Received.....", patients)
        return http.request.render('erpprojet.view_patient', {
            'patients': patients
        })

    # route for appointment website
    @http.route('/appointment_webform', type='http', auth='user', website=True)
    def appointment_webform(self, **kw):
        patient_rec = request.env['erpprojet.patient'].sudo().search([])
        doctor_rec = request.env['erpprojet.doctor'].sudo().search([])
        return http.request.render('erpprojet.create_appointment', {
            'patient_rec': patient_rec,
            'doctor_rec': doctor_rec
        })

    @http.route('/create/webappointment', type="http", auth="user", website=True)
    def create_webappointment(self, **kw):
        print("\nData Received.....", kw)
        request.env['erpprojet.appointment'].sudo().create(kw)
        return request.render("erpprojet.appointment_thanks", {})