# SSLCommerz Payment Acquirer

**Version:** 18.0.1.0.0  
**Author:** Md Sidratul Muntaher Tibrow  
**Email:** `msm.tibrow@gmail.com`

## Description

This module integrates SSLCommerz, a popular payment gateway primarily used in Bangladesh, with Odoo. SSLCommerz enables secure online payment processing for e-commerce websites.

## Features

- Integration with SSLCommerz payment gateway
- Support for both sandbox and production environments
- Secure payment processing
- Support for credit/debit card payments
- Easy configuration with store ID and password

## Installation

1. **Copy the module** to your Odoo custom addons directory:

2. **Update the app list** in Odoo:
   - restart odoo
   - Go to Apps > Update Apps List

3. **Install the module**:
   - Remove all filter from searchbar 
   - Search for "SSLCommerz Payment Acquirer" in the Apps menu 
   - Click Install
   - Also you need to activate website/ecommerce to use this sslcommerz package

## Configuration

1. Go to **Settings > Website > Shop - Payment > Activate Payments > view alternative**
2. Find and click on **SSLCommerz**
3. Set the following parameters:
   - **Name:** SSLCommerz (or your preferred name)
   - **Provider:** SSLCommerz
   - **Store ID:** Your SSLCommerz Store ID
   - **Store Password:** Your SSLCommerz Store Password
   - **State:** Enable to activate (securepay) or Test to activate (sandbox) the provider
   - **Configuration:** Go Enable Payment Methods > Card (Enable it)
   - Then save & publish it

### Getting SSLCommerz Credentials

1. Register at SSLCommerz merchant portal
2. After approval, you will receive your Store ID and Store Password
3. For testing, you can use sandbox credentials provided by SSLCommerz

## Usage

Once configured, customers will be able to select SSLCommerz as a payment method during checkout. The payment flow works as follows:

1. Customer selects SSLCommerz as payment method
2. Customer is redirected to SSLCommerz secure payment page
3. Customer enters payment details and completes payment
4. Customer is redirected back to your website with payment confirmation
5. Payment status is automatically updated in Odoo

## Supported Payment Methods

- Credit Cards (Visa, MasterCard, Amex)
- Debit Cards
- Mobile Banking (bKash, Nagad, Rocket, etc.)

- Other methods supported by SSLCommerz

## Security

- All payment data is processed securely on SSLCommerz servers
- PCI DSS compliant payment processing
- Encrypted communication between Odoo and SSLCommerz

## Troubleshooting

**Issue:** Payment not redirecting properly
- Check your store credentials are correct
- Ensure your SSLCommerz account is in the correct environment (sandbox/production)

**Issue:** Payment status not updating
- Check Odoo server can receive webhook notifications from SSLCommerz
- Verify your server allows incoming connections on the required ports

## Support

For support and further information:
- Check the SSLCommerz official documentation
- Contact your SSLCommerz account manager
- Consult with your Odoo implementation partner

## License

This module is licensed under LGPL-3.

## Credits

This module was developed to provide seamless integration between Odoo and SSLCommerz payment gateway for businesses operating in markets where SSLCommerz is a preferred payment method.