/** @odoo-module **/

import publicWidget from '@web/legacy/js/public/public_widget';
import { _t } from '@web/core/l10n/translation';

// Extend the PaymentForm widget to fix the redirect flow issue
publicWidget.registry.PaymentForm.include({
    /**
     * Redirect the customer by submitting the redirect form included in the processing values.
     * This overrides the original method to handle cases where redirectForm might be null.
     *
     * @private
     * @param {string} providerCode - The code of the selected payment option's provider.
     * @param {number} paymentOptionId - The id of the selected payment option.
     * @param {string} paymentMethodCode - The code of the selected payment method, if any.
     * @param {object} processingValues - The processing values of the transaction.
     * @return {void}
     */
    _processRedirectFlow: function (providerCode, paymentOptionId, paymentMethodCode, processingValues) {
        // Create and configure the form element with the content rendered by the server.
        const div = document.createElement('div');
        div.innerHTML = processingValues['redirect_form_html'] || '';
        
        const redirectForm = div.querySelector('form');
        
        if (!redirectForm) {
            // If no redirect form is found, log an error and handle gracefully
            console.error('No redirect form found in processing values for provider:', providerCode);
            
            // If redirect_form_html is empty or malformed, try to find an alternative approach
            // based on the provider implementation or handle the error gracefully
            if (processingValues['return_url']) {
                // If there's a return URL provided, redirect to that
                window.location = processingValues['return_url'];
            } else {
                // Show an error message to the user
                this._displayErrorDialog(
                    _t("Payment Processing Error"), 
                    _t("The payment provider did not return a valid redirect form. Please try again or contact support.")
                );
                this._enableButton(); // Re-enable the button
            }
            return;
        }

        redirectForm.setAttribute('id', 'o_payment_redirect_form');
        redirectForm.setAttribute('target', '_top');  // Ensures redirections when in an iframe.

        // Submit the form.
        document.body.appendChild(redirectForm);
        redirectForm.submit();
    }
});