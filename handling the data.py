# Packages 
import pandas as pd 
from pymongo import MongoClient

# Import IBC dataset 
object =pd.read_pickle('/home/alexandre/Documentos/Ciência de Dados/Monografia/Classifying_Political_Ideology/learning database/sampleData.pkl')

# Export to mongo 
# Create mongo connection 
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.Political_Ideology
col = db.IBC_truncated

# Extract label and text
for i in object:
    for j in i:
        dic={'text':j.get_words(),'classification':j.label}
        result = col.insert_one(dic)



