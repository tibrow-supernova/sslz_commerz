<h1>SSLCommerz Payment Acquirer</h1>

<p><strong>Version:</strong> 18.0.1.0.0<br>
<strong>Author:</strong> Md Sidratul Muntaher Tibrow<br>
<strong>Email:</strong> <code>msm.tibrow@gmail.com</code></p>

<h2>Description</h2>

<p>This module integrates SSLCommerz, a popular payment gateway primarily used in Bangladesh, with Odoo. SSLCommerz enables secure online payment processing for e-commerce websites.</p>

<h2>Features</h2>

<ul>
<li>Integration with SSLCommerz payment gateway</li>
<li>Support for both sandbox and production environments</li>
<li>Secure payment processing</li>
<li>Support for credit/debit card payments</li>
<li>Easy configuration with store ID and password</li>
</ul>

<h2>Installation</h2>

<ol>
<li><strong>Copy the module</strong> to your Odoo custom addons directory:</li>

<li><strong>Update the app list</strong> in Odoo:
   <ul>
   <li>restart odoo</li>
   <li>Go to Apps > Update Apps List</li>
   </ul></li>

<li><strong>Install the module</strong>:
   <ul>
   <li>Remove all filter from searchbar</li>
   <li>Search for "SSLCommerz Payment Acquirer" in the Apps menu</li>
   <li>Click Install</li>
   <li>Also you need to activate website/ecommerce to use this sslcommerz package</li>
   </ul></li>
</ol>

<h2>Configuration</h2>

<ol>
<li>Go to <strong>Settings > Website > Shop - Payment > Activate Payments > view alternative</strong></li>
<li>Find and click on <strong>SSLCommerz</strong></li>
<li>Set the following parameters:
   <ul>
   <li><strong>Name:</strong> SSLCommerz (or your preferred name)</li>
   <li><strong>Provider:</strong> SSLCommerz</li>
   <li><strong>Store ID:</strong> Your SSLCommerz Store ID</li>
   <li><strong>Store Password:</strong> Your SSLCommerz Store Password</li>
   <li><strong>State:</strong> Enable to activate (securepay) or Test to activate (sandbox) the provider</li>
   <li><strong>Configuration:</strong> Go Enable Payment Methods > Card (Enable it)</li>
   <li>Then <strong>save &amp; publish</strong> it</li>
   <li>Activate <strong>BDT</strong> currency</li>
   </ul></li>
</ol>

<h3>Getting SSLCommerz Credentials</h3>

<ol>
<li>Register at SSLCommerz merchant portal</li>
<li>After approval, you will receive your Store ID and Store Password</li>
<li>For testing, you can use sandbox credentials provided by SSLCommerz</li>
</ol>

<h2>Usage</h2>

<p>Once configured, customers will be able to select SSLCommerz as a payment method during checkout. The payment flow works as follows:</p>

<ol>
<li>Customer selects SSLCommerz as payment method</li>
<li>Customer is redirected to SSLCommerz secure payment page</li>
<li>Customer enters payment details and completes payment</li>
<li>Customer is redirected back to your website with payment confirmation</li>
<li>Payment status is automatically updated in Odoo</li>
</ol>

<h2>Supported Payment Methods</h2>

<ul>
<li>Credit Cards (Visa, MasterCard, Amex)</li>
<li>Debit Cards</li>
<li>Mobile Banking (bKash, Nagad, Rocket, etc.)</li>
<li>Other methods supported by SSLCommerz</li>
</ul>

<h2>Security</h2>

<ul>
<li>All payment data is processed securely on SSLCommerz servers</li>
<li>PCI DSS compliant payment processing</li>
<li>Encrypted communication between Odoo and SSLCommerz</li>
</ul>

<h2>Troubleshooting</h2>

<p><strong>Issue:</strong> Payment not redirecting properly</p>
<ul>
<li>Check your store credentials are correct</li>
<li>Ensure your SSLCommerz account is in the correct environment (sandbox/production)</li>
</ul>

<p><strong>Issue:</strong> Payment status not updating</p>
<ul>
<li>Check Odoo server can receive webhook notifications from SSLCommerz</li>
<li>Verify your server allows incoming connections on the required ports</li>
</ul>

<h2>Support</h2>

<p>For support and further information:</p>
<ul>
<li>Check the SSLCommerz official documentation</li>
<li>Contact your SSLCommerz account manager</li>
<li>Consult with your Odoo implementation partner</li>
</ul>

<h2>License</h2>

<p>This module is licensed under LGPL-3.</p>

<h2>Credits</h2>

<p>This module was developed to provide seamless integration between Odoo and SSLCommerz payment gateway for businesses operating in markets where SSLCommerz is a preferred payment method.</p>