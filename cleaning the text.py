# Pacotes  
import nltk 
from pymongo import MongoClient
from nltk.corpus import stopwords 
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import text
import sklearn.preprocessing as preproc
import pandas as pd 
import re
from sklearn.model_selection import train_test_split

# Definindo funções 
# Limpeza de texto 
def clean_text(text,remove_stopwords = True):
    # Convertendo a caixa das palavras para minuscula
    text = text.lower()
    #f = open("contractions.txt","r")
    contractions = contractions = {"ain't": "am not","aren't": "are not","can't": "cannot","can't've": "cannot have","'cause": "because","could've": "could have","couldn't": "could not","couldn't've": "could not have","didn't": "did not","doesn't": "does not","don't": "do not","hadn't": "had not","hadn't've": "had not have","hasn't": "has not","haven't": "have not","he'd": "he would","he'd've": "he would have","he'll": "he will","he's": "he is","how'd": "how did","how'll": "how will","how's": "how is","i'd": "i would","i'll": "i will","i'm": "i am","i've": "i have","isn't": "is not","it'd": "it would","it'll": "it will","it's": "it is","let's": "let us","ma'am": "madam","mayn't": "may not","might've": "might have","mightn't": "might not","must've": "must have","mustn't": "must not","needn't": "need not","oughtn't": "ought not","shan't": "shall not","sha'n't": "shall not","she'd": "she would","she'll": "she will","she's": "she is","should've": "should have","shouldn't": "should not","that'd": "that would","that's": "that is","there'd": "there had","there's": "there is","they'd": "they would","they'll": "they will","they're": "they are","they've": "they have","wasn't": "was not","we'd": "we would","we'll": "we will","we're": "we are","we've": "we have","weren't": "were not","what'll": "what will","what're": "what are","what's": "what is","what've": "what have","where'd": "where did","where's": "where is","who'll": "who will","who's": "who is","won't": "will not","wouldn't": "would not","you'd": "you would","you'll": "you will","you're": "you are"}
    # Expandindo as contrações 
    if True: 
        text = text.split()
        new_text = []
        for word in text:
            if word in contractions:
                new_text.append(contractions[word])
            else:
                new_text.append(word)
        text = " ".join(new_text)

    # Formatando palavras e removendo caracteres irrelevantes
    text = re.sub(r'https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
    text = re.sub(r'\<a href', ' ', text)
    text = re.sub(r'&amp;', '', text) 
    text = re.sub(r'[_"\-;%()|+&=*%.,!?:#$@\[\]/]', ' ', text)
    text = re.sub(r'<br />', ' ', text)
    text = re.sub(r'\'', ' ', text)

    # Removendo stopwords 
    if remove_stopwords:
        text = text.split()
        stops = set(stopwords.words("english"))
        text = [w for w in text if not w in stops]
        text = " ".join(text)

    # Tokenize cada palavra 
    text =  nltk.WordPunctTokenizer().tokenize(text)

    return text

# Importando os dados 
# Criando um cliente com o mongodb
cliente = MongoClient('localhost',27017)

# Acessando o dataset
banco = cliente.Political_Ideology

# Acesando a collection  
collections = banco['IBC_truncated']

# Criando o dataframe 
IBC = pd.DataFrame(list(collections.find()))

# Text cleaning and Preprocessing 
clear = []
for i in IBC['text']:
    clear.append(clean_text(i))
IBC['Text Clear'] = clear



# Export clearning data
col = banco['IBC_clear'] 
for i in range(len(IBC['text'])):
    dic = {'texto':IBC['text'].iloc[i],'clear':IBC['Text Clear'].iloc[i],'classificação': IBC['classification'].iloc[i]}
    col.insert_one(dic)