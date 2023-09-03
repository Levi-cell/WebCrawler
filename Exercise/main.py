from requests import get
from bs4 import BeautifulSoup

# Fazendo raspagem do código
resposta = get("https://pt.wikipedia.org/wiki/Bicicleta")
link = "https://pt.wikipedia.org/wiki/Bicicleta"

# mapear conteúdo html

tags = BeautifulSoup(resposta.text, "html5lib")

# localizando o titulo

title = tags.find("title")

# printando o nome da página/titulo
print(f"Link principal: {link}")
print(f"Nome da página principal: {title.text}") # Mds isso funciona mesmo que delicia
print("-"*35)
# Encontrando todos os links para outras páginas da Wikipédia
links_wikipedia = tags.find_all("a", href=lambda href: href and href.startswith("/wiki/"))

# Imprimindo os links encontrados
print("Páginas Secundárias:")
print("-"*35)
for link in links_wikipedia:
    link = "https://pt.wikipedia.org" + link['href']

    respostaSecundaria = get(link)
    tagsSecundarias = BeautifulSoup(respostaSecundaria.text, "html5lib")
    titleSecundario = tagsSecundarias.find("title")
    print(f"Link: {link}")
    print(f"Tópico: {titleSecundario.text}")
    print("-")