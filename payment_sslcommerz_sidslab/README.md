SSLCommerz Payment Acquirer

- Version: 18.0.1.0.0
- Author: Md Sidratul Muntaher Tibrow
- Email: msm.tibrow@gmail.com

Description
This module integrates the SSLCommerz payment gateway (widely used in Bangladesh) with Odoo, enabling secure online payment processing for e-commerce websites.

Features
    • Integration with SSLCommerz payment gateway
    • Support for both sandbox and production environments
    • Secure payment processing
    • Credit/debit card payments support
    • Easy configuration with a Store ID and password

Installation
    1. Copy the module into your Odoo custom addons directory.
    2. Restart Odoo.
    3. In Odoo go to Apps → Update Apps List.
    4. Remove all filters in the Apps search bar.
    5. Search for “SSLCommerz Payment Acquirer”.
    6. Click Install.
    7. Ensure Website/Ecommerce module is activated to use this package.

Configuration
    1. Go to Settings → Website → Shop – Payment → Activate Payments → View Alternative.
    2. Select “SSLCommerz”.
    3. Set up the following:
        ◦ Name: SSLCommerz (or your preferred name)
        ◦ Provider: SSLCommerz
        ◦ Store ID: Your SSLCommerz Store ID
        ◦ Store Password: Your SSLCommerz Store Password
        ◦ State: Choose “Enable” (production) or “Test” (sandbox)
        ◦ Enable Card under Payment Methods → Save & Publish
        ◦ Activate BDT currency

Getting SSLCommerz Credentials
    1. Register at the SSLCommerz merchant portal and wait for approval.
    2. Once approved you will receive your Store ID and Store Password.
    3. For testing, use the sandbox credentials provided by SSLCommerz.

Usage
After configuration:
    1. Customer selects SSLCommerz as payment method during checkout.
    2. Customer is redirected to the SSLCommerz secure payment page.
    3. Customer enters payment details and completes payment.
    4. Customer is redirected back to your website with a payment confirmation.
    5. Payment status is automatically updated in Odoo.

Supported Payment Methods
    • Credit Cards (Visa, MasterCard, Amex)
    • Debit Cards
    • Mobile Banking (bKash, Nagad, Rocket, etc.)
    • Other methods supported by SSLCommerz
Security
    • All payment data is processed securely on SSLCommerz servers.
    • Payment processing is PCI DSS compliant.
    • Communication between Odoo and SSLCommerz is encrypted.

Troubleshooting
Issue: Payment not redirecting properly
    • Ensure your store credentials are correct.
    • Confirm your SSLCommerz account is in the correct environment (sandbox vs. production).
Issue: Payment status not updating
    • Ensure Odoo server can receive webhook notifications from SSLCommerz.
    • Verify your server allows required incoming connections and ports.

Support
    • Check SSLCommerz official documentation.
    • Contact your SSLCommerz account manager.
    • Consult with your Odoo implementation partner.

License
This module is licensed under LGPL-3.

Credits
Developed to provide seamless integration between Odoo and SSLCommerz payment gateway for businesses operating in markets where SSLCommerz is a preferred payment method.

