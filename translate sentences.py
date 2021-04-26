# Pacotes 
from pymongo import MongoClient
import pandas as pd
from deep_translator import GoogleTranslator


# Importando os dados 
# Criando um cliente com o mongodb
cliente = MongoClient('localhost',27017)

# Acessando o dataset
banco = cliente.Political_Ideology

# Acesando a collection  
collections = banco['IBC_truncated']

# Criando o dataframe 
IBC = pd.DataFrame(list(collections.find()))

# Traduzindo as sentenças do Dataframe 

# Texto
Texto=[]
for i in IBC['text']:
    translated = GoogleTranslator(source='auto', target='pt').translate(i)
    Texto.append(translated)
IBC['text']=Texto

# Classificação 
classification=[]
for i in IBC['classification']:
    translated = GoogleTranslator(source='auto', target='pt').translate(i)
    classification.append(translated)
IBC['classification']=classification

# Exprortando os dados para o banco 
col = banco['IBC_truncated_translate']
for i in range(len(IBC)):
    dic={'texto':IBC['text'].iloc[i],'classificação': IBC['classification'].iloc[i]}
    result =col.insert_one(dic)