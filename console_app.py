from googlesearch import search
from bs4 import BeautifulSoup
import requests
import pdb

def main():
    # Lowes ===============================================
    my_results_list = []    

    query = "lowes WDT750SAHZ"  

    for i in search(query,        # The query you want to run
                    tld = 'com',  # The top level domain
                    lang = 'en',  # The language
                    num = 1,     # Number of results per page
                    start = 0,    # First result to retrieve
                    stop = 1,  # Last result to retrieve
                    pause = 2.0,  # Lapse between HTTP requests
                   ):
        my_results_list.append(i)   

    print(my_results_list[0])   
    

    # Karls ==================================================
    my_results_list = []    

    query = "Karls WDT750SAHZ"  

    for i in search(query,        # The query you want to run
                    tld = 'com',  # The top level domain
                    lang = 'en',  # The language
                    num = 1,     # Number of results per page
                    start = 0,    # First result to retrieve
                    stop = 1,  # Last result to retrieve
                    pause = 2.0,  # Lapse between HTTP requests
                   ):
        my_results_list.append(i)
        print(i)
        
    get_price(my_results_list[0])   

    # Home Depot ================================================
    my_results_list = []    

    query = "Home Depot WDT750SAHZ" 

    for i in search(query,        # The query you want to run
                    tld = 'com',  # The top level domain
                    lang = 'en',  # The language
                    num = 1,     # Number of results per page
                    start = 0,    # First result to retrieve
                    stop = 1,  # Last result to retrieve
                    pause = 2.0,  # Lapse between HTTP requests
                   ):
        my_results_list.append(i)
        print(i)    

    # Menards =====================================================
    my_results_list = []    

    query = "Menards WDT750SAHZ"    

    for i in search(query,        # The query you want to run
                    tld = 'com',  # The top level domain
                    lang = 'en',  # The language
                    num = 1,     # Number of results per page
                    start = 0,    # First result to retrieve
                    stop = 1,  # Last result to retrieve
                    pause = 2.0,  # Lapse between HTTP requests
                   ):
        my_results_list.append(i)
        print(i)    

    get_price(my_results_list[0])

def get_price(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    if(url[len(url)-1] == "/"):
        url = url[0:len(url)-1]
        print(url)
    req = requests.get(url, headers=headers)
    pdb.set_trace()
    soup = BeautifulSoup(req.content, 'html.parser')
    print(soup.prettify())

    return soup

if __name__ == '__main__':
    main()