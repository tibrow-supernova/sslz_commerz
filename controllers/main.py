import logging
import pprint
from odoo import http
from odoo.http import request


class SslcommerzController(http.Controller):
    _return_url = '/payment/sslcommerz/return'
    _ipn_url = '/payment/sslcommerz/ipn'

    @http.route(_return_url, type='http', auth='public', methods=['POST', 'GET'], csrf=False, save_session=False)
    def sslcommerz_return(self, **post):

        try:
            if not post:
                return request.redirect('/shop/payment')

            tx = request.env['payment.transaction'].sudo()._handle_notification_data('sslcommerz', post)

            if tx and tx.state == 'done':
                return_url = '/shop/payment/validate'
            else:
                return_url = '/shop/payment'

        except Exception as e:
            return_url = '/shop/payment'

        # Redirect to appropriate page
        return request.redirect(return_url)

    @http.route(_ipn_url, type='http', auth='public', methods=['POST'], csrf=False, save_session=False)
    def sslcommerz_ipn(self, **post):

        try:
            if not post:
                return http.Response("No data", status=400)

            request.env['payment.transaction'].sudo()._handle_notification_data('sslcommerz', post)

            return http.Response("OK", status=200)

        except Exception as e:
            return http.Response("Error", status=500)