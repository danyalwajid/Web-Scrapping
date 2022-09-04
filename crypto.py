# Importing Libraries 

from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL of website 
url = "https://www.coingecko.com/en"

# Get Request 
response = requests.get(url)

# Status Code 
print("Status Code :", response.status_code)

# Soup Object 
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())

# results 
# results = soup.find_all('table', {'class': "sort table mb-0 text-sm text-lg-normal table-scrollable"})
results = soup.find('table', {'class': "table-scrollable"}).find('tbody').find_all('tr')
print(len(results))

#  Name 
# name = results[0].find('a', {'class': 'tw-flex tw-items-start md:tw-flex-row tw-flex-col'}, 'span':{"class" :  'lg:tw-flex font-bold tw-items-center tw-justify-between'} ).text
name = results[0].find('span',{"class" :  'lg:tw-flex font-bold tw-items-center tw-justify-between'} ).get_text().strip()
print("Name :",name)

# Price 
price = results[0].find('span', {'class' : "no-wrap"}).get_text().strip()
print("Price :",price)

# 1 hour 
h1 = results[0].find('td', {'class':"td-change1h change1h stat-percent text-right col-market"}).text.strip()
print("1 Hour :", h1)

# 24 Hours 
h24 = results[0].find('td', {'class':"td-change24h change24h stat-percent text-right col-market"}).text.strip()
print("24 hours ",h24)

# 7 days 
days7 = results[0].find('td', {'class':"td-change7d change7d stat-percent text-right col-market"}).text.strip()
print("7 Days :",days7)

# 24 hours Volume  
h24vol = results[0].find('td', {'class':"td-liquidity_score lit text-right col-market"}).text.strip()
print("24 Hours Volume :",h24vol)

# mkt Cap
mkt = results[0].find('td', {'class':"td-market_cap cap col-market cap-price text-right"}).text.strip()
print("MKT cap :",mkt)


# put Everything togather in side the loop 
# Create empty list 
name = []
price = []
change_1h = []
change_24h = []
change_7days = []
volum_24h = []
market_cap = []

for result in results:
    # name
    try :
        name.append(result.find('span',{"class" :  'lg:tw-flex font-bold tw-items-center tw-justify-between'} ).get_text().strip())
    except:
        name.append("n/a")

    # price 
    try :
        price.append(result.find('span', {'class' : "no-wrap"}).get_text().strip())
    except:
        price.append("n/a")

    # Change 1 hours 
    try :
        change_1h.append(result.find('td', {'class':"td-change1h change1h stat-percent text-right col-market"}).text.strip())
    except:
        change_1h.append("n/a")

    # Change 24 hours 
    try :
        change_24h.append(result.find('td', {'class':"td-change24h change24h stat-percent text-right col-market"}).text.strip())
    except:
        change_24h.append("n/a")   

    # 7 days 
    try :
        change_7days.append(result.find('td', {'class':"td-change7d change7d stat-percent text-right col-market"}).text.strip())
    except:
        change_7days.append("n/a")

    # 24 hours Volum 
    try :
        volum_24h.append(result.ind('td', {'class':"td-liquidity_score lit text-right col-market"}).text.strip())
    except:
        volum_24h.append("n/a")

    # market capture 
    try :
        market_cap.append(result.find('td', {'class':"td-market_cap cap col-market cap-price text-right"}).text.strip())
    except:
        market_cap.append("n/a")


# creating DataFrame with pandas 
crypto_data = pd.DataFrame({'Coin': name , "Price": price, 'Change_1h': change_1h, "Change_24h": change_24h, 
                            'Chnage_7days': change_7days, 'Volume_24h': volum_24h, "Market_cap" : market_cap})

# Display Crypto data
print(crypto_data.head())

# Saving data in the form of xlsx(Excle)
crypto_data.to_excel("Single_page_data_crypto.xlsx", index=False)

# Saving Data in the Form of CSV
crypto_data.to_csv("Single_page_crypto_data.csv", index=False)
