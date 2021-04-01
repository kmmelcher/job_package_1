# -*- coding: utf-8 -*-

import base64
from odoo import models, fields, api
from .contract import CONTRACT_BODY
from .helper import find_dynamic_tags

class JobPackageFreelancer(models.Model):
    _name = 'job.package.freelancer'
    _description = 'Freelancer'
    _inherit = ['hr.employee', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']
    _description = 'Freelancer for job package'

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

    def get_contract_html_dynamic(self):
        """
        This method get the list of dynamic tags in the contract body
        by calling 'find_dynamic_tags' and then replaces 
        the value 
        """
        contract_body = self.contract_body
        dynamic_tags = find_dynamic_tags(contract_body, '${', '}')
        for tag in dynamic_tags:
            tag_attr = tag.replace('${object.', '').replace('}', '')
            if tag_attr == 'page_break':
                contract_body = contract_body.replace(tag, '<div class="page" style="page-break-before:always;"/>')
            elif getattr(self, tag_attr):
                contract_body = contract_body.replace(tag, getattr(self, tag_attr))
            else:
                contract_body = contract_body.replace(tag, "")
        return contract_body

    def action_get_attachment(self):
        """ 
        This method generates a new attachment with contract body pdf 
        """
        report_type = self.env.context.get('report_type')
        if report_type == 'report_1':
            report_id = 'job_package_1.report_sample_1'
            report_name = 'Contract1.pdf'

        elif report_type == 'report_2':
            report_id = 'job_package_1.report_sample_2'
            report_name = 'Contract2.pdf'

        elif report_type == 'report_3':
            report_id = 'job_package_1.report_sample_3'
            report_name = 'Contract3.pdf'
    
        elif report_type == 'report_4':
            report_id = 'job_package_1.report_sample_4'
            report_name = 'Contract4.pdf'

        self.env['ir.attachment'].search([('res_model','=',self._name), ('res_id','=', self.id), ('name', '=', report_name)]).unlink()
        pdf = self.env.ref(report_id)._render_qweb_pdf(self.ids)

        return {
              'type': 'ir.actions.client',
              'tag': 'reload',
        }
    
    def action_get_all_attachment(self):
        """
        This method is called when record is saved/updated
        to update all the contract reports. But 
        the user has to do manual page refresh.
        """
        report_data = [{'report_id': 'job_package_1.report_sample_{}'.format(x), 'report_name':'Contract{}.pdf'.format(x)} for x in range(1,5)]
        for report_info in report_data:
            report_id = report_info.get('report_id')
            report_name = report_info.get('report_name')
            self.env['ir.attachment'].search([('res_model','=',self._name), ('res_id','=', self.id), ('name', '=', report_name)]).unlink()
            pdf = self.env.ref(report_id)._render_qweb_pdf(self.ids)

    def action_email_send(self):
        ''' Opens a wizard to compose an email, with relevant mail template loaded by default '''
        self.ensure_one()
        template_id = self.env.ref("job_package_1.freelancer_email_template").id
        lang = self.env.context.get('lang')
        template = self.env['mail.template'].browse(template_id)
        if template.lang:
            lang = template._render_lang(self.ids)[self.id]
        attachment_ids = self.env['ir.attachment'].search([('res_model','=',self._name), ('res_id','=', self.id)])
        context = {
            'default_model': 'job.package.freelancer',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'force_email': True,
            'default_attachment_ids':[(6, 0, attachment_ids.ids)]
        }
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(False, 'form')],
            'view_id': False,
            'target': 'new',
            'context': context,
        }