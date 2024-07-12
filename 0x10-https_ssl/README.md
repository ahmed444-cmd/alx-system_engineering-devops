0x10. HTTPS SSL
World Wide Web Configuration
Configure your domain to ensure that the subdomain www points to your load balancer IP (lb-01). Additionally, add other subdomains for easier management, and write a Bash script to display information about these subdomains.

Requirements:

Add the subdomain www to your domain, pointing it to your lb-01 IP. (You may remove any default subdomains if needed.)
Add the subdomain lb-01 to your domain, pointing it to your lb-01 IP.
Add the subdomain web-01 to your domain, pointing it to your web-01 IP.
Add the subdomain web-02 to your domain, pointing it to your web-02 IP.
Bash Script:

The script must accept two arguments:

domain: (string) The domain name to audit (mandatory).
subdomain: (string) A specific subdomain to audit (optional).
Output:

If only the domain parameter is provided, display information for the subdomains www, lb-01, web-01, and web-02 in that order.
If both domain and subdomain parameters are provided, display information for the specified subdomain.
Output format: The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION].
Constraints:

Ignore shellcheck case SC2086.
Must use awk at least once.
Must include at least one Bash function.
Note:

You do not need to handle edge cases such as empty parameters, nonexistent domain names, or nonexistent subdomains.
HAproxy SSL Termination
Objective: Configure HAproxy to handle SSL termination, meaning it will accept encrypted traffic, decrypt it, and forward it to its destination.

Steps:

Create a certificate using certbot.
Configure HAproxy to accept encrypted traffic for your www subdomain.
Requirements:

HAproxy must listen on TCP port 443.
HAproxy must accept SSL traffic.
HAproxy must serve encrypted traffic that returns the root (/) of your web server.
When querying the root of your domain, the returned page must contain "Holberton School".
Share your HAproxy configuration file (/etc/haproxy/haproxy.cfg) as an answer file named 1-haproxy_ssl_termination.
Note:

Ensure you have installed HAproxy version 1.5 or higher, as SSL termination is not available in earlier versions.
