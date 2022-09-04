from bs4 import BeautifulSoup
import requests
import pandas as pd

name = []
price = []
change_1h = []
change_24h = []
change_7days = []
volum_24h = []
market_cap = []

for i in range(1,11):

    # website URL 
    url = 'https://www.coingecko.com/?page=' + str(i)

    # Get Request 
    response = requests.get(url)

    # creating object of beautyful soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Results 
    results = soup.find('table', {'class': "table-scrollable"}).find('tbody').find_all('tr')



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
    crypto_data.to_excel("Pagination_page_data_crypto.xlsx", index=False)

    # Saving Data in the Form of CSV
    crypto_data.to_csv("Pagination_page_crypto_data.csv", index=False)
