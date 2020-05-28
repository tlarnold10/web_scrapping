from googlesearch import search
from bs4 import BeautifulSoup
import requests
import pdb

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
    print(i)

pdb.set_trace()
req = requests.get(my_results_list[0])
soup = BeautifulSoup(req.content, 'html.parser')
print(soup.prettify())

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