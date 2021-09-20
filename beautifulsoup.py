from bs4 import BeautifulSoup

if __name__ == '__main__':
    
    with open('econpy.html', 'r') as file:
        
        content = file.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        title = soup.find('title')

        print(title.name)
        print(title.text)
        print(title.get_text())
        
        for element in soup.find_all('div', {'title': 'buyer-info'}):
            div = element.find('div')
            span = element.find('span')
            
            print(div.text,'\n', span.text)
            
#             Atributos de elementos
# Listado de atributos para nuestros objetos de tipo element.Tag.

# Atributo	Descripción
# parent	Elemento padre
# parents	Listado de elementos padres hasta el nível top
# next_sibling	Siguiente elemento después del elemento actual
# next_siblings	Listado de elementos después del elemento actual
# previous_sibling	Elemento anteriot al elemento actual
# previous_siblings	Listado de elemento anteriores al elemento actual
# contents	Listado de todos los elementos hijos
# children	Generador de todos los elementos hijos
# descendants	Generador de todos los elementos hijos de forma recursiva