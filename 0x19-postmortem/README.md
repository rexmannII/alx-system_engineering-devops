This task will cover the webstack debugging #1 for the 0x19-Postmortem project.



Issue Summary

Duration of the outage: The outage started at 01:15 PM and got resolved by 04:15 PM West African Time


Impact:
The site was not listening on port 80, causing users unable to access the website

Root Cause:
The Nginx server site settings were not properly linked. This means that the site was not activated at the time, causing users difficulties to access the site.


Timeline:
At 01:15 PM:  This issue was detected when the ALX team attempted to access the website and noticed it was unresponsive.

At 02:10 PM. The ALX monitoring team (alert) indicated that the site was down and the issue was brought to my notice.

I spent closely 1hr 10mins focusing on the Nginx configuration file but no error was found in the files

Then at about 03:20 PM, I discovered that the Nginx configuration in sites-available was not linked to sites-enabled after carrying out further investigation.

At 03;45 PM, the default configuration was correctly linked in sites-enabled and Nginx was restarted to apply the changes.

04:15 PM: the issues had been corrected and the site was back online.





Root Cause and Resolution

Root Cause:
The root cause was the failure to link sites-available configuration to sites-enabled, meaning the Nginx server configuration was not active despite being correct.

Resolution:
The issue was resolved by linking the default configuration from the sites-available to sites-enabled and restarting the Nginx service.



Corrective and Preventive Measures

Improvements:
Making sure that after any configuration changes, a script or automated check is run to confirm that the necessary configurations are linked and active. Improve the monitoring system to detect such problems in time.

Task List:
Build-up and execute a script to link the sites-available configuration to sites-enabled after each configuration change. Add a monitoring check that makes sure that Nginx is correctly ans actively listening to port 80.


Example Script:
Here is the script as mentioned previously to ensure the configuration is always active:
[bash] #!/usr/bin/env bash
Ensure Nginx is properly configured and listening to port 80
cat/etc/nginx/sites-available/default > /etc/nginx/sites-enabled/default sudo service nginx restart

