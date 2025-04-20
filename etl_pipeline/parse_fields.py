import re

def extract_fields(text):
    return {
        "vendor": re.search(r"Vendor: (.+)", text).group(1) if "Vendor:" in text else None,
        "date": re.search(r"Date: (\d{4}-\d{2}-\d{2})", text).group(1) if "Date:" in text else None,
        "total": re.search(r"Total Charged: \$(\d+\.\d+)", text).group(1) if "Total Charged:" in text else None,
        "contract_id": re.search(r"Contract ID: (CT-\d{4}-\d+)", text).group(1) if "Contract ID:" in text else None,
        "payment_terms": re.search(r"Payment Terms: (.+)", text).group(1) if "Payment Terms:" in text else None,
        "ticket_id": re.search(r"Ticket ID: (\d+)", text).group(1) if "Ticket ID:" in text else None
    }

if __name__ == "__main__":
    sample = open("data/raw_documents/receipt.txt").read()
    fields = extract_fields(sample)
    for k, v in fields.items():
        print(f"{k}: {v}")
