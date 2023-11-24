import nullpunkt

import pytest
import random
import math

# (Inkluder nullpunkt-funksjonen her)

def generer_tilfeldige_koeffisienter():
    """ Hjelpefunksjon for å generere tilfeldige koeffisienter. """
    a = random.uniform(-10, 10)
    b = random.uniform(-10, 10)
    c = random.uniform(-10, 10)
    return a, b, c

@pytest.mark.parametrize("a,b,c", [generer_tilfeldige_koeffisienter() for _ in range(100)])
def test_tilfeldige_nullpunkt(a, b, c):
    """ Tester nullpunkt-funksjonen med tilfeldig genererte koeffisienter. """
    discriminant = b**2 - 4*a*c
    expected = "Funksjonen har ingen nullpunkter!"
    if discriminant > 0:
        expected = ((-b + math.sqrt(discriminant)) / (2 * a), 
                    (-b - math.sqrt(discriminant)) / (2 * a))
    elif discriminant == 0:
        expected = (-b / (2 * a),)

    assert nullpunkt.nullpunkt(a, b, c) == expected
