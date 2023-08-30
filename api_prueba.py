import spacy
import numpy as np
from flask import Flask, request,jsonify

def spacy_func(jsonfile):
    nlp = spacy.load('es_core_news_sm')
    oracion=jsonfile['oraciones']
    T1=np.shape(oracion)[0]
    dic={}
    for j in range(T1):
        doc = nlp(oracion[j])
        ents = list(doc.ents)
        T=np.shape(ents)[0]
        dic[j]={}
        for i in range(T):
            k=ents[i]
            v=ents[i].label_
            dic[j].update({k:v})
    return dic

app= Flask(__name__)
@app.route('/',methods=['POST'])
def handle_json():
    json_data = request.get_json()
    entidades=spacy_func(json_data)
    return jsonify(entidades)


if __name__=='__main__':
    app.run(debug=True)