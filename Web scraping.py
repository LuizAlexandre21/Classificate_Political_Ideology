 # Pacotes 
from selenium import webdriver 
import time 
from pymongo import MongoClient
from deep_translator import GoogleTranslator

# Criando um cliente com o mongodb
cliente = MongoClient('localhost',27017)

# Acessando o dataset 
banco = cliente.Political_Ideology

# Acessando a collection
col = banco['Twitters']

# Definindo os perfis 
perfis = ['MichelTemer','dilmabr','jairbolsonaro','LulaOficial','FHC']

# Setando o drive do chrome 
drive = webdriver.Chrome(executable_path='/home/alexandre/Documentos/Ciência de Dados/Monografia/Classificate_Political_Ideology/Scraper/chromedriver')

# Criando vetor de mensagens
msg =[]

# Extraindo o perfil
for perfil in perfis:
    
    # Definindo a url
    url = "https://twitter.com/"+perfil
    
    # Acessando a url
    drive.get(url)
    
    # Adicionando um sleep 
    time.sleep(10)
    
    # Extraindo tweets 
    html= drive.find_element_by_xpath("//div[@class='css-1dbjc4n r-1jgb5lz r-1ye8kvj r-13qz1uu']")
    html1=html.find_element_by_xpath("//section[@class='css-1dbjc4n']")
    html2=html1.find_elements_by_xpath("//div[@class='css-1dbjc4n r-j7yic r-qklmqi r-1adg3ll r-1ny4l3l']")

    # Salvando as mensagens de texto
    for i in range(3):
        twitter = GoogleTranslator(source='auto', target='en').translate(html2[i].text)
        perfil = perfil 
        dic = {'twitter':twitter,'perfil':perfil}
        col.insert_one(dic)

