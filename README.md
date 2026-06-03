# Application Security Vulnerability Assessment

**OWASP ZAP | OWASP Juice Shop | DAST Project**

---

## Project Overview

This project demonstrates a **Dynamic Application Security Testing (DAST)** assessment performed on the intentionally vulnerable **OWASP Juice Shop** application using **OWASP ZAP**. The goal was to identify common web application vulnerabilities, analyze their risk using CVSS scoring, and map findings to the OWASP Top 10 framework.

The assessment simulates a real-world application security workflow including scanning, vulnerability analysis, and remediation recommendations.

---

## Tools & Technologies

* OWASP ZAP (DAST scanner)
* OWASP Juice Shop (vulnerable web application)
* Python (vulnerability prioritization script)
* CVSS v3.1 Calculator
* GitHub (documentation and reporting)

---

## Objectives

* Perform automated and passive security testing using OWASP ZAP
* Identify common web application vulnerabilities
* Analyze and classify findings using CVSS scoring
* Map vulnerabilities to OWASP Top 10 categories
* Provide remediation recommendations aligned with security best practices
* Automate vulnerability prioritization using Python

---

## Methodology

1. Deployed OWASP Juice Shop locally using Docker
2. Performed crawling and spidering using OWASP ZAP
3. Conducted active scanning to detect vulnerabilities
4. Collected and analyzed alerts from ZAP
5. Assigned CVSS scores based on severity and impact
6. Mapped each finding to OWASP Top 10 categories
7. Documented findings with evidence and remediation guidance
8. Prioritized vulnerabilities using a Python script

---

## Key Findings

### 1. Content Security Policy (CSP) Not Set

* **Risk Level:** Medium
* **CVSS Score:** 6.5
* **OWASP Top 10:** A05: Security Misconfiguration
* **Description:** Missing CSP header increases risk of client-side injection attacks such as XSS.

---

### 2. CSP Failure to Define Directive

* **Risk Level:** Medium
* **CVSS Score:** 6.5
* **OWASP Top 10:** A05: Security Misconfiguration
* **Description:** Incomplete CSP directives fail to properly restrict resource loading sources.

---

### 3. Cross-Domain Misconfiguration (CORS)

* **Risk Level:** Medium
* **CVSS Score:** 6.5
* **OWASP Top 10:** A05: Security Misconfiguration
* **Description:** Overly permissive cross-origin configuration may allow unauthorized cross-domain access.

---

### 4. HTTP Without Secure Transport

* **Risk Level:** Medium
* **CVSS Score:** 6.9
* **OWASP Top 10:** A02: Cryptographic Failures
* **Description:** Application does not enforce HTTPS, exposing data in transit to potential interception.

---

## CVSS Scoring Approach

CVSS v3.1 was used to evaluate vulnerability severity based on:

* Attack Vector (Network)
* Attack Complexity (Low)
* Privileges Required (None)
* User Interaction (None)
* Impact on Confidentiality, Integrity, and Availability

Scores were assigned based on observed risk and OWASP ZAP findings.

---

## Python Vulnerability Prioritization Script

A simple Python script was developed to sort vulnerabilities by severity and prioritize remediation efforts.

```python
findings = [
    ("CSP Not Set", 6.5),
    ("CORS Misconfiguration", 6.5),
    ("HTTP Without HTTPS", 6.9),
    ("CSP Failure to Define Directive", 6.5)
]

sorted_findings = sorted(
    findings,
    key=lambda x: x[1],
    reverse=True
)

for vuln, score in sorted_findings:
    print(f"{vuln}: {score}")
```

---

## Evidence

Screenshots and scan outputs are included in the `/screenshots` directory, including:

* ZAP Alerts Dashboard
* Spidered site structure
* Active scan results
* Vulnerability details

---

## ️Remediation Summary

Recommended mitigations include:

* Implementing strict Content Security Policy (CSP) headers
* Restricting cross-origin requests (CORS policy hardening)
* Enforcing HTTPS with TLS 1.2+ and HSTS
* Applying secure configuration baselines for web servers
* Validating and sanitizing all user inputs to prevent injection attacks

---

## Key Takeaways

* Automated DAST tools are effective for identifying common web vulnerabilities
* Security misconfigurations are among the most frequently detected issues
* CVSS scoring helps standardize vulnerability prioritization
* Mapping findings to OWASP Top 10 improves real-world relevance
* Even simple automation (Python sorting) improves vulnerability management workflows

---

## Project Structure

```
application-security-assessment/
├── README.md
├── report/
│   └── security-assessment.pdf
├── screenshots/
├── scripts/
│   └── findings.py
```

---

## Future Improvements

* Add authenticated scanning in OWASP ZAP
* Expand testing to include SQL Injection and XSS payload verification
* Automate ZAP scan execution using Python or CI/CD pipeline integration
* Export findings directly into structured JSON reports

---

## Author

**Nivea Mabeya**
Cybersecurity & Application Security Enthusiast
GitHub: https://github.com/nmabeya18

---

## Disclaimer

This project was performed in a controlled, intentionally vulnerable environment (OWASP Juice Shop) for educational and security testing purposes only.
# application-security-assessment
DAST security assessment using OWASP ZAP and OWASP Juice Shop
