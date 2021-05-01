# Pacotes 
import pandas as pd 
import matplotlib .pyplot as plt
from pymongo import MongoClient
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression

# Importando os dados 
# Criando um cliente com o mongodb
cliente = MongoClient('localhost',27017)

# Acessando o dataset
banco = cliente.Political_Ideology

# Acesando a collection  
collections = banco['IBC_truncated_translate']

# Criando o dataframe 
IBC = pd.DataFrame(list(collections.find()))

# Criando amostras de treino e teste 
x_train, x_test, y_train, y_test = train_test_split(IBC['texto'], IBC['classificação'], test_size=0.8, random_state=4)

# Criando os modelos 
# logit 
log_reg=LogisticRegression()
log_reg.fit(X_train,y_train)