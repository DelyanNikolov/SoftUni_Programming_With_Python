import re
number_of_barcodes = int(input())

valid_barcode_pattern = r"@#+([A-Z][A-Za-z0-9]{5,}(?<=[A-Z]))@#+"
product_group_pattern = r"\d"
for code in range(number_of_barcodes):
    barcode = input()
    valid_barcodes = re.findall(valid_barcode_pattern, barcode)
    if not valid_barcodes:
        print("Invalid barcode")
    for group in valid_barcodes:
        product_group = "".join(re.findall(product_group_pattern, group))
        if not product_group:
            product_group = "00"
        print(f"Product group: {product_group}")
