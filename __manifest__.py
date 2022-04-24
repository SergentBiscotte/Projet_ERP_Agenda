# -*- coding: utf-8 -*-
{
    'name': "erpprojet_Agenda",
    'sequence': 1,
    'summary': "Projet RDV Agenda",

    'description': "Projet RDV Agenda",

    'author': "gr3-22",
    'website': "",
    'category': '',
    'version': '1',
    'license': '',
    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'website', 'website_sale', 'mail'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/appointment_seq.xml',
        'wizard/create_appointment_view.xml',
        'wizard/appointment_report_view.xml',
        'views/patient_view.xml',
        'views/doctor_view.xml',
        'views/department_view.xml',
        'views/appointment_view.xml',
        'views/website_patient_form.xml',
        'views/website_patient_view.xml',
        'views/website_apntment_form.xml',
        'reports/appointment_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
