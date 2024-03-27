# Connect4 pelin määrittelydokumentti

#### Ohjelmointikieli:
Projektissa käytetään Python-ohjelmointikieltä.

#### Hallitut kielet:
Python.

#### Algoritmit ja tietorakenteet:
Projektissa toteutetaan Connect Four -pelin tekoäly käyttäen minimax-algoritmia alpha-beta karsinnalla. Lisäksi hyödynnetään tietorankenteena listoja pelilaudan käsittelyssä.

#### Ongelman ratkaisu:
Projektin tavoitteena on kehittää tekoäly, joka pystyy pelaamaan Connect Four -peliä vastaanottamalla pelilaudan tilanteen ja tekemällä parhaan mahdollisen siirron. Tekoälyn tulee pystyä arvioimaan eri siirtojen hyödyllisyyttä pelilaudan tilanteen perusteella ja valitsemaan niistä optimaalinen siirto.

#### Syötteet ja niiden käyttö:
Ohjelma saa syötteenään pelilaudan tilanteen, joka kuvaa pelilaudan tämänhetkistä tilaa. Syöte sisältää tiedon pelilaudan kunkin ruudun tilasta, esimerkiksi onko ruutu tyhjä vai onko siinä pelaajan merkki. Tämän tiedon perusteella tekoäly arvioi pelitilanteen ja tekee siirron.

#### Tavoitteena olevat aika- ja tilavaativuudet:
Minimax-algoritmin aikavaativuus on eksponentiaalinen, mutta alpha-beta karsinnan avulla pyritään vähentämään laskennan tarvetta. Aikavaativuuden tavoitteena on saavuttaa kohtuullinen suorituskyky, joka mahdollistaa tekoälyn pelaamisen ihmistä vastaan ilman liian pitkiä odotusaikoja. Tilavaativuuden osalta pyritään tehokkaaseen muistinkäyttöön, jotta pelin tilan arviointi ja siirtojen laskeminen on mahdollisimman resurssitehokasta.

#### Viitteet:
Connect Four -peliin liittyvät säännöt ovat samt kuin lautapeli versiossa.

#### Harjoitustyön ydin:
Projektin ydin on Connect Four -pelin tekoäly, joka pystyy pelaamaan peliä ihmistä vastaan. Tekoäly arvioi pelilaudan tilanteen ja valitsee optimaalisen siirron käyttäen minimax-algoritmia alpha-beta karsinnalla. Projektin tavoitteena on kehittää tekoäly, joka tarjoaa haastavan vastuksen pelaajalle ja kykenee pelaamaan peliä strategisesti oikein eri tilanteissa.

#### Opinto-ohjelma ja käytetty kieli:
Opinto-ohjelmani on tietojenkäsittelytieteen kandidaatti (TKT). Projektin dokumentaatiossa käytetty kieli on suomi mutta, koodin muuttujan ja nimet ovat englaninkielisiä.

## Viikkoraportit

[Viikko 1](./dokumentaatio/viikkoraportit/viikko1.md)

[Viikko 2](./dokumentaatio/viikkoraportit/viikko2.md)