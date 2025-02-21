from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_invoice_sent(self):
        """Override the send invoice method to use the correct email template based on customer type."""
        self.ensure_one()
        email_template = False

        if self.partner_id.customer_type == 'retail':
            email_template = self.env.ref('dynamic_invoice_email.email_template_invoice_retail')
        elif self.partner_id.customer_type == 'wholesale':
            email_template = self.env.ref('dynamic_invoice_email.email_template_invoice_wholesale')

        if email_template:
            email_template.send_mail(self.id, force_send=True)
        return True
