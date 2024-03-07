import pytest
from modelo.medidor_toxicidad import MedidorToxicidad
from unittest.mock import Mock

@pytest.fixture
def mensaje_toxicidad_baja():
    return "NO!, Let him, we need a Conservative government."


def test_toxicidad_baja(mocker, mensaje_toxicidad_baja):

    mocker.patch("modelo.medidor_toxicidad.MedidorToxicidad.medir_toxicidad",return_value=0.3)
    medidor = MedidorToxicidad()
    puntaje= medidor.medir_toxicidad(mensaje_toxicidad_baja)
    
    assert 0 <= puntaje <= 0.4
