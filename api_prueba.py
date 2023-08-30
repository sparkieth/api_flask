from spacy import load
import numpy as np
from flask import Flask, request,jsonify

def spacy_func(jsonfile):
    # 1. se llama la libería de Spacy que se utilizará
    nlp = load('es_core_news_sm')
    # 2. se extraen las oraciones
    oracion=jsonfile['oraciones']
    T1=np.shape(oracion)[0]
    # se prepara la función que albrgará los resultados
    dic={}
    for j in range(T1):
        #se procesa cada oración
        doc = nlp(oracion[j])
        ents = list(doc.ents)
        T=np.shape(ents)[0]
        #por cada oración se crea un diccionario con cada resultado
        dic[j]={}
        for i in range(T):
            k=ents[i]
            v=ents[i].label_
            dic[j].update({k:v})
            
    return 
"""
DISCLAIMER
Desafortunadamente, encontré el siguiente error cuando quise compilar la app de Flask

"zsh: illegal hardware instruction  python api_prueba.py"

Por ello, no pude probar la página. La siguiente es una estructura de la que partiría para hacer la app de Flask.
"""

app= Flask(__name__)
@app.route('/',methods=['POST'])
def handle_json():
    json_data = request.get_json()
    entidades=spacy_func(json_data)
    return jsonify(entidades)


if __name__=='__main__':
    app.run(debug=True)