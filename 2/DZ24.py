from bs4 import BeautifulSoup
import requests

def cbr_data():
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    res = requests.get(
        f'https://www.cbr.ru/key-indicators',
        headers=headers
    )
    
    soup = BeautifulSoup(res.text, 'html.parser')
    
            
    table = soup.findAll('table')

    d = []
    for tr in table:
        td = tr.find_all('td', {'class' : 'value td-w-4 _bold _end mono-num'})
        row = [i.text for i in td]
        d += row
    # print(d)
    
    d2 = []
    for tr in table:
        td = tr.find_all('td', {'class' : 'value td-w-4 _bold _end mono-num _with-icon _up _red'})
        row = [i.text for i in td]
        d2 += row
    # print(d2)
    
    d3 = []
    for tr in table:
        td = tr.find_all('td', {'class' : 'value td-w-4 _end'})
        row = [i.text for i in td]
        d3 += row
    # print(d3)
        
    d4 = []
    for tr in table:
        td = tr.find_all('td', {'class' : 'value td-w-4 _end'})
        row = [i.text for i in td]
        d4 += row
    # print(d4)
    
    print(d3[0])
    
    print('Китайский юань:', d[0])
    print('Доллар США:', d[1])
    print('Евро:', d[2])
    
    print(d4[1])
    
    print('Китайский юань:', d2[0])
    print('Доллар США:', d2[1])
    print('Евро:', d2[2])



cbr_data()
    