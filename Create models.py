# Pacotes 
from pymongo import MongoClient
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importando os dados 
# Criando um cliente com o mongodb
cliente = MongoClient('localhost',27017)

# Acessando o dataset
banco = cliente.Political_Ideology

# Acesando a collection  
collections = banco['IBC_clear']

# Criando o dataframe 
IBC = pd.DataFrame(list(collections.find()))

# Transformando os rotulos de previsão em valores binarios 
binary = pd.get_dummies(IBC['classificação'])
for j in binary.columns:
    IBC[j] = binary[j]

# Ajustando os conjuntos de treinos e teste 
# Listando as categorias
categorias = ['Liberal','Conservative']

# Criando um conjunto de treino e teste
train, test = train_test_split(IBC,random_state=42,test_size=0.33)
X_train = train.texto
X_test = test.texto
print(X_train.shape)
print(X_test.shape)

# Classificando os modelos 
# Bag of words 
# MultinomialNB
NB_pipeline = Pipeline([('bow', CountVectorizer(tokenizer=lambda doc: doc, ngram_range=[3,3], lowercase=False)),('clf', OneVsRestClassifier(MultinomialNB(fit_prior=True, class_prior=None)))])
for category in categorias:
    NB_pipeline.fit(X_train,train[category])
    prediction = NB_pipeline.predict(X_test)
    print('Test accuracy is Multinomial {}'.format(accuracy_score(test[category], prediction)))

# Logistic Regression 
Logit = Pipeline([('bow',CountVectorizer(tokenizer=lambda doc: doc, ngram_range=[3,3], lowercase=False)),('clf',OneVsRestClassifier(LogisticRegression(C=1.0,class_weight=None,dual=False,fit_intercept=True,intercept_scaling=1,max_iter=100,multi_class='ovr',n_jobs=1,penalty='l2',random_state=None,solver='liblinear',tol=0.0001,verbose=0)))])
for category in categorias:
    NB_pipeline.fit(X_train,train[category])
    prediction = NB_pipeline.predict(X_test)
    print('Test accuracy is Logit {}'.format(accuracy_score(test[category], prediction)))


# Tfidf
# MultinomialNB
NB_pipeline = Pipeline([('tfidf', TfidfVectorizer(stop_words=stop_words)),('clf', OneVsRestClassifier(MultinomialNB(fit_prior=True, class_prior=None)))])
for category in categorias:
    NB_pipeline.fit(X_train,train[category])
    prediction = NB_pipeline.predict(X_test)
    print('Test accuracy is Multinomial{}'.format(accuracy_score(test[category], prediction)))

# Logistic Regression 
Logit = Pipeline([('tfidf',TfidfVectorizer(stop_words=stop_words)),('clf',OneVsRestClassifier(LogisticRegression(C=1.0,class_weight=None,dual=False,fit_intercept=True,intercept_scaling=1,max_iter=100,multi_class='ovr',n_jobs=1,penalty='l2',random_state=None,solver='liblinear',tol=0.0001,verbose=0)))])
for category in categorias:
    NB_pipeline.fit(X_train,train[category])
    prediction = NB_pipeline.predict(X_test)
    print('Test accuracy is Logit{}'.format(accuracy_score(test[category], prediction)))

# Importando os twitters dos candidatos
collections2 = banco['Twitters']
Twitter = pd.DataFrame(list(collections2.find()))

# Recriando os modelos 
# MultinomialNB
Multi_pred=[]
Multinomial = Pipeline([('tfidf', TfidfVectorizer(stop_words=stop_words)),('clf', OneVsRestClassifier(MultinomialNB(fit_prior=True, class_prior=None)))])
for category in categorias:
    Multinomial.fit(IBC['texto'],IBC[category])
    prediction = Multinomial.predict(Twitter['twitter'])
    Multi_pred.append(prediction)


# Logistic Regression
log_pred=[]
Logit = Pipeline([('tfidf',TfidfVectorizer(stop_words=stop_words)),('clf',OneVsRestClassifier(LogisticRegression(C=1.0,class_weight=None,dual=False,fit_intercept=True,intercept_scaling=1,max_iter=100,multi_class='ovr',n_jobs=1,penalty='l2',random_state=None,solver='liblinear',tol=0.0001,verbose=0)))])
for category in categorias:
    Logit.fit(IBC['texto'],IBC[category])
    prediction = Logit.predict(Twitter['twitter'])
    log_pred.append(prediction)

# Adicionando as colunas de classificação 
Twitter['Conservador'] = list(Multi_pred[1])
Twitter['Liberal'] = list(Multi_pred[0])
Twitter['Neutra'] = list(1-(Multi_pred[0]+Multi_pred[1]))

# Agrupando os dados 
group=Twitter.groupby('perfil').agg({'Conservador':"sum",'Liberal':"sum",'Neutra':"sum"})

# Criando plot
fig,ax = plt.subplots()
ax.bar(group.index,group['Conservador'],color='green')
ax.bar(group.index,group['Liberal'],bottom=group['Conservador'],color='red')
ax.bar(group.index,group['Neutra'],bottom=np.array(group['Conservador'])+np.array(group['Liberal']),color='silver')
plt.ylim(0,5)
plt.legend(['Conservador','Liberal','Neutro'])
plt.ylabel("Numero de Noticias")
plt.title("Sentimentos dos Textos das Noticias ")
plt.show()
