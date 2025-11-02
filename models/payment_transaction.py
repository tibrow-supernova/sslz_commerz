import logging
import pprint
import requests
from odoo import _, models, fields
from odoo.exceptions import ValidationError



class SslcommerzPaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    def _get_specific_rendering_values(self, processing_values):
        """
        Override of payment to perform a server-to-server call to SSLCommerz.
        This call gets the unique GatewayPageURL, which is then passed to the redirect form template.
        """

        res = super()._get_specific_rendering_values(processing_values)
        if self.provider_code != 'sslcommerz':
            return res


        provider_sudo = self.sudo().provider_id
        base_url = provider_sudo.get_base_url()

        success_url = f'{base_url}/payment/sslcommerz/return'

        partner_name = self.partner_name or "Odoo Customer"
        partner_email = self.partner_email or "no-email@example.com"
        partner_phone = self.partner_phone or "0000000000"

        api_call_payload = {
            'store_id': provider_sudo.sslcommerz_store_id,
            'store_passwd': provider_sudo.sslcommerz_store_password,
            'total_amount': float(self.amount),
            'currency': self.currency_id.name,
            'tran_id': self.reference,
            'success_url': success_url,
            'fail_url': success_url,
            'cancel_url': success_url,
            'ipn_url': f'{base_url}/payment/sslcommerz/ipn',
            'cus_name': partner_name,
            'cus_email': partner_email,
            'cus_phone': partner_phone,
            'cus_add1': self.partner_address or 'N/A',
            'cus_city': self.partner_city or 'N/A',
            'cus_postcode': self.partner_zip or '0000',
            'cus_country': self.partner_country_id.name if self.partner_country_id else 'Bangladesh',
            'shipping_method': 'NO',
            'product_name': self.reference,
            'product_category': 'ecommerce',
            'product_profile': 'general',
        }


        try:
            # Make the server-to-server request.
            api_url = provider_sudo._get_sslcommerz_urls()['pay_url']
            response = requests.post(api_url, data=api_call_payload, timeout=20)
            response.raise_for_status()
            response_data = response.json()

        except (requests.exceptions.RequestException, ValueError) as e:

            res['api_url'] = ''
            res['error'] = str(e)
            return res

        if response_data.get('status') == 'FAILED':

            error_reason = response_data.get('failedreason', _("Unknown error from payment gateway."))
            res['api_url'] = ''
            res['error'] = error_reason
            return res
        elif response_data.get('status') == 'SUCCESS' and response_data.get('GatewayPageURL'):
            res['api_url'] = response_data['GatewayPageURL']
            return res
        else:
            error_reason = response_data.get('failedreason', _("Unexpected response from payment gateway."))
            res['api_url'] = ''
            res['error'] = error_reason
            return res


    def _get_tx_from_notification_data(self, provider_code, notification_data):
        tx = super()._get_tx_from_notification_data(provider_code, notification_data)
        if provider_code != 'sslcommerz' or len(tx) == 1:
            return tx
        reference = notification_data.get('tran_id')
        if not reference:
            raise ValidationError("SSLCommerz: " + _("Received data with missing transaction reference (tran_id)"))
        tx = self.search([('reference', '=', reference), ('provider_code', '=', 'sslcommerz')])
        if not tx:
            raise ValidationError("SSLCommerz: " + _("No transaction found for reference %s.", reference))
        return tx

    def _process_notification_data(self, notification_data):
        super()._process_notification_data(notification_data)
        if self.provider_code != 'sslcommerz':
            return
        status = notification_data.get('status')
        if status in ('VALID', 'VALIDATED'):
            if not self._sslcommerz_validate_payment(notification_data):
                self._set_error(_("Payment validation failed."))
                return
            self.provider_reference = notification_data.get('val_id')
            self._set_done()

            if self.sale_order_ids:
                for order in self.sale_order_ids:
                    if order.state in ['draft', 'sent']:
                        order.action_confirm()

        elif status == 'FAILED':
            self._set_canceled(_("Payment failed."))
        elif status == 'CANCELLED':
            self._set_canceled(_("Payment was cancelled by the user."))
        else:
            self._set_pending()

    def _sslcommerz_validate_payment(self, data):
        self.ensure_one()
        provider = self.sudo().provider_id
        validation_url = provider._get_sslcommerz_urls()['validation_url']
        params = {
            'val_id': data.get('val_id'),
            'store_id': provider.sslcommerz_store_id,
            'store_passwd': provider.sslcommerz_store_password,
            'format': 'json',
        }
        try:
            response = requests.get(validation_url, params=params, timeout=20)
            response.raise_for_status()
            response_data = response.json()
            if response_data.get('status') in ('VALID', 'VALIDATED'):
                return True
            else:

                return False
        except requests.exceptions.RequestException as e:
            return False