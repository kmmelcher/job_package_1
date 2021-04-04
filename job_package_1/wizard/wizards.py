# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ReportGenerationWizard(models.TransientModel):

    _name = 'job.package.freelancer.report.generation'
    _description = "Report Generation Wizard"

    contract_report_type = fields.Selection([
            ('report_1', 'Report 1'),
            ('report_2', 'Report 2'),
            ('report_3', 'Report 3'),
            ('report_4', 'Report 4'),
        ], default='report_1', required=True)


    def generate_contract_report(self):
        """
        This method identifies the type of report
        to be generated and saves it to the freelancer
        record.
        """
        freelancer_obj = self.env[self.env.context.get('active_model')].browse(self.env.context.get('active_id'))
        return freelancer_obj.with_context({'report_type':self.contract_report_type}).action_get_attachment()


class SendEmailWizard(models.TransientModel):

    _name = 'job.package.freelancer.send.email'
    _description = "Send Freelancer Email Wizard"

    def send_email_1(self):
        """
        This method identifies the type of email as '1' and 
        calls method action_email_send of the freelancer obj. with 
        email_type as 1. 
        """
        freelancer = self.env[self.env.context.get('active_model')].browse(self.env.context.get('active_id'))
        return freelancer.with_context({'email_type':'1'}).action_email_send()

    def send_email_2(self):
        """
        This method identifies the type of email as '2' and 
        calls method action_email_send of the freelancer obj. with 
        email_type as 2. 
        """
        freelancer = self.env[self.env.context.get('active_model')].browse(self.env.context.get('active_id'))
        return freelancer.with_context({'email_type':'2'}).action_email_send()

    def send_email_3(self):
        """
        This method identifies the type of email as '3' and 
        calls method action_email_send of the freelancer obj. with 
        email_type as 3. 
        """
        freelancer = self.env[self.env.context.get('active_model')].browse(self.env.context.get('active_id'))
        return freelancer.with_context({'email_type':'3'}).action_email_send()