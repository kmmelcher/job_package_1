# -*- coding: utf-8 -*-

import base64
from odoo import models, fields, api
from .contract import CONTRACT_BODY
from .helper import find_dynamic_tags

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

    contract_body = fields.Html(string='Contract Body', translate=True, default=CONTRACT_BODY)

    @api.model
    def create(self, vals):
        """
        This overrides the create method to update
        the contract body  and calls 'set_contract_html_dynamic' method
        to set values in the contract body in vals.
        """
        if vals.get("contract_body"):
            contract_body = vals.get('contract_body')
            vals['contract_body'] = self.set_contract_html_dynamic(contract_body, vals)
        res = super(JobPackageFreelancer, self).create(vals)
        return res

    def write(self, vals):
        """
        This overrides the write method to update
        the contract body and calls 'set_contract_html_dynamic' method
        to set values in the contract body in vals.
        """
        if vals.get("contract_body"):
            contract_body = vals.get('contract_body')
            vals['contract_body'] = self.set_contract_html_dynamic(contract_body)
        res = super(JobPackageFreelancer, self).write(vals)
        return res

    def set_contract_html_dynamic(self, contract_body, vals={}):
        """
        This method get the list of dynamic tags in the contract body
        by calling 'find_dynamic_tags' and then replaces 
        the value 
        """
        dynamic_tags = find_dynamic_tags(contract_body, '${', '}')
        for tag in dynamic_tags:
            tag_attr = tag.replace('${object.', '').replace('}', '')
            if getattr(self, tag_attr):
                contract_body = contract_body.replace(tag, getattr(self, tag_attr))
            elif vals.get(tag_attr):
                contract_body = contract_body.replace(tag, vals.get(tag_attr))
            else:
                contract_body = contract_body.replace(tag, "")
        return contract_body

    def action_get_attachment(self):
        """ this method generates a new attachment with contract body pdf """
        self.env['ir.attachment'].search([('res_model','=',self._name), ('res_id','=', self.id)]).unlink()
        pdf = self.env.ref('job_package_1.report_sample')._render_qweb_pdf(self.ids)
        return {
              'type': 'ir.actions.client',
              'tag': 'reload',
        }