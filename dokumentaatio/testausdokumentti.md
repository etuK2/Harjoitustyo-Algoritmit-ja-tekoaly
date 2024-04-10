# Testausdokumentti

## Testikattavuus

![Testikattavuus](./imgs/coveragereport.png)

## Testit

Tällä hetkellä on testattu vain pelin omien funktioden toimintaa ja toimivuutta.

Testeissä verrataan haluuttuun syötteeseen teisteistä saatua syötettä. Jotkut testit tarvitsevat valmiiksi luodun pelilaudan toimiakseen, joten näissä testeissä loin testeihi valmiit laudat ja suoritin testit niitten pohjalta. Testeissä on pääsääntöisesti syötteenä pelilauta, rivi, sarake ja pelinappula tai vain osa niistä.

## Testien suoritus

Suorita testit komennolla

```bash
poetry run invoke test
```

Aja testikattavuusraportti komennolla
```bash
poetry run invoke coverage
```