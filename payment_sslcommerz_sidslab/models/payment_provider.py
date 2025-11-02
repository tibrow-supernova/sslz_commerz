import logging
from odoo import _, api, fields, models


class SslcommerzPaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[('sslcommerz', 'SSLCommerz')],
        ondelete={'sslcommerz': 'set default'}
    )

    sslcommerz_store_id = fields.Char(
        string='SSLCommerz Store ID',
        help='The Store ID provided by SSLCommerz.',
        required_if_provider='sslcommerz',
    )
    sslcommerz_store_password = fields.Char(
        string='SSLCommerz Store Password',
        help='The Store Password provided by SSLCommerz.',
        required_if_provider='sslcommerz',
    )

    def _get_sslcommerz_urls(self):
        """ SSLCommerz URLs """
        self.ensure_one()
        if self.state == 'enabled':
            return {
                'pay_url': 'https://securepay.sslcommerz.com/gwprocess/v4/api.php',
                'validation_url': 'https://securepay.sslcommerz.com/validator/api/validationserverAPI.php',
            }
        else:
            return {
                'pay_url': 'https://sandbox.sslcommerz.com/gwprocess/v4/api.php',
                'validation_url': 'https://sandbox.sslcommerz.com/validator/api/validationserverAPI.php',
            }


    def _get_default_payment_method_id(self):
        self.ensure_one()
        if self.code == 'sslcommerz':
            return self.env.ref('payment.payment_method_card').id
        return super()._get_default_payment_method_id()