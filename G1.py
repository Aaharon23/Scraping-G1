import requests
from requests.models import Response
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

Response = requests.get('https://g1.globo.com/')

content = Response.content

site = BeautifulSoup(content, 'html.parser')

# HTML DA NOTICIA
noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:

    #TITULO DA NOTICIA
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

    #print(titulo.text)
    #print(titulo['href'])
    #SUB TITULO 
    subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})
    if(subtitulo):
        #print(subtitulo.text)
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text, '', titulo['href']])

news = pd.DataFrame(lista_noticias, columns=['Titulo','Subtitulo','Link'])

news.to_html('G1DAY.html', index=False)
  