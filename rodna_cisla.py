'''
Napiš tyto funkce. Každá z nich dostane jako argument řetězec s~rodným číslem a nějak ho zanalyzuje:

Je ve správném formátu: 6 číslice, lomítko, 4 číslice? (vrací True nebo False)
Je dělitelné jedenácti? (vrací True nebo False)
Jaké datum narození je v čísle zakódováno? (vrací trojici čísel – den, měsíc, rok)
Jaké pohlaví je v čísle zakódováno? (vrací 'muž' nebo 'žena')
Napiš i testy, abys ověřila, že funkce fungují správně.

Pro účely úkolu stačí, když bude program umět zpracovat čísla vydávaná od roku 1985. Reálná rodná čísla můžou být složitější :)
'''
from datetime import date
rc=input('Zadej sve rodne cislo s lomitkem: ')
#print(rc)


def kontrola_rc(rc):
    casti=rc.split("/")
    #print(casti)
    if len(casti[0])==6 and len(casti[1])==4:
        kontrola= True
    else:
        kontrola= False
    return kontrola

print("Je rodne cislo ve spravnem formatu: ", kontrola_rc(rc))


def delitelnost(rc):
    rc_edit = rc.replace("/", "")
    predchozi_soucet=0

    for cislo in rc_edit:
        cislo=int(cislo)
        suma=predchozi_soucet + cislo
        predchozi_soucet=suma

    if predchozi_soucet%11==0:
            kontrola_delitelnosti= True
    else:
            kontrola_delitelnosti= False
    return kontrola_delitelnosti

print("Je rodne cislo delitelne 11: ", delitelnost(rc))




def datum(rc):
    rok_pre=rc[0:2]
    rok_pre=int(rok_pre)
    if rok_pre >int((date.today().strftime("%y"))): #18
        rok=1900+rok_pre
    else:
        rok=2000+rok_pre

    mes_pre=rc[2:4]
    mes_pre=int(mes_pre)
    if mes_pre>50:
        mes=mes_pre-50
    else:
        mes=mes_pre

    den_pre=rc[4:6]
    den=int(den_pre)

    return(den,mes,rok)


print(datum(rc))

def pohlavi(rc):
    mes_pre=rc[2:4]
    mes_pre=int(mes_pre)
    
    if mes_pre>50:
        pohlavi='zena'
    else:
        pohlavi='muz'

    return pohlavi

print(pohlavi(rc))
