# -*- coding: utf-8 -*-
{
    'name': "twilioSMS",

    'summary': """ App interage twilio sms for odoo 12 """,

    'description': """
       App to setup and send message with twilio
    """,

    'author': "PhucLe",
    'website': "https://innoria.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'SMS app',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/twilio_sms_module.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}