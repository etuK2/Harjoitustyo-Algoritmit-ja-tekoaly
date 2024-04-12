# Toteutusdokumentti

## Ohjelman yleisrakenne

Connect Four -pelin toteutus koostuu kolmesta päämoduulista:

1. game.py: Tämä moduuli sisältää pelilogiikan, kuten pelilaudan luomisen, pelinappuloiden sijoittamisen, voittotilanteen tarkistamisen ja pelilaudan piirtämisen.

2. gameloop.py: Tämä moduuli hallitsee pelin kulkua, pelaajien vuoroja ja voittajan määrittämistä.

3. game_ai.py: Tämä moduuli sisältää tekoälyn, joka vastaa tietokonevastustajan liikkeistä.

## Saavutetut aika- ja tilavaativuudet

Aika- ja tilavaativuudet voidaan arvioida erikseen kullekin osalle ohjelmaa:

- Pelin tilavaativuus: Pelilaudan koko on vakio (6 riviä ja 7 saraketta), joten pelilaudan tilavaativuus on O(1). Muistinkäyttö on suoraan verrannollinen pelilaudan koko.

- Aikavaativuus: Pelin suorituskyky riippuu pelilaudan koosta ja tekoälyn käytöstä. Pelilaudan tarkistaminen voittotilanteen osalta vie enintään O(n), missä n on pelilaudan koko. Tekoälyn käyttö lisää aikavaativuutta riippuen määritetystä aika ja syvyysrajasta.

## Suorituskyky- ja O-analyysivertailu

Ohjelman suorituskykyyn vaikuttaa pelilaudan koko, tekoälyn käyttö ja syvyysraja minimax-algoritmissa. Koska Connect Four -pelin pelilaudan koko on kiinteä, suorituskykyä voidaan optimoida lähinnä tekoälyn osalta. Käytetyn tekoälyn algoritmi mahdollistaa hyvän suorituskyvyn verrattuna bruteforce-tarkistukseen, mutta syvien etsintäpuiden kanssa algoritmi voi olla hidasta. Iteratiivinen syveneminen parantaa suorituskykyä antamalla aikarajan jokaiselle siirrolle.

## Työn mahdolliset puutteet ja parannusehdotukset

Puutteita tai parannusehdotuksia:

- Käyttöliittymä: Ohjelma toimii pääasiassa tekstipohjaisena, mutta käyttöliittymän parantaminen graafiseksi voisi parantaa käyttökokemusta.

## Laajojen kielimallien käyttö

Olen käyttänyt ChatGPT 3.5 työssäni yksikkötestien pohjien luomiseen ja pylint virheiden korjaamiseen.