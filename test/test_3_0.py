import pytest
from src.Ej_3_0 import cuenta, control_errores


@pytest.mark.parametrize(
    "inPalabra, inLetra, outNumero",
    [
        ("Amarillo", "a", 2),
        ("Rosadito", "O", 2)
    ]
)
def test_cuenta(inPalabra, inLetra, outNumero):
    assert cuenta(inPalabra, inLetra) == outNumero


@pytest.mark.parametrize(
    "inPalabra, inLetra, outNum_error",
    [
        ("Toro br4v0", "1e", 5),
        ("mart!l1e4ndo", "7", 1),
        ("Instituto", "", 2),
        ("Azulado", "La", 4),
        ("alemanes", "4", 3),
        ("Amarillo", "L", 0),
    ]
)
def test_control_errores(inPalabra, inLetra, outNum_error):
    assert control_errores(inPalabra, inLetra) == outNum_error