# String methods: startswith() aur endswith()
# Task
#     1. filename = "report.pdf" variable banao.
#     2. Check karo ki filename "report" se start hota hai ya nahi.
#     3. Check karo ki filename ".pdf" par end hota hai ya nahi.
#     4. Dono results print karo.

# Expected output:
    # Starts with report: True
    # Ends with .pdf: True

filename = "report.pdf"
is_start = filename.startswith("report")
is_end = filename.endswith(".pdf")

print(f"Starts with report: {is_start}")
print(f"Ends with .pdf: {is_end}")