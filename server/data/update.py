import json
import requests

output = []


def getGas(regione, provincia):
    global output
    url = "https://carburanti.mise.gov.it/ospzApi/search/area"
    raw_data = '{"region":'+regione+',"province":"'+provincia+'","town":null}'
    headers = {
        "Connection": "keep-alive",
        "sec-ch-ua": '"Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        "Accept": "application/json",
        'Content-Type': 'application/json',
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
        "sec-ch-ua-platform": '"Windows"',
        "Origin": "https://carburanti.mise.gov.it",
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://carburanti.mise.gov.it/ospzSearch/area',
        'Accept-Language': 'en-US,en;q=0.9,it;q=0.8',
        'Cookie': 'cookies_consent=true'
    }

    r = requests.post(url, data=raw_data, headers=headers)

    if r.status_code == 200:
        response = r.json()
        results = response['results']
        output.append(results)


zone = [{'11': ['AG', 'CL', 'CT', 'EN', 'ME', 'PA', 'RG', 'SR', 'TP']}]

for zona in zone:
    regione_key = list(zona.keys())[0]
    for regione in zona.values():
        for provincia in regione:
            print(provincia)
            getGas(regione_key, provincia)
        with open('./regione/'+regione_key+'/'+'latest.json', 'w') as file:
            flat_list = [item for sublist in output for item in sublist]
            json.dump(flat_list, file)
