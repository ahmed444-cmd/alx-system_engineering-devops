
# README: Web Stack Outage Postmortem

## Overview

This README summarizes the details of a recent outage experienced on August 14, 2024, and provides insights into the root cause, resolution, and corrective measures taken.

---

## Incident Summary

- **Date and Time**: August 14, 2024, 14:30 - 16:00 UTC
- **Impact**: The API was intermittently unavailable for 40% of users, causing slow response times and failed requests.
- **Root Cause**: Misconfiguration in Nginx load balancer, which led to routing traffic to unhealthy backend servers.

---

## Detailed Timeline

1. **14:30 UTC**: Monitoring alert triggered due to a spike in 5xx errors and increased latency.
2. **14:32 UTC**: Initial investigation focused on API servers, suspecting a memory leak.
3. **14:45 UTC**: API servers restarted, but the issue persisted.
4. **15:00 UTC**: Analysis shifted to the database layer, but slow queries were ruled out as the issue.
5. **15:15 UTC**: Reassessment of the issue revealed potential load balancer misconfigurations.
6. **15:30 UTC**: Load balancer investigation confirmed that Nginx was routing traffic to unhealthy instances.
7. **15:40 UTC**: Nginx configuration updated to route traffic only to healthy instances.
8. **16:00 UTC**: Service restored, and normal operations resumed.

---

## Root Cause and Resolution

**Root Cause**: Nginx was misconfigured to route traffic to unhealthy backend servers due to incorrect health checks. This resulted in elevated error rates and slow responses.

**Resolution**: Corrected Nginx health check configurations to ensure traffic was only routed to healthy servers. Redeployed the load balancer with updated settings.

---

## Corrective and Preventative Measures

### Improvements:
1. **Enhanced Monitoring**: Improve alerting for Nginx health check misconfigurations.
2. **Incident Playbook**: Include load balancer checks as a standard part of the incident response.
3. **Structured Troubleshooting**: Develop a structured approach to investigating similar issues.

### To-Do List:
- [ ] Patch Nginx configuration to ensure accurate health check settings.
- [ ] Implement monitoring alerts for unhealthy instance routing.
- [ ] Conduct monthly audits of the load balancer configuration.
- [ ] Document and review troubleshooting procedures.
- [ ] Schedule a review of the postmortem to identify further improvements.

---

## Blog Summary

In the blog titled "The One Where the Load Balancer Went Rogue," the outage is humorously recounted with a timeline and diagram illustrating the misadventure of the Nginx load balancer. The blog emphasizes the importance of proper configuration and a systematic approach to troubleshooting, with a light-hearted look at how the issue was resolved.

---

## Contact

For questions or further information, please reach out to Joseph Mahiuha at [ahmedelabide@gmail.com](mailto:ahmedelabide@gmail.com).

---

Thank you for reviewing this summary. Your feedback and suggestions are appreciated!

