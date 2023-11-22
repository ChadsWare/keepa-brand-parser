import json
import urllib.parse
import webbrowser

def read_brands_from_file(file_name):
    with open(file_name, 'r') as file:
        brands = file.read().splitlines()
    return brands

def chunk_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

if __name__ == "__main__":
    input_file_name = 'brands.txt'  # Replace with your input file name
    url = 'https://keepa.com/#!finder/'

    brands = read_brands_from_file(input_file_name)
    chunked_brands = chunk_list(brands, 50)
    
    for chunk in chunked_brands:
        payload = {
            "f": {
                "brand": {
                    "filterType": "autocomplete",
                    "filter": '###'.join(chunk),
                    "type": "isOneOf"
                },
                "SALES_current": {
                    "filterType": "number",
                    "type": "lessThanOrEqual",
                    "filter": 150000,
                    "filterTo": None
                },
                "SALES_deltaPercent90": {
                    "filterType": "number",
                    "type": "greaterThanOrEqual",
                    "filter": 50,
                    "filterTo": None
                },
                "buyBoxIsFBA": {
                    "filterType": "boolean",
                    "filter": "0",
                    "type": "equals"
                }
            },
            "s": [{"colId": "SALES_current", "sort": "asc"}],
            "t": "g"
        }

        encoded_payload = urllib.parse.quote(json.dumps(payload))
        modified_url = f"{url}{encoded_payload}"
        webbrowser.open_new_tab(modified_url)

