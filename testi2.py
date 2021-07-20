import random
print("""

-----------------------------------------------

""")
teksti = """Ehken kaikella tällä on oma merkityksensä,
mutta silti, tämä on se asia mikä tässä viehättää.
Ei toki kaikkea kaiken aikaa, mutta toki tiettyjä
asioita on muuttuttava. Miten sitten muuttaa jotain
sellaista mikä on jo ennalta määriltelty, mutta voiko
jotain sellaista muuttaa vielä parempaan
suuntaan mistä olisi hyötyä {}


"""
print(teksti.upper())
print(teksti)

print(teksti.strip())

print(teksti.replace("k",'m'))
omakommandi = "testi"

testiä = """


Toimiiko Tämäkin


"""

print(teksti.format(testiä))

#########################################################################
print("""

-----------------------------

""")

tassa = 500
tassa2 = "Jotain tekstiä"
tassa3 = "Kerron vielä kertaalleen"
omateksti = """

Tähän kirjoitan pienen koodin  {}  Josta voisin jotain oppia
ja silti, jatkan vielä jotta voisin lisätä  {} tähän ja vielä toistamiseen
koitan {} ja edelleen.

"""

print(omateksti.format(tassa2, tassa, tassa3))
print("""

-------------------------------


""")
##########################################################################
print(omakommandi)

testi1 = "Tämä voisi jopa toimiakkin"
testi2 = "Tämä toimii vissiin myös"
def funktio():
    global r
    r = " Globaali funktio jota voi käyttää ilmeisesti hyvinkin ja ulkopuolella funktiosta"


    print(testi1 + r)
#    print(testi2)
funktio()
print(testi2 + r)

print("Hello")

##toimii
i = 3.14
o = 3
s = 2

print(i + o)

print("""

--------------------------------

""")

print(random.randrange(1,30))

#kolme lainausmerkkiä antaa luvan käyttää useammalla rivillä tekstiä
g = """Testi toimiiko
toimiiko edelleen
miten toimiiko
ja toimiiko vieläpä"""
print(g[0:15])       #kirjoittaa kyseisten lukujen merkit
print(len(g))
print(g[:5])
print(g[10:])

if "toimiiko" in g:
    print(" Tämäkin toimii")
if "edelleen" in g:
    print("Tämäkin löytyi")
if "Tässä" not in g:
    print("Lausetta tässä ei löytynyt")
#print(random.randrange(1,10))


print("""
-------------------------------------
""")

tama = "On tekstiä"
tama2 = "Osa tekstiä myös"
tama3 = 4
tama4 = 20

tassa5 = "Pieni kirjotelma, jos se onnistuu {} mitä \" Koe \" kirjoitan ja\n tämä on {}, jota kirjoitan edelleen {}\ntoden sanoo ja ehken vielä {}"

print(tassa5.format(tama4, tama2, tama3, tama))


print("""
-----------------------------------
""")

teksti1 = "Kokeillaan, montako merkkiä mahtuu yhteen, toiseen ja yhteen ja kolmanteen"
merkki = teksti1.count("yhteen")

print(merkki)

print(teksti1.index("m")) #missä sijaitsee m kirjain

print(teksti1.index("yhteen")) #kertoo missä kyseinen sana on

print("""

--------------------------------------

""")

tekstiä1 = "Kokeillaan taas toista kertaa miten homma toimisi"
tekstiä2 = "Yhteenkirjoitettuna"
test1 = tekstiä1.isalnum() #false koska välilyönnit
testi2 = tekstiä2.isalnum() #toimii koska Yhteenkirjoitettuna

print(test1) #false
print(testi2) #true
