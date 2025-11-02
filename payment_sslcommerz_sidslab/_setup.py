def post_init_hook(env):
    """Post-install script"""
    from odoo.addons.payment import setup_provider
    setup_provider(env, 'sslcommerz')


def uninstall_hook(env):
    """Post-uninstall script"""
    from odoo.addons.payment import setup_provider
    setup_provider(env, 'sslcommerz', uninstall=True)
