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