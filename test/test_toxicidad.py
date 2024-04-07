import pytest
from modelo.medidor_toxicidad import MedidorToxicidad
from unittest.mock import Mock

@pytest.fixture
def mensaje_toxicidad_baja():
    return "As always, yours is dripping with sarcasm, which as I quoted from Psychology Today to you yesterday is a form of bullying."

@pytest.fixture
def mensaje_toxicidad_moderada():
    return "Okay.....Should we not be investigating Eric Holder for ""Fast and Furious"", Obama/Hillary for Benghazi, The secret meeting of Susan Rice and Bill Clinton, Hillary/Obama selling 20 percent of US uranium to RUSSIA, Releasing five terrorist at gitmo for one traitor.......?"

@pytest.fixture
def mensaje_toxicidad_alta():
    return "trump is a shyster.  He refuses to pay his hotel bills and cheat contractors who've worked for him.  He's bad news and his followers are too stupid to realize it."

def test_toxicidad_baja(mocker, mensaje_toxicidad_baja):

    medidor = MedidorToxicidad()
    type_message = medidor.funcion_prediccion(mensaje_toxicidad_baja)
    
    assert type_message == "Mensaje con toxicidad baja"

def test_toxicidad_moderada(mocker, mensaje_toxicidad_moderada):

    medidor = MedidorToxicidad()
    type_message = medidor.funcion_prediccion(mensaje_toxicidad_moderada)

    assert type_message == "Mensaje con toxicidad moderada"

def test_toxicidad_alta(mocker, mensaje_toxicidad_alta):

    medidor = MedidorToxicidad()
    type_message = medidor.funcion_prediccion(mensaje_toxicidad_alta)

    assert type_message == "Mensaje con toxicidad alta"