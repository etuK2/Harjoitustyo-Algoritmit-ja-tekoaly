# Käyttöohje

## Asennus ja käynnistys

Asenna riippuvuudet komennolla

```bash
poetry install --no-root
```

Käynnistä peli komennolla

```bash
poetry run invoke start
```

## Pelin pelaaminen ja säännöt

Peliä pelataan komentoterminaalissa. Pelilauta on jaettu 7 sarekkeeseen johon pelaaja voi laitaa nappulansa. Pelaajalla 1 eli sinulla on punaiset nappulat ja pelaajalla 2 eli tekoälyllä on keltaiset. Pelin aloittaa aina pelaaja 1.

Pelisiirrot tapahtuvat syötteen perusteella, minkä pelaaja antaa vuoronsa alussa. Syötteiden tulee olla jokin luku väliltä 1-7. Kun syöte on kelvollinen pelaajan nappula tiputetaan syötettä vastaavaan sarakkeen pohjalle. Sarakkeet on numeroitu vasemmalta oikealle eli kaikista vasemman puoleisin sarake on numeroltaan 1 ja kaikista oikein puolimmaisin sarake on 7.

Peliä pelataan vuorotelle. Tavoitteena on saada neljä omaa nappulaa vierekkäin, joko pysty, vaaka tai vinottaissuunnassa ja samalla estää vastapelaaja tekemästä samoin. Pelin voittaa siis se pelaaja joka saa ensimmäisenä neljä samanväristä nappulaa vierekkäin.

## Testit

Suorita testit komennolla

```bash
poetry run invoke test
```

Aja testikattavuusraportti komennolla
```bash
poetry run invoke coverage
```

Tee Pylint-tarkastukset komennolla
```bash
poetry run invoke pylint
```