import pandas as pd
import joblib
import os
from .vocabulario import vocabulary
from sklearn.feature_extraction.text import CountVectorizer

class MedidorToxicidad:
    
    def __init__(self) -> None:
        self.__model = None
        self.__load_model()

    def __load_model(self):
        self.__model = joblib.load(os.path.dirname(__file__) + '\\training\\toxicidad_model.pkl') 

    def funcion_prediccion(self, texto):
        texto_cv = CountVectorizer(vocabulary=vocabulary).transform([texto]).conjugate()
        toxicidad = self.__model.predict(texto_cv)[0]
            
        if (0 <= toxicidad <= 0.3):
            return "Mensaje con toxicidad baja"
        elif (0.31 <=  toxicidad <= 0.6):
            return "Mensaje con toxicidad moderada"
        elif (0.61 <= toxicidad <= 1):
            return "Mensaje con toxicidad alta"
