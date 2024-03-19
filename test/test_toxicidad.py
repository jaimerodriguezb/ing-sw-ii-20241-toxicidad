import pytest
from modelo.medidor_toxicidad import MedidorToxicidad
from unittest.mock import Mock

@pytest.fixture
def mensaje_toxicidad_baja():
    return "NO!, Let him, we need a Conservative government."

@pytest.fixture
def mensaje_toxicidad_moderada():
    return "And, being white, they're dancing badly."

@pytest.fixture
def mensaje_toxicidad_alta():
    return "You don't care whether Alaska educates its children. We get it. You are an ass."

def test_toxicidad_baja(mocker, mensaje_toxicidad_baja):

    medidor = MedidorToxicidad()
    type_message = medidor.medir_toxicidad(mensaje_toxicidad_baja)
    
    assert type_message == "Mensaje con toxicidad baja"

def test_toxicidad_moderada(mocker, mensaje_toxicidad_moderada):

    medidor = MedidorToxicidad()
    type_message = medidor.medir_toxicidad(mensaje_toxicidad_moderada)

    assert type_message == "Mensaje con toxicidad moderada"

def test_toxicidad_alta(mocker, mensaje_toxicidad_alta):

    medidor = MedidorToxicidad()
    type_message = medidor.medir_toxicidad(mensaje_toxicidad_alta)

    assert type_message == "Mensaje con toxicidad alta"

"""
def test_toxicidad_baja(mocker, mensaje_toxicidad_baja):

    medidor = MedidorToxicidad()
    puntaje = medidor.medir_toxicidad(mensaje_toxicidad_baja)
    
    assert 0.0 <= puntaje <= 0.4

def test_toxicidad_moderada(mocker, mensaje_toxicidad_moderada):

    medidor = MedidorToxicidad()
    puntaje = medidor.medir_toxicidad(mensaje_toxicidad_moderada)

    assert 0.41 <= puntaje <= 0.6

def test_toxicidad_alta(mocker, mensaje_toxicidad_alta):

    medidor = MedidorToxicidad()
    puntaje = medidor.medir_toxicidad(mensaje_toxicidad_alta)

    assert 0.61 <= puntaje <= 1
"""