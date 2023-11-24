# Nullpunkter til andregradsfunksjoner
## Oppgave:
Du skal nå lage en funksjon kalt ```nullpunkt``` som skal ha tre parametre: a, b og c.
Funksjonen skal fungere slik at man putter inn argumenter for a, b og c som skal svare til verdien i et andregradsuttrykk med formelen ax^2+bx+c.
Funksjonen skal deretter returnere nullpunktene til funksjonen.
Funksjonen skal altså se slik ut, så du skal ikke endre navnet eller parameterne til funksjonen:
```Python
nullpunkt(a, b, c)
```

Ta utgangspunkt i programmer som er laget i python-filen "nullpunkt.py" og utvid programmet slik at det klarer denne oppgaven.

### Kriterier for å få til oppgaven:
1. Om funksjonen ikke har noen nullpunkt skal den returnere "Funksjonen har ingen nullpunkter!".
2. Om funksjonen kun har ett nullpunkt skal den returnere det ene nullpunktet som en avrundet float med 2 desimaler
3. Om funksjonen har to nullpunkt skal den returnere begge nullpunktene slik: (nullpunkt1, nullpunkt2) der begge nullpunktene skal være avrundet til 2 desimaler.

Eks:
   ```Python
def nullpunkt(a, b, c):
  #Kode her
  #Hvis ingen nullpunkt:
    return "Funksjonen har ingen nullpunkter!"
  #Hvis kun ett nullpunkt:
    return nullpunkt1 #Et flyttall avrundet til to desimaler.
  #Hvis to nullpunkt:
    return (nullpunkt1, nullpunkt2) En tuppel med to flyttall som begge er avrundet til to desimaler.
   ```
