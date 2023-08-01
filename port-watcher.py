import requests
from bs4 import BeautifulSoup

def print_meta_properties_of_head_in_html_page_of_get_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(response.url)
        print(response.headers)
        print("-----END OF HEADER------")
        soup = BeautifulSoup(response.text, 'html.parser')
        metas = soup.find_all('meta')
        for meta in metas:
            print(f'{meta}')
        print("-----HTLML HEAD PROPERTIES------")
    else:
        print(f'Error: {response.status_code}')

if __name__ == '__main__':
    url = 'http://127.0.0.1:7860'
    print_meta_properties_of_head_in_html_page_of_get_url(url)