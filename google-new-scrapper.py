import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://news.google.com/topics/CAAqLQgKIidDQkFTRndvSkwyMHZNR1ptZHpWbUVnWmxjeTAwTVRrYUFrMVlLQUFQAQ?hl=es-419&gl=MX&ceid=MX%3Aes-419"

if __name__=='__main__':
    response = requests.get(URL)
    if response.status_code == 200:
        content = response.text
        soup = BeautifulSoup(content,'html.parser')
        now = datetime.now().strftime('%d_%m_%Y %H_%M')
        with open(f'news/news_{now}.txt', 'w+') as file:
            for element in soup.find_all('h3', class_='ipQwMb ekueJc RD0gLb', limit=20):
                title = element.a.text
                file.write(title + '\n')
        print('archivo generado exitosamente')