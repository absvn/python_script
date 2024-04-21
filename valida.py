from domain_validation.whois import WHOIS

temp = WHOIS("arya.com")

print("Creation Date:", temp.creation_date())
print("Registrar:", temp.registrar())

# import requests

# def ping_url(url):
#     try:
#         response = requests.head(url, timeout=5)  
#         if response.status_code == 200:
#             return True, "URL is reachable."
#         else:
#             return False, f"URL returned status code: {response.status_code}"
#     except requests.ConnectionError:
#         return False, "Failed to connect to the URL."
#     except requests.Timeout:
#         return False, "Request timed out."

# url = "https://0.0.0.0:8000/"
# reachable, message = ping_url(url)
# if reachable:
#     print(message)
# else:
#     print("Ping failed:", message)



# from email_validator import validate_email, EmailNotValidError

# email = "aasdfgh@dacg*u.com"

# try:
#   emailinfo = validate_email(email, check_deliverability=False)
#   email = emailinfo.normalized
#   print(emailinfo)

# except EmailNotValidError as e:
#   print(str(e))

# import re
# import smtplib
# import dns.resolver

# def validate_email(email):
#     # Regular expression pattern for email validation
#     pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
#     if not re.match(pattern, email):
#         return False, "Invalid email format"

#     domain = email.split('@')[1]

#     try:
#         # Resolve MX records for the domain
#         mx_records = dns.resolver.resolve(domain, 'MX')
#         if len(mx_records) > 0:
#             return True, "Email domain exists"
#         else:
#             return False, "Email domain does not exist"
#     except dns.resolver.NoAnswer:
#         return False, "No MX records found for the domain"
#     except dns.resolver.NXDOMAIN:
#         return False, "Domain does not exist"

# # Example usage:
# email = "example@example.com"
# is_valid, message = validate_email(email)
# print(message)