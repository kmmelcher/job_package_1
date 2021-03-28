# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ReportGenerationWizard(models.TransientModel):

    _name = 'job.package.freelancer.report.generation'

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