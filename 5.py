import requests
import numpy as np
import json
from bs4 import BeautifulSoup

def load_countries_name(n):
    url = 'https://randomuser.me/api/'
    params = {
        'results': n
    } 
    response = requests.get(url, params)
    datas = response.json()['results']
    countries = []
    for data in datas: 
        country = data['location']['country']
        countries.append(country)
    #countries = [data['location']['country'] for data in datas] заменяет предыдущие 4 строчки
    return countries  

def generate_product_id(n):
    ids = np.random.randint(0, 25, size=n)
    return ids

def generate_region_sales(n):
    sales = np.random.randint(0, 999, size=n)
    return sales

def generate_regions(n, city_names=[]):
    regions = np.random.choice(city_names, size=n, replace=True)
    return regions

def extract_currency_codes():
    url = "https://www.exchangerate-api.com/docs/supported-currencies"
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    tables = soup.find_all("table")
    currency_codes = {}
    for table in tables:
        for row in table.find_all("tr")[1:]:
            cells = row.find_all("td")
            country = cells[2].text.strip()
            currency_code = cells[0].text.strip()
            currency_codes[country] = currency_code
    return currency_codes

def get_exchange_rate(currency_code):
    url = f"https://open.er-api.com/v6/latest/{currency_code}"
    response = requests.get(url)
    data = response.json()
    rates = data.get("rates")
    rub_value = rates["RUB"]
    return rub_value


def add_currency_and_sales_in_rub(data, currency_codes):
    data_with_currency = np.empty((data.shape[0], data.shape[1] + 2), dtype=object)
    data_with_currency[:, :-2] = data

    for i in range(data.shape[0]):
        country = data[i, 2]
        currency_code = currency_codes.get(country, "EUR")
        exchange_rate = get_exchange_rate(currency_code)
        sales = float(data[i, 1])
        converted_sales = sales * exchange_rate

        data_with_currency[i, -2] = currency_code
        data_with_currency[i, -1] = converted_sales

    return data_with_currency


n = 50
city_names = load_countries_name(n)[:6]
data = np.column_stack((generate_product_id(n), generate_region_sales(n), generate_regions(n, city_names)))

np.savetxt('data.txt', data, delimiter=',', fmt='%s')

data = np.loadtxt('data.txt', delimiter=',', dtype=str) 
currency_codes = extract_currency_codes()
data_with_currency = add_currency_and_sales_in_rub(data, currency_codes)

np.savetxt('data_with_currency.txt', data_with_currency, delimiter=',', fmt='%s')
