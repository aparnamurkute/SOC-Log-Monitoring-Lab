# SOC-Log-Monitoring-Lab

##  Objective
Simulate a Security Operations Center (SOC) workflow by monitoring and analyzing server logs for suspicious activities such as brute-force login attempts and abnormal behavior.

##  Tools Used
- Splunk (or ELK Stack) – Log monitoring & dashboards  
- Python – Log parsing & detection rules  
- Sysmon / Sample Apache logs  

##  Methodology
1. Collected sample logs from web servers and authentication systems.  
2. Imported logs into Splunk for indexing and querying.  
3. Created detection rules for suspicious activities (e.g., >5 failed logins/min).  
4. Triggered alerts and documented incident response steps.  

##  Results
- Detected brute-force login attempts from a single IP.  
- Generated SOC alert and response report.  

##  Recommendations
- Enable account lockout policy after multiple failed attempts.  
- Monitor privileged account activity.  
- Regularly review and fine-tune SIEM rules.  

---
