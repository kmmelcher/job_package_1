# -*- coding: utf-8 -*-

from odoo import models, fields, api

class JobPackageFreelancer(models.Model):
    _name = 'job.package.freelancer'
    _description = 'Freelancer'
    _inherit = 'hr.employee'

    #Ignore
    category_ids = fields.Many2many(
        'hr.employee.category', 'job_package_freelancer_category_rel',
        'job_package_freelancer_id', 'category_id')

    #Boolean field to hide/show attachments on the right side of the screen
    show_attachments_preview = fields.Boolean(default=False)

    def show_attachments(self):
        """ Show attachments preview
        It shows on the right side of the form view, but only
        with screen resolutions with width > 1533px """
        self.update({'show_attachments_preview': True})
        
    def hide_attachments(self):
        """ Hide attachments preview """
        self.update({'show_attachments_preview': False,})
