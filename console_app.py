from googlesearch import search
from bs4 import BeautifulSoup
import requests
import pdb

def main():
    # Lowes ===============================================
    my_results_list = []    

    query = "lowes WDT750SAHZ"  

#     for i in search(query, 
#                     tld = 'com', 
#                     lang = 'en',  
#                     num = 1, 
#                     start = 0, 
#                     stop = 1,
#                     pause = 2.0,
#                    ):
#         my_results_list.append(i)   
# 
#     print(my_results_list[0])   
    

    # Karls ==================================================
    my_results_list = []    

    query = "Karls WDT750SAHZ"  

    for i in search(query, 
                    tld = 'com', 
                    lang = 'en',  
                    num = 1, 
                    start = 0, 
                    stop = 1,
                    pause = 2.0,
                   ):
        my_results_list.append(i)
        print(i)
        
    get_price(my_results_list[0])   

    # Home Depot ================================================
    my_results_list = []    

    query = "Home Depot WDT750SAHZ"

#     for i in search(query, 
#                     tld = 'com', 
#                     lang = 'en',  
#                     num = 1, 
#                     start = 0, 
#                     stop = 1,
#                     pause = 2.0,
#                    ):
#         my_results_list.append(i)
#         print(i)    

    # Menards =====================================================
    my_results_list = []    

    query = "Menards WDT750SAHZ"    

    for i in search(query, 
                    tld = 'com', 
                    lang = 'en',  
                    num = 1, 
                    start = 0, 
                    stop = 1,
                    pause = 2.0,
                   ):
        my_results_list.append(i)
        print(i)    

    get_price(my_results_list[0])

def get_price(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    if(url[len(url)-1] == "/"):
        url = url[0:len(url)-1]
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    price = soup.find_all(class_ = "h3")
    print(price)

    return soup

if __name__ == '__main__':
    main()