{
    'name': 'SSLCommerz Payment Acquirer',
    'version': '18.0.1.0.0',
    'category': 'Accounting/Payment Acquirers',
    'summary': 'Payment Acquirer: SSLCommerz Implementation',
    'author': 'Md Sidratul Muntaher Tibrow',
    'website': 'https://github.com/tibrow-supernova',
    'depends': ['payment', 'website_sale'],
    'images': ['static/description/icon.png'],
    'data': [
        'security/ir.model.access.csv',
        'views/payment_sslcommerz_templates.xml',
        'views/payment_provider_views.xml',
        'data/payment_provider_data.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'payment_sslcommerz/static/src/js/payment_form.js',
        ],
    },
    'post_init_hook': '_sslcommerz_post_init_hook',
    'uninstall_hook': '_sslcommerz_uninstall_hook',
    'license': 'LGPL-3',
    'application': True,
    'price': 180.0,
    'currency': 'USD',
}
