# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import re
import logging
from odoo.exceptions import ValidationError
from odoo import models, fields, api
from twilio.rest import TwilioRestClient
from twilio import TwilioRestException
_logger = logging.getLogger(__name__)

# Provide account value and token on below line

class TwilioSMSModule(models.Model):
    _name = 'twilio.sms.module'

    name = fields.Char(string="Name", required=True)
    account_sid = fields.Char(required=True)
    authen_token = fields.Char(required=True)
    phone_number = fields.Char(description="A phone number that will be send a SMS", string="Phone number send SMS",required=False)
    default = fields.Boolean(string="Using")

    @api.constrains('phone_number')
    def check_mobile(self):
        regex = '(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
        res = re.search(regex, self.phone_number)
        if (res == None):
            raise ValidationError(_("Phone number invalid"))
        return True

    @api.constrains('default')
    def check_default(self):
        print("check default")
        if(self.default) :
            default_record = self.sudo().search_read([('default', '=', True), ('id', '!=', self.id)])
            for item in default_record:
                self.sudo().search([('id', '=', item.get('id'))]).write({'default': False})
        else:
            default_record = self.sudo().search_read([('default', '=', True)])
            if(not len(default_record)):
                raise ValidationError(_("You must be setup least one phone number default"))
        return True

    @api.model
    def sendsms(self, params):
        default_record = self.sudo().search_read([('default', '=', True)])
        if(len(default_record)) :
            if(default_record[0].get('account_sid') != None and default_record[0].get('authen_token') != None):
                client = TwilioRestClient(account=default_record[0].get('account_sid'), token=default_record[0].get('authen_token'))
                if(params.get('to') != None and params.get('message') != None):
                    try:
                        client.messages.create(from_=default_record[0].get('phone_number'), to=params.get('to'), body=params.get('message'))
                    except TwilioRestException as e:
                        _logger.info(e)
                        return None
                else:
                    return None
            else:
                return None
        else:
            return None

