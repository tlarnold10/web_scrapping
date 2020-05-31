from googlesearch import search
from bs4 import BeautifulSoup
import requests
import pdb
from urllib.parse import quote


def main():

    # setup the html file ====================================
    file = open("estimate.html", "w")
    html_text = ''
    html_text = """
        <html>
            <body>
                <table style="border: 1px solid black;">
                    <thead>
                        <tr>
                            <th style="border: 1px solid black;">Company Name</th>
                            <th style="border: 1px solid black;">Product ID</th>
                            <th style="border: 1px solid black;">Price</th>
                            <th style="border: 1px solid black;">Product URL</th>
                        </tr>
                    </thead>
                <tbody>""" 

    # Karls ==================================================
    soup, url = get_html('Karls', 'WDT750SAHZ')
    if soup != '':  
        price = soup.find(id = "model_price")
    else:
        price = None
    html_text += write_row('Karls', 'WDT750SAHZ', price, url)

    # Menards =====================================================
    soup, url = get_html('Menards', 'WDT750SAHZ') 
    if soup != '':  
        price = soup.find(id = "itemDetailPage")
    else:
        price = None
    html_text += write_row('Menards', 'WDT750SAHZ', price, url)

    # Sears =====================================================
    soup, url = get_html('Sears', 'WDT750SAHZ') 
    if soup != '':  
        price = soup.find(id = "itemDetailPage")
    else:
        price = None
    html_text += write_row('Sears', 'WDT750SAHZ', price, url)

    # Home Depot =====================================================
    soup, url = get_html('Home Depot', 'WDT750SAHZ')  
    if soup != '': 
        price = soup.find(id = "itemDetailPage")
    else:
        price = None
    html_text += write_row('Home Depot', 'WDT750SAHZ', price, url)

    # Lowes =====================================================
    soup, url = get_html('Lowes', 'WDT750SAHZ')
    if soup != '':   
        price = soup.find(id = "itemDetailPage")
    else:
        price = None
    html_text += write_row('Lowes', 'WDT750SAHZ', price, url)

    # Heartland Hardware =====================================================
    soup, url = get_html('Heartland Hardware', 'WDT750SAHZ')
    if soup != '': 
        price = soup.find(id = "itemDetailPage")
    else:
        price = None
    html_text += write_row('Heartland Hardware', 'WDT750SAHZ', price, url)

    html_text += """
                    </tbody>
                </table>
            </body>
        </html>
    """

    file.write(html_text) 
    file.close() 

def get_html(competitor, model_num):
    my_results_list = []
    query = competitor + model_num
    for i in search(query, tld = 'com', lang = 'en', num = 5, start = 0, stop = 5, pause = 2.0,):
        my_results_list.append(i)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    print(competitor)
    print(my_results_list)
    url = my_results_list[0]
    if(url[len(url)-1] == "/"):
        url = url[0:len(url)-1]
    if competitor in ('Lowes', 'Sears', 'Home Depot', 'Menards'):
        soup = ''
    else:
        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.content, 'html.parser')
    # response = urllib.request.urlopen(url)
    # html = response.read()
    # pdb.set_trace()
    return(soup, url)

def write_row(company_name, product_num, price, product_url):
    # print(product_url)
    # product_url = quote(product_url)
    html_text = """
        <tr>
            <td style="border: 1px solid black;">""" + company_name + """</td>
            <td style="border: 1px solid black;">""" + product_num + """</td>
            <td style="border: 1px solid black;">""" + str(price) + """</td>
            <td style="border: 1px solid black;">""" + str(product_url) + """</td>
        </tr>"""
    return html_text

if __name__ == '__main__':
    main()