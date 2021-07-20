import random

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
