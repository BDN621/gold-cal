import requests

apikey = "8cep8n23gv6v27ji5845docolhd3wavjv8hb73ucsfie6opctulu4tmvjf2i"
currency = "USD"
link = f"https://metals-api.com/api/latest?access_key={apikey}&base={currency}&symbols=XAU"
grams = 28.3495
response = requests.get(link)
r = response.json()

rate = r["rates"]['XAU']/grams

priceUSD = round(rate,2)

print(f"PRICE OF GOLD = {priceUSD} per gram")
file = open("link.txt", "w")
file.write(link)
file.close()