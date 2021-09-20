import requests
import re #este modulo es el de regular expressions y se encuentra ya en la biblioteca standard

URL = 'http://econpy.pythonanywhere.com/ex/001.html'

if __name__ == '__main__':
    
    # esto es con solicitud sin embargo usaremos el file html local
    # response = requests.get(URL)
    
    # if response.status_code == 200:
    #     content = response.text
        
    with open('econpy.html','r') as file:
        content = file.read()
        
        regex = '<div title="buyer-name">(.+?)</div>'        
        for title in re.findall(regex, content):
            print(title)
        
        
        # esto es con un algoritmo normal sin embargo usaremos regex
        # regexa = '<div title="buyer-name">'
        # regexb = '</div>'
        # for line in content.split('\n'):
        #     if regexa in line:
        #         start = line.find(regexa) + len(regexa)
        #         end = line.find(regexb)
        #         title = line[start:end]
        #         print(title)