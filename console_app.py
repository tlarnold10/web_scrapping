from googlesearch import search
from bs4 import BeautifulSoup
import lxml
import requests
import pdb
import urllib.request

def main():

    # Karls ==================================================
    soup = get_html('Karls', 'WDT750SAHZ')   
    price = soup.find(id = "model_price")
    try:
        print(price.text)
    except:
        print("No price found")

    # Menards =====================================================
    soup = get_html('Menards', 'WDT750SAHZ')  
    price = soup.find(id = "itemDetailPage")
    try:
        print(price.text)
    except:
        print("No price found")

def get_html(competitor, model_num):
    my_results_list = []
    query = competitor + model_num
    for i in search(query, tld = 'com', lang = 'en', num = 1, start = 0, stop = 1, pause = 2.0,):
        my_results_list.append(i)
        print(i)  
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    url = my_results_list[0]
    if(url[len(url)-1] == "/"):
        url = url[0:len(url)-1]
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    response = urllib.request.urlopen(url)
    html = response.read()
    pdb.set_trace()
    return(soup)

if __name__ == '__main__':
    main()