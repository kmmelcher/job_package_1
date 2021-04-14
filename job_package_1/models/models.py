# -*- coding: utf-8 -*-

import base64
from .contract import CONTRACT_BODY
from .helper import find_dynamic_tags

from odoo import models, fields, api, SUPERUSER_ID


class JobPackageFreelancer(models.Model):
    _name = 'job.package.freelancer'
    _description = 'Freelancer'
    _inherit = ['hr.employee', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']


    #Relation between Freelancer and Job
    job_position_ids = fields.Many2many(
        'job.package.job',
        'package_freelancer_job_rel',
        'package_freelancer_id', 'job_position_id', 
        "Applied Job",
        readonly=True)

    #Recruitment process stage (This is where the issue lives)
    stage_id = fields.Many2one('job.package.stage', 'Stage', ondelete='restrict', tracking=True,
                               store=True, readonly=False,
                               copy=False, index=True, group_expand='_read_group_stage_ids')

    #Ignore
    category_ids = fields.Many2many(
        'hr.employee.category', 'job_package_freelancer_category_rel',
        'job_package_freelancer_id', 'category_id')

    #Boolean field to hide/show attachments on the right side of the screen
    show_attachments_preview = fields.Boolean(default=False)

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        """ Return all job process stages to display on freelancers
        stage view """
        stage_ids = stages._search([], order=order, access_rights_uid=SUPERUSER_ID)
        return stages.browse(stage_ids)

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
        
        email_type = self.env.context.get('email_type')
        
        email_attachment_names = list()

        if email_type == '1':
            email_attachment_names = ['Contract1.pdf']

        elif email_type == '2':
            email_attachment_names = ['Contract1.pdf', 'Contract2.pdf']

        elif email_type == '3':
            email_attachment_names = ['Contract3.pdf']
    
        if email_attachment_names:
            attachment_ids = self.env['ir.attachment'].search([('res_model','=',self._name), ('res_id','=', self.id), ('name', 'in', email_attachment_names)])

        else:
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


class Job(models.Model):
    """
    Job Positions model linked to Freelancers
    """
    _name = 'job.package.job'
    _description = "Freelancer's Job Positions"

    name = fields.Char(string='Job Position',help="Job Position's Name", required=True)
    color = fields.Integer("Color Index", default=10)
    is_favorite = fields.Boolean()

    package_freelancer_ids = fields.Many2many(
        'job.package.freelancer', 
        'package_freelancer_job_rel',
        'job_position_id', 'package_freelancer_id', 
        string='Freelancers')


class Stage(models.Model):
    """
    Recruitment Stages model for a freelancer to be recruited in a Job Position.
    """
    _name = 'job.package.stage'
    _description = "Recruitment Stages"
    _order = 'sequence'

    name = fields.Char(string='Name',help="Stage Name", required=True)
    sequence = fields.Integer(
        "Sequence",
        help="Gives the sequence order when displaying a list of stages.")
    fold = fields.Boolean(
        "Folded in Kanban",
        help="This stage is folded in the kanban view when there are no records in that stage to display.")
