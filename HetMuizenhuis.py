# 'Het Muizenhuis'
import random, os
locaties, locatie, rugzak, muizenGevonden,voorwerpenGevonden, locatiesBezocht, ZizaMetToverstok, ZizaGesproken, DreisGesproken, vuurGemaakt, olifantenVerdreven, EngiOmgekocht, schapenGetemd, olifantenDoorMuizenDood, EarinVerslagen, kaart, GranRobijn, DreisGaatMee, schapenEten, boekGelezen = None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None

def reset(): #zet locaties op de goede waardes aan het begin van het spel en als het spel opnieuw wordt gespeeld
    global locaties, locatie, rugzak, muizenGevonden,voorwerpenGevonden, locatiesBezocht, ZizaMetToverstok, ZizaGesproken, DreisGesproken, vuurGemaakt, olifantenVerdreven, EngiOmgekocht, schapenGetemd, olifantenDoorMuizenDood, EarinVerslagen, kaart, GranRobijn, DreisGaatMee, schapenEten
    locaties = ['de resten van het Muizenhuis', 'een bos kreupelhout', 'de Heksenkring', 'de vuilnisbelt', 'de Vlakte van het Vuur', 'een groot meer', 'een weiland', 'het Moeras', 'het Olifantenpaleis']
    locatie = locaties[0] #je begint bij het muizenhuis
    rugzak = [] #inventory
    muizenGevonden = []
    voorwerpenGevonden = [] #wordt bijgehouden voor aan het einde van het spel, zodat je kunt zien hoeveel je had gevonden
    locatiesBezocht = ['de resten van het Muizenhuis'] #wordt bijgehouden voor aan het einde van het spel, zodat je kunt zien op hoeveel plekken je bent geweest
    # variabelen die gebeurtenissen in het spel bijhouden, om te checken of iets wel of niet kan of moet gebeuren:
    ZizaMetToverstok = False
    ZizaGesproken = False
    DreisGesproken = False
    vuurGemaakt = False
    olifantenVerdreven = False
    EngiOmgekocht = False
    schapenGetemd = False
    olifantenDoorMuizenDood = False
    EarinVerslagen = False
    GranRobijn = False
    DreisGaatMee = False
    schapenEten = False
    boekGelezen = False
    kaart ={ #dictionary met veel beschrijvingen en lists, die vaak met variabelen worden aangeroepen, waardoor ik de code een stuk korter kon schrijven
    #de beschrijvingen en voorwerpen die je kunt vinden per locatie:
        "de resten van het Muizenhuis" : {
            "beschrijving" : "Je ziet een grote hoop splinters, die ooit het muizenhuis vormden. Gran Famka zit ernaast, huilend.",
            "voorwerpen" : ["banaan", "blok kaas", "stoelpoot", "doosje met lucifers", "stapeltje geld"],
            "vinden": ['Tussen allemaal splinters vind je een ', 'Onder een stapel zwaar beschadigde boeken vind je een ', 'Achter een stapel versplinterde dakpannen ontdek je een ', 'Met grote moeite til je een matras op. Eronder ligt een ', 'Je wil het bijna opgeven, maar dan vind je onder een gedeukte oven een '],
            "richtingen": '''Je staat op een tweesplitsing:
1. het pad naar links leidt naar een plek waar veel hout ligt;
2. het pad naar rechts leidt naar een plek met veel paddenstoelen en mist.'''
            },
        "een bos kreupelhout" : {
            "beschrijving" : "Een luid gekraak komt van onder je voeten vandaan. Onder, voor, achter, overal om je heen liggen takken en stukken schors.",
            "voorwerpen" : ["bos takken", "stok", "stuk schors", "boek over wapens"],
            "vinden": ["Tussen een enorme stapel dennenappels vind je een ", "Achter een boom vind je een ", "Je kruipt een struik in en vind een ", "Nadat je in een stapel bladeren bent gesprongen, ontdek je dat erin iets ligt: een "],
            "richtingen": '''Je kunt drie kanten op:
1. het pad naar links ligt vol afval;
2. het pad naar rechts leidt naar een plek met veel water;
3. het laatste pad leidt naar het Muizenhuis.'''
            },
        "de Heksenkring" : {
            "beschrijving" : "Er hangt een groene mist rond de open plek waar je terecht bent gekomen. De open plek wordt omringd door honderden en nog eens honderden paddenstoelen.",
            "voorwerpen" : ["paddenstoelen die een walgelijke geur afstoten", 'veel bladeren'],
            "vinden": ['Aan de rand van de open plek vind je ', 'Verder het bos in vind je '],
            "richtingen": '''Je kunt drie kanten op:
1. het pad naar links leidt naar een plek met veel water;
2. het pad naar rechts is verbrand;
3. het laatste pad leidt naar het Muizenhuis.'''
            },
        "de vuilnisbelt" : {
            "beschrijving" : "Een smerige, zure stank dringt je neus binnen. In plaats van het mos dat hiervoor de aarde bedekte, is hier elke vierkante centimeter bedekt met rottend afval.",
            "voorwerpen" : ["robijn", "aansteker", "leeg blikje", "verroeste sleutel", "nagelschaartje"],
            "vinden" : ["Aan de rand van het afval vind je een ", "Je graaft wat in de hoop afval en vindt een ", "Tussen de wortels van een boom vind je een ", "Je loopt een rondje om de hoop afval en vind onderweg een ", "Je steekt je arm eens extra diep de hoop afval in en vindt een "],
            "richtingen": '''Je staat op een driesplitsing:
1. het pad naar links leidt naar een weiland;
2. het pad naar rechts lijkt vaak door olifanten te zijn belopen;
3. het laatste pad leidt naar een plek vol hout.'''
            },
        "de Vlakte van het Vuur" : {
            "beschrijving" : "Alles is zwart. De grond is zwart en is bezaaid met as en verkoolde takken, de bomen zijn niet meer dan verkoolde resten en er hangt een geur die je niet helemaal kunt plaatsen.",
            "richtingen": '''Er zijn drie richtingen die je op kunt:
1. het pad naar links lijkt vaak door olifanten te zijn belopen;
2. het pad rechtdoor leidt naar een moeras;
3. het laatste pad leidt naar een plek met veel paddenstoelen en mist.'''
            },
        "een groot meer" : {
            "beschrijving" : "Het meer strekt zich alle kanten op uit en je kan nog net de oever aan de overkant onderscheiden, waar iets gouds het zonlicht weerkaatst.",
            "voorwerpen" : ["Excalibur"],
            "vinden" : ["Je zwemt steeds dieper, totdat je de bodem hebt bereikt en je vingers zich sluiten om het gevest van een zwaard. Als je weer boven komt hap je naar lucht en kun je de letters lezen die op het zwaard staan: "],
            "richtingen": '''Je kunt twee kanten op:
1. het ene pad leidt naar een plek met veel paddenstoelen en mist;
2. het andere pad leidt naar een plek met veel hout.'''
            },
        "een weiland" : {
            "beschrijving" : "Gras. Schapen. Een gevoel van rust overvalt je."
            },
        "het Moeras" : {
            "beschrijving" : "Je voeten zakken weg in groene smurrie, die zover je kan zien alles bedekt."
            },
    #de muizen en de beschrijvingen bij het vinden van hen:
        "Tuen" : {
            'vind' : 'Terwijl je naar Gran Famka loopt, zie je dat er een muis naast haar zit. Het is Tuen!',
            "beschrijving" : '''Hij heeft een rondje gelopen, totdat hij uiteindelijk weer het Muizenhuis vond.
Hij neemt afscheid van Gran Famka en gaat met je mee op je zoektocht naar de andere muizen.
Nadat hij zich bij je heeft gevoegd, zegt hij:
    "Ik kwam onderweg trouwens langs een weiland vol met moordlustige schapen. Ik ben ze maar op het nippertje ontsnapt. Als je Ziza vindt en haar haar toverstok geeft, zouden we ze misschien samen kunnen temmen.
     Niet voor lang, maar misschien dat we ze kunnen gebruiken om de olifanten wat op de kast te jagen..."'''
            },
        "Maas" : {
            'vind' : 'Tussen al het hout vind je Maas!',
            "beschrijving" : '''Maas is de langste muis die je ooit heb gezien. Hij is verrast je te zien.
Je vertelt hem dat Gran Famka je eropuit heeft gestuurd om de muizen te zoeken. Maas besluit met je mee te gaan op je zoektocht.
Terwijl jullie teruglopen naar het pad, vertelt hij dat hij vroeger op de vuilnisbelt ging staan als ze verdwaald waren en dat hij dan de weg terug kon zien.''',
            'gevonden': "Je vindt niks interessants tussen het hout"
        },
        "Dreis" : {
            'vind' : 'Naast een afgebrande boom vind je Dreis!',
            "beschrijving" : '''Dreis is blij je te zien. Hij was per ongeluk op deze vlakte terecht gekomen terwijl hij zocht naar een banaan, want hij wilde net eentje gaan eten toen het huis werd aangevallen.
Je vertelt hem dat Gran Famka je eropuit heeft gestuurd om de muizen te zoeken.
Dreis zegt dat hij wel met je mee wil gaan op je zoektocht, in ruil voor een banaan. Als je die niet hebt, gaat hij liever terug naar het Muizenhuis.''',
            "gevonden" : "Je vindt niks interessants op de vlakte, behalve heel veel as."
        },
        "Thyen" : {
            'vind': 'De sleutel past! De kooi gaat open en Thyen stormt eruit.',
            'beschrijving' : 'Thyen is gelukkig niet gewond geraakt tijdens zijn verblijf bij de olifanten. Hij is blij dat hij eindelijk uit die kooi is en bedankt je dat je hem hebt gered.'
        },
    #de beschrijvingen voor als het spel eindigt:
        'gameOver': '''Je bent gestorven en hebt je missie niet kunnen volbrengen.
Dat betekent dat de muizen niet meer bij elkaar zullen komen, maar alsnog zullen worden vermoord door de olifanten.''',
        'win' : '''Je loopt opgetogen naar Gran Famka toe, met de muisjes achter je aan. Gran Famka kijkt verrast op.
    "Je hebt ze gevonden!" piept ze blij.

    Gefeliciteerd! Je hebt je missie volbracht en het spel gewonnen!'''
    }
    intro()

def clear(): #leegt het scherm na een lang stuk tekst is gelezen en op Enter is gedrukt
    input()
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print()

def clearInp(): #leegt het scherm nadat een antwoord is ingevoerd en op Enter is gedrukt
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print()

def eindSpel(x) : #voor als het spel is afgelopen: je bent dan gestorven of hebt gewonnen, de 'x' geeft aan wat het geval is
    global muizenGevonden, locatiesBezocht, voorwerpenGevonden
    print(kaart[x])
    print()

    #leuke statistieken:
    if len(muizenGevonden) == 6:
        print('Je hebt alle muizen gevonden')
    else:
        print(str(len(muizenGevonden)) + '/6 muizen gevonden')
    if len(voorwerpenGevonden) == 16 :
        print('Je hebt alle voorwerpen gevonden')
    else:
        print(str(len(voorwerpenGevonden)) + '/16 voorwerpen gevonden')
    if len(locatiesBezocht) == 9 :
        print('Je hebt alle locaties bezocht')
    else:
        print(str(len(locatiesBezocht)) + '/9 locaties bezocht')
    print()

    #credits:
    if x == 'win':
        print('''Dit spel is gemaakt door Femke Wenneker(alter ego: Gran Famka) en mede mogelijk gemaakt door:
* Clemens Wenneker (proeftester)
* Inge Wenneker(proeftester, alter ego: Engi)
* Zazi Nieuwenhuijs(alter ego: Ziza)
* Theyn Kan(alter ego: Thyen)
* Teun Heerze(alter ego: Tuen)
* Mees Moerel(alter ego: Maas)
* Dries Boermans(alter ego: Dreis)
* Aerin Gaston(alter ego: Earin)
* De docenten bij ICT in de wolken
''')

    #vragen of speler het spel opnieuw wil spelen:
    nietGekozen = True
    while nietGekozen :
        print('''Wil je het spel nog een keer spelen?
1. ja
2. nee
Kies 1 of 2''')
        antwoord = input()
        clearInp()
        if antwoord == '1':
            nietGekozen = False
            reset()
        elif antwoord == '2':
            nietGekozen = False
            exit()
        else:
            print('Dat was geen optie.')
            nietGekozen = True

def intro(): #begin van het spel, bevat uitleg over het spel
    global muizenGevonden, locatiesBezocht, voorwerpenGevonden
    introBezig = True
    print()
    print('''Welkom bij het spel \'Het Muizenhuis!\'
Druk op F11 voor een volledig scherm.
Druk op 'Enter' om door te gaan als je een stuk tekst hebt gelezen of een antwoord hebt ingevoerd.''')
    clear()
    print('Wat is je naam?')
    naam = input().capitalize()
    #hoezo, je mag jezelf geen voordelen gunnen?
    if naam == 'Femke':
        clearInp()
        eindSpel('win')
    clearInp()
    print('Hallo, ' + naam + '.')
    print()

    print('''Je bevindt je in het bos Mites Leucym.
Je hebt al een half uur een wanhopig gesnotter moeten aanhoren en je hebt eindelijk de bron gevonden.
Er zit een oude muis huilend naast een grote hoop splinters.
Je loopt op haar af en ze begint zodra ze je ziet te praten:

   "De olifanten hebben het Muizenhuis aangevallen en er is nog maar weinig van over...
    Alle muizen hebben kunnen vluchten, maar zijn nu verspreid door het bos...
    Ik ben Gran Famka, de huisoudste, en ik heb je hulp nodig de rest van de bewoners van het muizenhuis te vinden...
    Het zijn er zes: Ziza, Engi, Maas, Thyen, Tuen en Dreis...
    En een van hen is meegenomen door de olifanten...!
    Boehoehoe...
    Kan ik op je rekenen...?"

1. ja
2. nee
Kies 1 of 2''')

    while introBezig: # de speler heeft Gran Famka's vraag nog niet beantwoord
        antwoord = input()
        clearInp()
        if(antwoord == '1'):
            print('''    "Dankje...! Ik zal hier blijven wachten... Kom maar terug als je alle muizen hebt gevonden..."

Het kan zijn dat je onderweg spullen vindt. Gran Famka geeft je een rugzak om die spullen erin te doen.
Let wel op: Er passen maximaal acht voorwerpen in je rugzak.''')
            introBezig = False
            vertelLocatie() # het spel begint!
        elif(antwoord == '2'):
            print('Je draait je om en loopt weer weg van de muis. Na een tiental meters valt er een boom op je.')
            introBezig = False
            print()
            eindSpel('gameOver') # de speler is gestorven en het spel eindigt
        else: # er is een ongeldige waarde ingevoerd, de vraag wordt opnieuw gesteld
            print('''    "Sorry, was dat
            1. \'ja\' of
            2. \'nee\'...?
            M\'n gehoor is niet meer wat het ooit was..."
Kies 1 of 2 om Gran Famka's vraag te beantwoorden.''')
            introBezig = True

def vertelInhoudRZ(): #display van welke voorwerpen je in je rugzak hebt
    global rugzak
    if len(rugzak) == 0:
        print('Je hebt momenteel geen voorwerpen in je rugzak.')
    else:
        print()
        print('Je hebt nu de volgende voorwerpen:')
        for x in rugzak:
            print(x)
        print()
        #vertel hoeveel voorwerpen in je rugzak zitten:
        if len(rugzak) > 1:
            print('Je hebt nu', len(rugzak), 'voorwerpen in je rugzak.')
        else:
            print('Je hebt nu 1 voorwerp in je rugzak.')

def nogEenActie(): #vragen of de speler nog een speciale actie van voorwerpActies(x) wil uitvoeren
    print()
    print('''Wil je nog een actie uitvoeren?
1. ja
2. nee
Kies 1 of 2''')
    antwoord = input()
    clearInp()
    if antwoord == '1':
        voorwerpActies(True)
    elif antwoord == '2':
        actieVragen()
    else:
        print('Dat was geen optie.')
        nogEenActie()

def voorwerpActies(x): # de inhoud van je rugzak bekijken en eventueel speciale acties met voorwerpen uitvoeren. Optie 3 bij actieVragen()
    global rugzak, muizenGevonden, locatie, locaties, EarinVerslagen, ZizaMetToverstok, boekGelezen
    if not x: #alleen inhoud van de rugzak laten zien als die nog niet is bekeken (x = False)
        vertelInhoudRZ()
        print()
        if 'stok'in rugzak and 'Ziza' in muizenGevonden:
            print('''Ziza merkt de stok op in je tas en haar ogen worden groot.
    "Mijn toverstok!" roept ze.
Je kijkt verbaasd naar de stok. Hij ziet eruit als een doodnormale stok.
Is Ziza langzaam gek aan het worden? Of is het echt een toverstok?''')
            print()
    acties = []
    # kijk welke acties mogelijk zijn:
    if 'boek over wapens' in rugzak:
        acties.append("het boek over wapens lezen")
    if 'blok kaas' in rugzak:
        acties.append("het blok kaas eten")
    if 'blok kaas' in rugzak and 'paddenstoelen die een walgelijke geur afstoten' in rugzak:
        acties.append("een stinkbom maken met het blok kaas en de paddenstoelen die een walgelijke geur afstoten")
    if 'leeg blikje' in rugzak:
        acties.append("het lege blikje hooghouden")
    if 'nagelschaartje' in rugzak:
        acties.append("je nagels knippen met het nagelschaartje")
    if 'stok' in rugzak and 'Ziza' in muizenGevonden:
        acties.append("de (tover)stok aan Ziza geven")
    if 'stapeltje geld' in rugzak and locatie == locaties[0]:
        acties.append('het geld geven aan Gran Famka')
    if 'verroeste sleutel' in rugzak and EarinVerslagen:
        acties.append('proberen Theyns kooi open te maken met de verroeste sleutel')
    if 'banaan' in rugzak:
        acties.append("de banaan eten")

    nietGekozen = True
    while nietGekozen:
        # geef de speler de keuze te kiezen tussen de mogelijke acties
        if len(acties) == 0:
            print('Je kunt geen speciale acties uit voeren.')
            nietGekozen = False
            print()
            actieVragen()
        else:
            print('Je kunt de volgende speciale acties uitvoeren:')
            for a in acties:
                print(str(acties.index(a) + 1) + '.', a)
            print(str(len(acties) + 1) + '. geen speciale actie uitvoeren')
            print()

            print('Wat wil je doen? Kies tussen de getallen 1 t/m', len(acties) + 1)
            antwoord = input()
            clearInp()
            if antwoord == str(len(acties) + 1):
                actieVragen()
            try: # try en except gebruikt om errors te voorkomen; voert de gekozen actie uit
                antwoordA = acties[int(antwoord) - 1]
                if antwoordA == 'het boek over wapens lezen':
                    print('''Dit is wat er in het boek staat:
    "Als je tegen de olifantenkoningin wilt vechten, zijn er verschillende wapens die nuttig zouden kunnen zijn. De belangrijkste en effectiefste is:
     Excalibur: een machtig, volgens legendes magisch, zwaard, waarmee je zelfs een koninklijke olifant zou kunnen uitschakelen. Dit zwaard is echter al eeuwen zoek...
                Er zijn geruchten die zeggen dat het in een meer ligt...
     Tegen een grote groep olifanten kun je het beste de volgende gebruiken:
     1. vuur: de meeste olifanten vluchten hiervoor. Je kunt het maken met lucifers of een aansteker en een brandstof.
                Let wel op: het lukt niet altijd, en als het lukt is er een kans dat het uit de hand loopt. Die kans wordt beinvloed door welke aansteker en brandstof je gebruikt.
     2. moordlustige wezens die de olifanten opeten: leeuwen of gemuteerde wezens voldoen vaak, vooral als ze honger hebben
     3. ze ontwijken via een achteringang: het enige probleem is dat er niet veel zijn die weten waar de achteringang van het Olifantenpaleis is
     4. een leger van vier muizen: gek genoeg soms sterker dan een heleboel olifanten, je hebt wel nog een vijfde nodig om de deur open te krijgen." ''')
                    boekGelezen = True
                    nietGekozen = False
                elif antwoordA == 'het blok kaas eten':
                    print('Je eet het blok kaas met smaak op. Het geeft je net het beetje energie dat je nodig had om je zoektocht naar de muizen door te zetten.')
                    rugzak.remove('blok kaas')
                elif antwoordA == 'een stinkbom maken met het blok kaas en de paddenstoelen die een walgelijke geur afstoten':
                    print('''Het kost je wat moeite, maar dan heb je ook wat: een prachtige stinkbom die je op eventuele vijanden zou kunnen gooien.
De stank is waarschijnlijk zo sterk, dat het bijvoorbeeld een muis zo zou kunnen uitschakelen.
Je weet alleen niet hoe ver de stank zou reiken en of het dus willekeurige omstanders, waaronder jijzelf, ook zou uitschakelen.
Je haalt je schouders op. Dat zie je nog wel. Je doet je stinkbom in je rugtas.''')
                    rugzak.remove('blok kaas')
                    rugzak.remove('paddenstoelen die een walgelijke geur afstoten')
                    rugzak.append('stinkbom')
                    nietGekozen = False
                elif antwoordA == 'het lege blikje hooghouden':
                    print('''De zoektocht vind je een beetje saai worden. Terwijl je naar het blikje in je tas krijgt, krijg je een goed idee.
Je houdt het met je voet hoog en begint te tellen.

Je houdt het blikje''', random.randint(1,100), '''keer hoog, voor je het per ongeluk het bos in schiet.
Je kan het niet meer terugvinden.''')
                    rugzak.remove('leeg blikje')
                    nietGekozen = False
                elif antwoordA == 'je nagels knippen met het nagelschaartje':
                    print('''Je knipt je nagels netjes kort. Bij de laatste nagel die je knipt, breekt het schaartje.
De resten vliegen weg en je kunt ze niet meer terugvinden.''')
                    rugzak.remove('nagelschaartje')
                    nietGekozen = False
                elif antwoordA == 'de (tover)stok aan Ziza geven':
                    print('''Je geeft de stok twijfelend aan Ziza, die hem gretig aanneemt.
Zodra ze de stok vastpakt, ontstaat er een fel licht.

Nadat het licht is weggevaagd, zie je dat de stok nu prachtig bewerkt is. Ziza grijnst.
Ze zwaait met de stok, waar vuurwerk uitschiet. Het was dus echt een toverstok.''')
                    rugzak.remove('stok')
                    ZizaMetToverstok = True
                    nietGekozen = False
                elif antwoordA == 'het geld geven aan Gran Famka':
                    print('''Je loopt naar Gran Famka en laat het stapeltje geld vallen in haar schoot. Ze kijkt je verbaasd aan.
    "Bedankt...! Ik zal het hard nodig hebben om het huis weer op te bouwen... Als we tenminste deze verschrikkelijke situatie overleven..."
Je knikt, trots op deze goede daad. Je vraagt je alleen wel af of jij het eigenlijk niet ook had kunnen gebruiken...''')
                    rugzak.remove('stapeltje geld')
                    nietGekozen = False
                elif antwoordA == 'proberen Theyns kooi open te maken met de verroeste sleutel':
                    rugzak.remove('verroeste sleutel')
                    nietGekozen = False
                    muisVinden('Thyen')
                elif antwoordA == 'de banaan eten':
                    print('Je eet de banaan tevreden op. Het geeft je net het beetje energie dat je nodig had om je zoektocht naar de muizen door te zetten, maar je vraagt je ergens af of iemand anders deze banaan misschien nog wilde.')
                    rugzak.remove('banaan')
                nietGekozen = False
            except (ValueError, IndexError) as e :
                print('Dat was geen optie.')
                nietGekozen = True
        nogEenActie()

def vertelLocatie(): # vertel waar de speler zich bevindt en beschrijf hoe het eruit ziet, optie 4 bij actieVragen()
    global schapenGetemd, locatie, locaties, muizenGevonden, ZizaMetToverstok
    print('Je bent nu bij ' + locatie)
    print(kaart[locatie]['beschrijving'])

    if locatie == locaties[6]: # speciaal geval: het weiland, geen speciale acties behalve als je Tuen hebt gevonden en Ziza haar toverstok hebt gegeven
        if 'Tuen' in muizenGevonden and ZizaMetToverstok and not schapenGetemd:
            print('''Tuen lokt de schapen, die met ontblote tanden op hem afkomen. Hun tanden zijn ongelofelijk scherp.
        Ziza zwaait met haar toverstok en zegt:
            "Oh, kudde gemuteerde schapen, gij zijt vijandig tot de verkeerde! Eet olifanten, geen muizen!" gevolgd door een hoop onverstaanbare woorden.
        Er knalt iets uit haar toverstok en de schapen blijven plots stilstaan, bedekt met gouden spikkels.
        De voorste buigt zijn hoofd en begint, tot je grootste verbazing, te praten.
            "Schapen... Er staat olifant op het menu!"
        Ze denderen allemaal langs je. ''')
            schapenEten = True # de schapen hebben de olifanten gegeten
            if olifantenVerdreven: # er is eerder al succesvol een vuur gemaakt: dit beinvloed wat er wordt verteld
                print('''Even later komen ze terug.
    "Er waren geen olifanten", zeggen ze, "maar wel veel rook".
Ze kijken nogal moordlustig, dus je vlucht terug naar de vuilnisbelt.''')
            else:
                print('''Al snel volgen er geluiden waar je uit opmaakt dat de schapen erg aan het genieten zijn van hun maaltijd.

        Even later komen de schapen met bebloede vacht en volle maag terug.
            "Alleen de koningin hebben we niet kunnen eten, maar de rest..."
        Het schaap dat sprak staart dromend naar de lucht.

        Samen met Ziza en Tuen ga je terug naar de vuilnisbelt.
''')
            schapenGetemd = True
            locatie = locaties[3] # locatie gaat terug naar de vuilnisbelt
            vertelLocatie()
        else:
            weiland()
    elif locatie == locaties[7]: #speciaal geval: het moeras: er zijn geen speciale acties uit te voeren, dus het moeras heeft een andere functie
        moeras()

    print()
    actieVragen()

def richtingKiezen(): #vraagt waar de speler heen wilt, optie 2 bij actieVragen()
    global locatie, locaties, locatiesBezocht
    print(kaart[locatie]['richtingen']) #vertelt welke kanten je op kunt
    print()

    if locatie == locaties[0] or locatie == locaties[5]: #2 richtingen mogelijk
        print('Welke kant ga je op? Kies 1 of 2')
        antwoord = input()
        clearInp()
        #hieronder wordt de locatie naar de nieuwe locatie aangepast:
        if(antwoord == '1'): #naar links
            if locatie == locaties[0]:
                locatie = locaties[1]
            elif locatie == locaties[5]:
                locatie = locaties[2]
        elif(antwoord == '2'): #naar rechts
            if locatie == locaties[0]:
                locatie = locaties[2]
            elif locatie == locaties[5]:
                locatie = locaties[1]
            else:
                print('Dat was geen optie')
                print()
                richtingKiezen()

    else: #3 richtingen mogelijk
        print('Welke kant ga je op? Kies 1, 2 of 3')
        antwoord = input()
        clearInp()
        if(antwoord == '1'): #naar links
            if locatie == locaties[1]:
                locatie = locaties[3]
            elif locatie == locaties[2]:
                locatie = locaties[5]
            elif locatie == locaties[3]:
                locatie = locaties[6]
            elif locatie == locaties[4]:
                if EarinVerslagen:
                    print('Het olifantenpaleis is nu niet meer een bezoekbare locatie. Het gebied is onbegaanbaar.')
                    print()
                    actieVragen()
                else:
                    olifantenpaleis.betreden()

        elif(antwoord == '2'): #naar rechts
            if locatie == locaties[1]:
                locatie = locaties[5]
            elif locatie == locaties[2]:
                locatie = locaties[4]
            elif locatie == locaties[3]:
                if EarinVerslagen:
                    print('Het olifantenpaleis is nu niet meer een bezoekbare locatie. Het gebied is onbegaanbaar.')
                    print()
                    actieVragen()
                else:
                    olifantenpaleis.betreden()
            elif locatie == locaties[4]:
                locatie = locaties[7]

        elif(antwoord == '3'): #laatste optie
            if locatie == locaties[1]:
                locatie = locaties[0]
            elif locatie == locaties[2]:
                locatie = locaties[0]
            elif locatie == locaties[3]:
                locatie = locaties[1]
            elif locatie == locaties[4]:
                locatie = locaties[2]

        else:
            print('Dat was geen optie')
            print()
            richtingKiezen()

    if locatie not in locatiesBezocht : #als een locatie nog niet is bezocht, wordt het toegevoegd aan de list
        locatiesBezocht.append(locatie)
    vertelLocatie()

def actieVragen(): #vragen welke actie de speler uit wil voeren
    print('''Wat wil je doen?
1. een actie uitvoeren op deze locatie
2. doorgaan naar een andere locatie
3. de inhoud van je rugzak bekijken of een speciale actie met een voorwerp uitvoeren
4. (opnieuw) de locatie bekijken
Kies 1, 2, 3 of 4''')
    antwoord = input()
    clearInp()
    if antwoord == '1': #elke locatie heeft zijn eigen rondkijkfunctie
        if locatie == locaties[0]:
            muizenhuis.rondkijken()
        elif locatie == locaties[1]:
            kreupelhout.rondkijken()
        elif locatie == locaties[2]:
            heksenkring.rondkijken()
        elif locatie == locaties[3]:
            vuilnisbelt.rondkijken()
        elif locatie == locaties[4]:
            vuurvlakte.rondkijken()
        elif locatie == locaties[5]:
            meer.rondkijken()
    elif antwoord == '2' :
        richtingKiezen()
    elif antwoord == '3':
        voorwerpActies(False)
    elif antwoord == '4':
        vertelLocatie()
    else:
        print('Dat was geen optie')
        actieVragen()

def voorwerpHouden(g): #g = het voorwerp; functie om het voorwerp dat is gevonden te houden
    global voorwerpenGevonden, rugzak, locatie
    kaart[locatie]['vinden'].pop(0)
    print('Je gevonden ' + g + ' stop je in je rugzak.')
    rugzak.insert(0, g)
    if g not in voorwerpenGevonden:
        voorwerpenGevonden.append(g)
    kaart[locatie]['voorwerpen'].remove(g)
    vertelInhoudRZ()
    print()
    opnieuwZoeken()

def opnieuwZoeken(): #vraag of de speler door wil zoeken
    print('''Wil je doorzoeken?
1. ja
2. nee
Kies 1 of 2''')
    antwoord = input()
    clearInp()
    if antwoord == '1':
        vind()
    elif antwoord == '2':
        actieVragen()
    else:
        print('Dat was geen optie. Kies opnieuw: wil je doorgaan met zoeken?')
        opnieuwZoeken()

def vind():#functie om een voorwerp te vinden: kan op locaties[0],[1],[2],[3] en [5]
    global locatie, locaties, rugzak
    teVindenVoorwerpen= kaart[locatie]['voorwerpen']

    if len(teVindenVoorwerpen) > 0:
        gevondenVoorwerp = str(random.choice(teVindenVoorwerpen)) # selecteer een willekeurig voorwerp uit de list
        print(str(kaart[locatie]['vinden'][0]) + gevondenVoorwerp + '''. Wil je deze houden?
1. ja
2. nee
Kies 1 of 2''')

        nietGekozen = True
        while nietGekozen:
            antwoord = input()
            clearInp()
            if(antwoord == '1'):
                if len(rugzak) < 8:
                    voorwerpHouden(gevondenVoorwerp)
                else:
                    print('''Je hebt momenteel het maximale aantal spullen in je rugzak.
Je kunt je rugzak leger maken door een voorwerp weg te gooien op de vuilnisbelt of door een voorwerp te vernietigen.''')
                    nietGekozen2 = True
                    while nietGekozen2:
                        print('''Wil je een voorwerp vernietigen? Let op: je kunt het dan in de rest van het spel niet meer gebruiken.
1. ja
2. nee
Kies 1 of 2''')
                        antwoord2 = input()
                        clearInp()
                        if antwoord2 == '1':
                            nietGekozen3 = True
                            while nietGekozen3:
                                print('Je hebt de volgende voorwerpen:')
                                for x in rugzak:
                                    print(str(rugzak.index(x) + 1) + '.', x)
                                print()
                                print('Wat wil je vernietigen? Kies tussen de getallen 1 t/m', len(rugzak))
                                try: # voorkom errors
                                    antwoord3 = rugzak[int(input()) - 1]
                                    clearInp()
                                    if antwoord3 in rugzak:
                                        rugzak.remove(antwoord3)
                                        print('Je hebt je ' + antwoord3 + ' vernietigd!' )
                                        voorwerpHouden(gevondenVoorwerp)
                                        nietGekozen3 = False
                                    else:
                                        print('Dat is geen optie.')
                                        nietGekozen3 = True
                                except (ValueError, IndexError) as e:
                                    print('Dat is geen optie.')
                                    nietGekozen3 = True
                            nietGekozen2 = False

                        elif antwoord2 == '2':
                            print('Je legt het voorwerp terug waar je het had gevonden.')
                            nietGekozen2 = False

                        else:
                            print('Dat was geen optie. Kies opnieuw.')
                            nietGekozen2 = True

                nietGekozen = False

            elif(antwoord == '2'):
                print("Je bekijkt het even, maar gooit het dan terug.")
                opnieuwZoeken()
                nietGekozen = False

            else:
                print('Dat was geen optie. Wil je je', gevondenVoorwerp, '''houden?
1. ja
2. nee
Kies 1 of 2''')
    else:
        print('Je vindt niks interessants. Blijkbaar heb je hier alles al weggehaald.')
    print()
    actieVragen()

def voorwerpVoorMuis(v, m): #v = het voorwerp, m = de muis; functie om een voorwerp aan een muis te geven, nodig bij Ziza(een robijn) en Dreis(een banaan)
    global DreisGesproken, ZizaGesproken, muizenGevonden, DreisGaatMee
    print('Je hebt een ' + v + ', wil je die aan ' + m + ''' geven?
1. ja
2. nee
Kies 1 of 2''')

    nietGekozen = True
    while nietGekozen:
        antwoord = input()
        clearInp()
        if(antwoord == '1'):
            print('Je haalt een ' + v + ' uit je rugzak en geeft hem aan ' + m + '. ' + m + ' kijkt je dolgelukkig aan.')
            print()
            print('     "Oke dan, ik ga met je mee op je zoektocht."')
            print()
            rugzak.remove(v)
            if m == 'Dreis':
                print('     "Ik kan je wel aanraden later nog eens terug te komen hier. Tuen kent de wegen erg goed, het kan zijn dat hij de weg terug heeft gevonden naar huis", zegt hij.')
                DreisGaatMee = True
                DreisGesproken = False
            elif m == 'Ziza':
                ZizaGesproken = False
                muizenGevonden.append(m) # Ziza vinden gaat niet via muisVinden(m), want haar vinden gaat wat anders dan bij de andere muizen
                if len(muizenGevonden) == 1:
                    print('Je hebt nu', len(muizenGevonden), 'muis gevonden:')
                    for x in muizenGevonden:
                        print(x)
                elif len(muizenGevonden) == 6:
                    print('Je hebt alle muizen gevonden! Ga naar Gran Famka op je missie te voltooien.')
                else:
                    print('Je hebt nu', len(muizenGevonden), 'muizen gevonden:')
                    for x in muizenGevonden:
                        print(x)
                print()
                actieVragen()
            nietGekozen = False

        elif(antwoord == '2'):
            if m == 'Dreis':
                print("Je zegt tegen Dreis dat je geen banaan hebt. Dreis zegt dat hij bij het Muizenhuis zal zijn als je hem nodig hebt.")
                DreisGesproken = True
            elif m == 'Ziza':
                print('Ziza negeert je.')
                ZizaGesproken = True
            nietGekozen = False

        else:
            print('Dat was geen optie. Wil je je ' + v + ' aan ' + m + ' geven?.')
    print()
    actieVragen()

def muisVinden(m): #m = de muis die je vindt, de functie beschrijft het vinden van die muis
    global muizenGevonden, DreisGesproken
    if m in muizenGevonden:
        print(kaart[m]['gevonden'])
        print()
        actieVragen()
    else:
        print(kaart[m]['vind'])
        print(kaart[m]['beschrijving'])
        print()
        muizenGevonden.append(m)
        if len(muizenGevonden) == 1:
            print('Je hebt nu', len(muizenGevonden), 'muis gevonden:')
            for x in muizenGevonden:
                print(x)
        elif len(muizenGevonden) == 6:
            print('Je hebt alle muizen gevonden! Ga naar Gran Famka op je missie te voltooien.')
        else:
            print('Je hebt nu', len(muizenGevonden), 'muizen gevonden:')
            for x in muizenGevonden:
                print(x)

        if m == 'Dreis' :
            print()
            if 'banaan'in rugzak:
                voorwerpVoorMuis('banaan', 'Dreis')
            else:
                print('Je hebt geen banaan, dus je legt Dreis uit hoe hij bij het Muizenhuis moet komen en hij vertrekt. Je zult je zoektocht zonder Dreis moeten voortzetten. Als je wel een banaan hebt, kun je die aan hem geven bij het Muizenhuis.')
                DreisGesproken = True

        print()
        actieVragen()

def weiland(): #wordt uitgevoerd als je het weiland(locaties[6]) betreedt
    global schapenGetemd, locatie, locaties
    print('''Wil je
1. doorlopen en al je zorgen achter je laten of
2. terugkeren naar de vuilnisbelt?
Kies 1 of 2''')
    antwoord = input()
    clearInp()
    if antwoord == '1':
        print('Je loopt door het weiland, weg van het bos. Je laat alles achter, vergeet wat je ookal weer aan het doen was en verdwijnt in de uitgestrektheid van het landschap.')
        print()
        print('De schapen in het weiland waren door radioactieve straling gemuteerd tot moordlustige wezens en rijten je uiteen met hun tanden.')
        print()
        eindSpel('gameOver')
    elif antwoord == '2':
        locatie = locaties[3]
        vertelLocatie()
    else:
        print('Dat was geen optie')
        weiland()

def moeras(): #wordt uitgevoerd als je het moeras(locaties[7]) betreedt
    global locatie, locaties
    print('''Wil je
1. het moeras in lopen of
2. terugkeren naar de Vlakte van het Vuur?
Kies 1 of 2''')
    antwoord = input()
    clearInp()
    if antwoord == '1':
        print('Je zet drie stappen het moeras in, zakt weg en verdrinkt in het drijfzand.')
        print()
        eindSpel('gameOver')
    elif antwoord == '2':
        locatie = locaties[4]
        actieVragen()
    else:
        print('Dat was geen optie')
        moeras()

class muizenhuis: #de functies die horen bij locaties[0]
    def rondkijken():
        print('''Wil je
1. met Gran Famka praten of
2. een kijkje nemen bij de resten van het Muizenhuis?
Kies 1 of 2''')
        antwoord = input()
        clearInp()
        if antwoord == '1':
            muizenhuis.GranFamka()
        elif antwoord == '2':
            vind()
        else:
            print('Dat was geen optie')
            muizenhuis.rondkijken()

    def GranFamka(): #er zijn verschillende acties die je toegang kunnen geven tot een nieuwe interactie met Gran Famka
        global muizenGevonden, GranRobijn, DreisGesproken, ZizaGesproken, rugzak

        if DreisGesproken and 'banaan' not in rugzak:
            print('Dreis hangt rond in de buurt van Gran Famka, op zoek naar een banaan.')
            print()

        if DreisGaatMee and 'Tuen' not in muizenGevonden:
            muisVinden('Tuen')

        elif DreisGesproken and 'banaan' in rugzak:
            print("Naast Gran Famka zit Dreis.")
            voorwerpVoorMuis('banaan', 'Dreis')

        elif ZizaGesproken:
            print('''Je gaat naast Gran Famka zitten en wacht totdat ze je opmerkt.

    "Wat moet je...?"

Je vertelt haar over je ontmoeting met Ziza en dat ze niet mee wil zonder haar dierbaarste voorwerp.
    "Weet jij misschien wat dat is?", vraag je.

Gran Famka is even stil, maar zegt dan:
    "Een robijn..."
Dan keert ze zich weer van je af en gaat door met huilen.''')
            GranRobijn = True

        elif len(muizenGevonden) < 6:
            print('''Je loopt naar Gran Famka en gaat naast haar zitten. Gran Famka merkt je niet op en blijft dramatsich huilen.
Je schraapt je keel.
Gran Famka kijkt op met een betraand gezicht en vraagt:

    "Heb je ze gevonden...? Heb je mijn familie gevonden...?"

Je schudt je hoofd. Nog voor je kunt vragen naar informatie over waar je ze zou kunnen vinden, heeft Gran Famka je de rug toegekeerd.''')
            print()

        else:
            eindSpel('win')

        print()
        actieVragen()

class kreupelhout: #de functie die hoort bij locaties[1]
    def rondkijken():
        print('''Wil je
1. naar een muis zoeken of
2. tussen het hout naar voorwerpen zoeken?
Kies 1 of 2''')
        antwoord = input()
        clearInp()
        if antwoord == '1':
            muisVinden('Maas')
        elif antwoord == '2':
            vind()
        else:
            print('Dat was geen optie')
            kreupelbout.rondkijken()

class heksenkring: #de functies die horen bij locaties[2]
    def rondkijken():
        global muizenGevonden
        if 'Ziza' in muizenGevonden:
            print('''De open plek is nog steeds mistig, maar verder is de rust teruggekeerd nu Ziza weg is.
Wil je
1. het midden van de open plek bekijken
2. de muis met rust laten en de plek rondom de open plek onderzoeken?
Kies 1 of 2''')
        else:
            print('''Nu je beter kijkt, zie je dat in het midden van de open plek een muis zit, die iets aan het mompelen is en haar armen beweegt, waardoor de mist gaat wervelen.
Wil je
1. met de muis praten of
2. de muis met rust laten en de plek rondom de open plek onderzoeken?
Kies 1 of 2''')
        antwoord = input()
        clearInp()
        if antwoord == '1':
            heksenkring.Ziza()
        elif antwoord == '2':
            vind()
        else:
            print('Dat was geen optie')
            heksenkring.rondkijken()

    def Ziza():
        global ZizaGesproken, GranRobijn, rugzak, muizenGevonden
        if ZizaGesproken and 'robijn' not in rugzak and not GranRobijn:
            print('Je hebt Ziza\'s dierbaarste voorwerp nodig om haar over te halen met je mee te gaan. Vind eerst uit wat dat voorwerp is. Ziza negeert je.')
        elif ZizaGesproken and 'robijn' not in rugzak and GranRobijn:
            print('Je hebt een robijn nodig om Ziza over te halen met je mee te gaan. Je hebt geen robijn, dus Ziza negeert je.')
        elif ZizaGesproken and 'robijn' in rugzak:
            voorwerpVoorMuis('robijn', 'Ziza')
        elif 'Ziza' in muizenGevonden:
            print('De open plek is leeg.')
        else:
            print('''Je loopt naar de muis toe, die ongestoord verder gaat. De muis heeft haar ogen dicht, dus ze ziet je niet.

Je kucht.

De muis lijkt nog steeds je aanwezigheid niet te hebben bemerkt.

Dan vertraagt de beweging van haar armen en onstaat er paarse mist. De mist omhult jou en de muis, totdat je alleen haar nog ziet.
Na een tijdje begint ze te praten:

    "Het Oog had me al ingelicht over je komst", zegt ze.
Haar stem lijkt van overal te komen en je wordt een beetje duizelig.

    "Ik ben Ziza De Alwetende. Je verlangt van me dat ik me herenig met mijn familie, in opdracht van Gran Famka."
     Dat had je gedacht. Ik ben eindelijk vrij mijn kunsten te beoefenen."
Hier was je niet op voorbereid. Na wat een eeuwigheid lijkt, begint Ziza opeens weer met praten:

    "Alleen als je mij mijn dierbaarste voorwerp brengt, zal ik overwegen met je mee te gaan. Anders. Niet."

De paarse mist verdwijnt en je bent weer omringt door de bomen van de open plek.
Je vraagt je af of Gran Famka misschien weet wat Ziza's dierbaarste voorwerp is.''')
            ZizaGesproken = True #ZizaGesproken = True als je met haar hebt gesproken, maar nog niet hebt gevonden
        print()
        actieVragen()

class vuilnisbelt: #de functies die horen bij locaties[3]
    def rondkijken():
        print('''Wil je
1. tussen het afval zoeken,
2. op de hoop afval gaan staan en om je heen kijken of
3. een voorwerp weggooien?
Kies 1, 2 of 3''')
        antwoord = input()
        clearInp()
        if antwoord == '1':
            vind()
        elif antwoord == '2':
            vuilnisbelt.uitzicht()
        elif antwoord == '3':
            vuilnisbelt.weggooien()
        else:
            print('Dat was geen optie')
            vuilnisbelt.rondkijken()

    def uitzicht():
        if 'Maas' in muizenGevonden:
            print('''Je maakt net aanstalten om de hoop op te klimmen, als Maas je aantikt.
    "Je kunt beter aan de andere kant omhoog klimmen. De andere kant is beter beklimbaar."
Hij leidt je om de hoop heen en wijst je het pad omhoog. Jullie beginnen te klimmen.

Eenmaal op de top kijk je om je heen, maar je ziet alleen maar bomen. Je wilt alweer naar beneden gaan, maar Maas houdt je tegen.
    "Waarom loop je weg? Je hebt hier perfect uitzicht over het hele bos!"
Vervolgens legt hij je alles uit wat hij ziet:

     "Vanaf hier terug kom je bij het kreupelhout, en daar weer terug bij het muizenhuis.
      Als je hier naar rechts gaat, kom je bij een groot meer.
      Hier naar links is een weiland.
      Verder kan ik het niet zo goed zien, maar ik zie rechts van het weiland iets glinsteren en achter het meer komen rookpluimen en heel veel groene mist het bos uit."

Nadat jullie nog even op de hoop afval hebben gestaan, klimmen jullie weer naar beneden en lopen weer naar de andere kant van de hoop.''')
        else:
            print('''Je glijdt een aantal keer bijna in het rottende afval, maar komt na een hoop moeite dan eindelijk aan op de top van de hoop afval.
Je komt even op adem en kijkt vervolgens om je heen. Er is niks te zien.

Na veel moeite en ontmoetingen met substanties waarvan je liever niet wil weten wat het is, kom je uiteindelijk weer beneden.''')
        print()
        actieVragen()

    def weggooien():
        global rugzak, locatie
        if len(rugzak) == 0:
            print('Je hebt geen voorwerpen in je rugzak, dus je kunt niks weggooien.')
        else:
            nietGekozen = True
            while nietGekozen:
                if len(rugzak) == 1:
                    print('Je hebt maar 1 voorwerp:')
                    for x in rugzak:
                        print(x)
                    weggegooidVoorwerp = wapens[0]
                else:
                    print('Je hebt de volgende voorwerpen:')
                    for x in rugzak:
                        print(str(rugzak.index(x) + 1) + '.', x)
                        print()
                        print('Welk voorwerp wil je weggooien Kies tussen de getallen 1 t/m', len(rugzak))
                    try: #voorkom errors
                        weggegooidVoorwerp = rugzak[int(input()) - 1]
                        clearInp()
                        nietGekozen = False
                    except (ValueError, IndexError) as e:
                        print('Dat is geen optie.')
                        nietGekozen = True
        if weggegooidVoorwerp in rugzak:
            rugzak.remove(weggegooidVoorwerp)
            print('Je hebt je ' + weggegooidVoorwerp + ' weggegooid.')
            print('Later kun je het hier altijd nog terugvinden.')
            kaart[locatie]['voorwerpen'].append(weggegooidVoorwerp)
            kaart[locatie]['vinden'].append(random.choice(["Aan de rand van het afval vind je een ", "Je graaft wat in de hoop afval en vindt een ", "Tussen de wortels van een boom vind je een ", "Je loopt een rondje om de hoop afval en vind onderweg een ", "Je steekt je arm eens extra diep de hoop afval in en vindt een "]))
            vertelInhoudRZ()
            nietGekozen2 = True
            while nietGekozen2:
                print()
                print('''Wil je nog een voorwerp weggooien?
1. ja
2. nee
Kies 1 of 2''')
                antwoord = input()
                clearInp()
                if antwoord == '1':
                    nietGekozen2 = False
                    vuilnisbelt.weggooien()
                elif antwoord == '2':
                    nietGekozen2 = False
                else:
                    print('Dat was geen optie.')
                    nietGekozen2 = True
        print()
        actieVragen()

class vuurvlakte: #de functies die horen bij locaties[4]
    def rondkijken():
        print('''Wil je
1. rondzoeken op de vlakte of
2. proberen een vuurtje te starten?
Kies 1 of 2''')
        antwoord = input()
        clearInp()
        if antwoord == '1':
           muisVinden('Dreis')
        elif antwoord == '2':
            vuurvlakte.vuur()
        else:
            print('Dat was geen optie')
            vuurvlakte.rondkijken()

    def vuur():
        #de kans variabelen werken als een soort percentages om te berekenen welke optie er gebeurt. De kansen zijn in principe per aansteker en brandstof verschillend
        #de kansen van de aansteker en brandstof worden bij elkaar opgeteld, de totale kans is dan 100
        global rugzak, muizenGevonden, vuurGemaakt, olifantenVerdreven, schapenGetemd
        if vuurGemaakt:
            print('Je hebt al eens een vuur gemaakt. De vlakte zal niet nog eens in de fik kunnen vliegen.')
            print()
            actieVragen()
        else:
            aanstekers = ['aansteker', 'doosje met lucifers']
            brandstoffen = ['stuk schors', 'bos takken', 'stok', 'boek over wapens', 'stoelpoot', 'veel bladeren']
            mijnAanstekers = [x for x in rugzak if x in aanstekers] #list comprehension
            mijnBrandstoffen = [x for x in rugzak if x in brandstoffen]
            print('Je hebt om een vuur te maken iets nodig dat iets kan aansteken en iets dat als brandstof kan dienen. Pas wel op: het zou ook fout kunnen gaan...')

            nietGekozenA = True
            while nietGekozenA:
                if len(mijnAanstekers) == 0:
                    print('Je hebt geen voorwerp waarmee je iets kan aansteken. Kom terug als je er wel een hebt.')
                    print()
                    nietGekozenA = False
                    actieVragen()
                elif len(mijnAanstekers) == 1:
                    print('Je hebt 1 voorwerp om iets mee aan te steken:')
                    aansteker = mijnAanstekers[0]
                    nietGekozenA = False
                    for a in mijnAanstekers:
                        print(a)
                else:
                    print('Je hebt de volgende voorwerpen om iets mee aan te steken:')
                    for a in mijnAanstekers:
                        print(str(mijnAanstekers.index(a) + 1) + '.', a)
                    print('Kies 1 of 2')
                    print('Welk voorwerp wil je gebruiken als aansteker?')
                    try:
                        aansteker = mijnAanstekers[int(input()) - 1]
                        clearInp()
                        nietGekozenA = False
                    except (ValueError, IndexError) as e:
                        print('Dat is geen optie.')
                        nietGekozenA = True
            if aansteker in mijnAanstekers:
                nietGekozenA = False
                if aansteker == 'aansteker':
                    kansA1, kansA2 = 10, 30
                elif aansteker == 'doosje met lucifers':
                    kansA1, kansA2 = 20, 25
            print()

            nietGekozenB = True
            while nietGekozenB:
                if len(mijnBrandstoffen) == 0:
                    print('Je hebt niets dat als brandstof kan dienen. Kom terug als je er wel een hebt.')
                    print()
                    nietGekozenB = False
                    actieVragen()
                elif len(mijnBrandstoffen) == 1:
                    print('Je hebt het volgende voorwerp dat als brandstof kan dienen:')
                    brandstof = mijnBrandstoffen[0]
                    nietGekozenB = False
                    for b in mijnBrandstoffen:
                        print(b)
                else:
                    print('Je hebt de volgende voorwerpen die als brandstof kunnen dienen:')
                    for b in mijnBrandstoffen:
                        print(str(mijnBrandstoffen.index(b) + 1) + '.', b)
                    print('Kies tussen de getallen 1 t/m', len(mijnBrandstoffen))
                    try:
                        brandstof = mijnBrandstoffen[int(input()) - 1]
                        clearInp()
                        nietGekozenB = False
                    except (ValueError, IndexError) as e:
                        print('Dat is geen optie.')
                        nietGekozenB = True
            if brandstof in mijnBrandstoffen:
                rugzak.remove(brandstof)
                nietGekozenB = False
                if brandstof == 'bos takken':
                    kansB1, kansB2 = 10, 30
                elif brandstof == 'stuk schors' or brandstof == 'stoelpoot':
                    kansB1, kansB2 = 10, 25
                elif brandstof == 'stok':
                    kansB1, kansB2 = 0, 10
                elif brandstof == 'veel bladeren':
                    kansB1, kansB2 = 5, 20
                elif brandstof == 'boek over wapens':
                    kansB1, kansB2 = 15, 25

            print('Je pakt je', aansteker, 'en je', brandstof, 'en probeert een vuur te starten.')
            print()
            uitkomst = random.randint(1,100) #willekeurig getal dat in combinatie met de kansen bepaalt wat er gebeurt
            if uitkomst <= kansA1 + kansB1: #optie 1: het lukt niet
                print('Helaas, het lukt niet! Je', brandstof, '''wil maar geen vlam vatten, maar waait wel weg. Je zucht. Die ben je kwijt.
Probeer het later nog eens met een andere brandstof.''')
            elif uitkomst <= kansA2 + kansB2 + kansA1 + kansB1: #optie 2: het lukt,mmaar de pleegt zelfmoord als hij/zij Dreis nog niet had gevonden
                if schapenGetemd:
                    print('''Het lukt! Het vuur grijpt om zich heen en laait op tot de grootte van een groot kampvuur.
    Je''', aansteker, '''valt helaas ook in het vuur, maar die ga je toch niet meer nodig hebben. Na een tijdje dooft het vuur weer.''')
                elif 'Dreis' in muizenGevonden:
                    print('''Het lukt! Het vuur grijpt om zich heen en laait op tot de grootte van een groot kampvuur.
Je''', aansteker, '''valt helaas in het vuur, maar die ga je toch niet meer nodig hebben.
De rook waait van je weg, een pad op naar links. Niet veel later hoor je trompetgeschal en begint de grond te schudden.

De meeste olifanten zijn doodsbang voor vuur. De rook heeft alle olifanten, behalve hun koningin Earin, weggejaagd uit het paleis.
Na een tijdje dooft het vuur weer.''')
                    olifantenVerdreven = True
                    vuurGemaakt = True
                    rugzak.remove(aansteker)
                else: #optie 3: het loopt uit de hand
                    print('''Het lukt! Het vuur grijpt om zich heen en laait op tot de grootte van een groot kampvuur.
Je''', aansteker, '''valt helaas ook in het vuur, maar die ga je toch niet meer nodig hebben.
Dan hoor je een vreselijk gekrijs. Geschrokken kijk je om je heen.
Het gekrijs is gestopt, maar het ruikt plotseling verdacht veel naar aangebrand vlees...
Huiverend realiseer je je dat er een muis zat op de vlakte, die nu levend is verbrand.
Van wanhoop gooi je jezelf ook in het vuur.''')
                    print()
                    eindSpel('gameOver')
            else: #optie 3: het loopt uit de hand, de speler gaat dood
                if brandstof == 'stok':
                    print('De stok vat vlam, maar de vlammen zijn blauw! Na een paar tellen explodeert de stok en vaagt het hele bos weg.')
                    eindSpel('gameOver')
                print('''Het lukt! Het vuur grijpt gretig om zich heen en laat niks van zijn omgeving over.
Een pyromanische grijns glijdt over je gezicht. Je bent zo afgeleid door je geluk, dat het je te laat opvalt dat het vuur de bosrand heeft bereikt.
In no-time staat het hele bos in de fik. Je hoort verschillende kreten van zowel muizen als olifanten terwijl ze levend worden verbrand.''')
                print()
                eindSpel('gameOver')
            actieVragen()

class meer: #de functies die horen bij locaties[5]
    def rondkijken():
        global muizenGevonden, boekGelezen, rugzak
        if 'Engi' in muizenGevonden:
            print('''Wil je
1. naar de rots midden op het meer zwemmen of
2. het meer induiken?
Kies 1 of 2''')
        else:
            print('''Op een rots in het midden van het meer zit een muis erg luid te jammeren. Wil je
1. naar de muis toezwemmen of
2. het meer induiken?
Kies 1 of 2''')
        antwoord = input()
        clearInp()
        if antwoord == '1':
            meer.Engi()
        elif antwoord == '2':
            if boekGelezen and 'Excalibur' not in rugzak:
                vind()
            else:
                print('Je duikt dieper en dieper, maar vindt niks. Je blijft te lang onder water en verdrinkt.')
                eindSpel('gameOver')
        else:
            print('Dat was geen optie')
            meer.rondkijken()

    def Engi(): #Engi is een soort 'tussenbaas' en begint een gevecht en/of doodt de speler
        global rugzak, muizenGevonden, locatiesBezocht, EngiOmgekocht, boekGelezen
        if 'Engi' in muizenGevonden:
            print('De rots is leeg. Je ziet niks interessants en zwemt weer terug.')
            print()
            actieVragen()
        else:
            print('''Je zwem naar het midden van het meer, terwijl de muis op de rots maar door blijft jammeren.
Zodra je op de rots bent geklommen, stopt ze met huilen en draait zich om.
    "Eindelijk!" piept ze uit, "Eindelijk heb je me gevonden! Ik heb hier zolang gezeten, helemaal alleen..."
Ze kijkt dramatisch uit over het water.

Je hebt Engi gevonden!''')
            muizenGevonden.append("Engi")
            if len(muizenGevonden) == 1:
                print('Je hebt nu', len(muizenGevonden), 'muis gevonden!')
            elif len(muizenGevonden) == 6:
                print('Je hebt alle muizen gevonden!')
            else:
                print('Je hebt nu', len(muizenGevonden), 'muizen gevonden!')
            print()

            print('''Je wil net terugzwemmen naar de oever, als Engi doorgaat met praten:
        "Nu je er toch bent, daar in de verte glinstert iets gouds... Ik denk dat het iets kan zijn dat ons kan helpen de olifanten te verslaan. Zullen we erheen gaan om te kijken wat het is?"
1. ja
2. nee
Kies 1 of 2''')
            nietGekozen = True
            while nietGekozen:
                antwoord = input()
                clearInp()
                if antwoord == '1': #De speler gaat met Engi mee, Engi blijkt een verrader en Earin vermoordt de speler
                    print('''Engi grijnst en stapt opzij. Achter haar blijkt een kleine motorboot te liggen. Ze duwt je erin, springt erbij, en start de motor.

    De wind waait door je haren en je kijkt tevreden uit over het meer.
    Het uitzicht is adembenemend.

    Jullie meren aan bij de oever en Engi pakt je stevig vast. De gouden glinstering is nu enorm geworden, maar je kan niet goed onderscheiden wat het is.
    Je hoopt dat Engi gelijk had en dat het je kan helpen de olifanten te verslaan.

        "Er is nu geen onstnapping meer mogelijk", fluistert Engi in je oor.
    Nog voor je kunt vragen wat ze daarmee bedoelt, duwt ze je verder, met je handen op je rug.

    Ze duwt je weg van het meer en naar het gouden licht toe.
    Nadat jullie langs een paar bomen zijn gestapt, komt het eindelijk duidelijk in beeld. Je hapt naar adem.

    "Welkom bij het Olifantenpaleis," zegt Engi, "De plek waar je zult sterven."''')
                    locatiesBezocht.append('het Olifantenpaleis')
                    print()
                    print('''Je wordt op de rug van een olifant gegooid en vervolgens het paleis binnengedragen.
    De olifant gaat door talloze gangen, totdat hij uiteindelijk stilstaat voor een grote, rijkversierde deur. Langzaam gaat hij open.

    De deur onthult een enorme troonzaal, verlicht door de honderden kaarsen op de kroonluchters.
    Je knijpt je ogen dicht tegen het licht, terwijl de olifant je naar voren draagt.

        "Zo zo, wat hebben we hier?", galmt het door de zaal, gevolgd door een wrede lach.
    Je opent je ogen en ziet een koninklijke olifant zitten op de troon. Het is Earin, de olifantenkoningin.

        "Dankje Engi, je hebt je taak goed volbracht", zegt ze.
    Engi laat een lachje horen.
        "Dank u, koningin", zegt ze, en ze maakt grijzend een buiging.

    Earin glimlacht. Dan richt ze haar blik terug op jou.
        "Gooi haar in de Put van Verloor!"

    De olifant draait een kwartslag en lanceert je een put in, waar je minutenlang valt, totdat je de bodem bereikt.''')
                    clear()
                    eindSpel('gameOver')

                elif antwoord == '2': #de speler gaat niet mee en er begint een gevecht
                    print('''Engi's gezicht vertrekt plotsteling van woede.
        "De muizen hadden allemaal dood moeten zijn! Dan had IK kunnen heersen over het bos. Denk je echt dat de olifanten zelf op het idee waren gekomen om het Muizenhuis aan te vallen?
         HA! Ik was het die ze op het idee bracht! Ik was het die ze naar het huis leidde!
         Maar toen ging het mis: iedereen ontsnapte ongedeerd, waardoor mijn hele plan in duigen viel! En nu breng jij ze ook nog eens bij elkaar!"

    Engi haalt naar je uit. Ze heeft bizar lange nagels. Je deinst achteruit en de nagels raken je net niet.
    Ze staat echter al klaar om opnieuw uit te halen. Wat nu?''')
                    print()

                    nietGekozen2 =True
                    while nietGekozen2:
                        #inventariseer welke wapens de speler tot zijn beschikking heeft:
                        wapens = []
                        if 'nagelschaartje' in rugzak:
                            wapens.append('een nagelschaartje, om Engi\'s nagels proberen te knippen')
                        if ZizaMetToverstok:
                            wapens.append('Ziza met haar toverstok in de aanslag om Engi als het nodig is in bedwang te houden')
                        if 'stapeltje geld' in rugzak:
                            wapens.append('geld: misschien kun je Engi omkopen?')
                        if "paddenstoelen die een walgelijke geur afstoten" in rugzak:
                            wapens.append('paddenstoelen die een walgelijke geur afstoten om Engi op afstand te houden')
                        if 'stoelpoot' in rugzak:
                            wapens.append('een stoelpoot om als een wapen te gebruiken')
                        if 'stinkbom' in rugzak:
                            wapens.append('een stinkbom, waarvan de stank Engi buiten westen zou kunnen brengen')
                        if 'Excalibur' in rugzak:
                            wapens.append('Excalibur, een machtig zwaard waarmee je Engi ernstig zou kunnen verwonden. Misschien wat overdreven, denk je niet?')

                        if len(wapens) == 0:
                            print('''Je graait door je rugzak, maar er is niks wat je zou kunnen gebruiken om Engi te verslaan. Engi pakt je vast en ze gooit je in een motorboot.
Je raakt buiten westen.

Als je weer wakker wordt, zie je nog net een rijkversierde olifant op een troon zitten, met Engi naast haar, voor je een hele diepe put in wordt gegooid.
Je valt, en valt, en valt, totdat je de bodem bereikt.''')
                            clear()
                            nietGekozen2 = False
                            eindSpel('gameOver')
                        elif len(wapens) == 1:
                            print('Je hebt 1 ding waarmee je Engi kunt proberen te verslaan:')
                            for w in wapens:
                                print(w)
                            antwoord = wapens[0]
                        else:
                            print('Je hebt de volgende dingen waarmee je Engi kunt proberen te verslaan:')
                            for w in wapens:
                                print(str(wapens.index(w) + 1) + '.', w)
                            print('Kies tussen de getallen 1 t/m', len(wapens))
                            print()
                            print('Wat wil je gebruiken?')
                            try: #voorkom errors
                                antwoord = wapens[int(input()) - 1]
                                clearInp()
                            except (ValueError, IndexError) as e:
                                print('Dat was geen optie.')
                                nietGekozen2 = True
                        if antwoord == 'een nagelschaartje, om Engi\'s nagels proberen te knippen': #Engi verslaat de speler
                                print('Je krijgt Engi\'s poot te pakken en begint haar nagels te knippen. Maar je vergeet even dat ze nog een andere poot heeft! Ze haalt daarmee uit en slaat je het water in, waar je verdrinkt.')
                                rugzak.remove('nagelschaartje')
                                nietGekozen2 = False
                                eindSpel('gameOver')
                        elif antwoord == 'Ziza met haar toverstok in de aanslag om Engi als het nodig is in bedwang te houden': #De speler verslaat Engi, Engi gaat gedwongen mee
                            print('''Ziza stapt naar voren en zwaait met haar toverstok. Engi schrikt en piept.
    "H-h-hehe, het was maar een grapje!"
Ze laat een ongeloofwaardige glimlach zien. Ziza rolt met haar ogen.
Er verschijnt een touw om Engi's polsen, dat ze vastbindt op haar rug. Engi snuift.
    "Goed dan, ik ga mee op je zielige zoektocht. Maar denk maar niet dat ik het leuk vind!"
    Je glimlacht tevreden. Je merkt opeens een motorboot op, die achter Engi verborgen lag.
Nadat je de motor aan de praat hebt gekregen, varen jullie terug naar de oever.''')
                            nietGekozen2 = False
                        elif antwoord == 'geld: misschien kun je Engi omkopen?': #De speler koopt Engi om, Engi gaat vrijwillig mee en is nu een bondgenoot
                            print('''Je wappert met het geld voor Engi's neus.
    "Kan je hiermee overhalen je weer bij je familie te voegen?"
Engi pakt het geld aan en telt het.
Ze grijnst.
    "Ja, dat is wel genoeg. Dus, zullen we teruggaan met mijn boot?"

Ze stapt opzij en wijst naar een motorboot die bij de rots aangemeerd ligt. Enigszins beduusd vaar je met Engi terug naar de oever.''')
                            nietGekozen2 = False
                            if 'Excalibur' not in rugzak:
                                print('''Eenmaal daar zegt Engi:
        "Heb je Excalibur al opgedoken? Als je de olifantenkoningin wilt verslaan, zul je dat hard nodig hebben."
    Dat klinkt niet eens als een heel slecht plan, moet je toegeven. ''')
                            boekGelezen = True
                            rugzak.remove('stapeltje geld')
                            EngiOmgekocht = True
                        elif antwoord == 'paddenstoelen die een walgelijke geur afstoten om Engi op afstand te houden': #Er gebeurt niks, de speler moet iets anders proberen
                                print('''Je zwaait met de paddenstoelen voor Engi's gezicht.
    "Gadverdamme!" roept ze.
Ze graait de paddenstoelen uit je hand en gooit ze in het water.
    "Is dat echt het beste dat je hebt?", vraagt ze.
Je besluit opnieuw je opties te overwegen, terwijl Engi zich weer klaarmaakt om je aan te vallen.''')
                                print()
                                rugzak.remove('paddenstoelen die een walgelijke geur afstoten')
                                wapens.remove('paddenstoelen die een walgelijke geur afstoten om Engi op afstand te houden')
                                nietGekozen2 = True
                        elif antwoord == 'een stoelpoot om als een wapen te gebruiken': #Er gebeurt niks, de speler moet iets anders proberen
                                print('''Je haalt met de stoelpoot uit naar Engi.
Engi ontwijkt moeiteloos je aanval.
Ze lacht.
Gefrustreerd haal je nog een keer uit. Engi steekt haar poot uit en boort haar nagels in het hout.
Ze trekt de stoelpoot uit je hand en gooit hem in het meer.
    "Is dat echt het beste dat je hebt?", vraagt ze.
Je besluit opnieuw je opties te overwegen, terwijl Engi zich weer klaarmaakt om je aan te vallen.''')
                                print()
                                rugzak.remove('stoelpoot')
                                wapens.remove('een stoelpoot om als een wapen te gebruiken')
                                nietGekozen2 = True
                        elif antwoord == 'een stinkbom, waarvan de stank Engi buiten westen zou kunnen brengen': #De speler verslaat Engi, Engi gaat gedwongen mee
                            print('''Je gooit de stinkbom, en met succes. De stank verspreid zich over de hele rots.
Engi hoest en valt flauw. Je zet een stap om haar vast te pakken, maar de stank is ook jouw luchtwegen binnengedrongen en je valt net als Engi flauw.

Als je wakker wordt, is de stank weg. Engi ligt bewusteloos bij je voeten. Je tilt haar op en bindt haar poten en vast met een stuk touw dat je op de rots vindt.
Je vraagt je net af hoe je met een bewusteloze muis weer terug bij de oever komt, als je een motorboot opmerkt, die aangemeerd is bij de rots. Je stapt erin en scheurt terug naar de oever.''')
                            rugzak.remove('stinkbom')
                            nietGekozen2 = False
                        elif antwoord == 'Excalibur, een machtig zwaard waarmee je Engi ernstig zou kunnen verwonden. Misschien wat overdreven, denk je niet?': #de speler doodt Engi en zichzelf
                            print('''Je haalt Excalibur tevoorschijn, en Engi deinst doodsbang achteruit.
Je haalt uit en hakt haar kop eraf. Dan realiseer je je dat je arm zoveel vaart heeft, dat je het zwaard er niet van kan weerhouden je eigen kop ook af te hakken.
    ''')
                            nietGekozen2 = False
                            eindSpel('gameOver')
                    nietGekozen = False
                    print()
                    actieVragen()
                else:
                    print('''Dat was geen optie. Kies opnieuw: wil je met Engi de gouden glinstering in de verte bekijken?
1. ja
2. nee
Kies ja of nee''')
                    nietGekozen = True

class olifantenpaleis: #de functies die horen bij locaties[8], draait om het gevecht met de 'eindbaas', Earin, en het vinden van Thyen, nadat de speler dit is gelukt, is deze loctie niet meer bereikbaar
    def betreden(): #check of de speler echt naar binnen wilt
        global olifantenVerdreven, schapenEten, EngiOmgekocht, muizenGevonden, locatiesBezocht, locaties, olifantenDoorMuizenDood
        if olifantenVerdreven:
            print('''Nadat je het pad hebt betreden, zie je dat het vol grote pootafdrukken zit.
Dit pad leidt naar het Olifantenpaleis, realiseer je je.
Het vuur dat je had gemaakt, heeft de meeste olifanten weggejaagd. Alleen Earin, de olifantenkoningin is achtergebleven.
Ze is misschien alleen, maar nog steeds heel sterk en moeilijk te verslaan.
Weet je zeker dat je het grondgebied van de olifanten wil betreden? Eenmaal daar kan je niet zomaar terug.
1. ja
2. nee
Kies 1 of 2''')
        elif schapenEten:
            print('''Het pad ligt vol bloed en olifantenresten.
Dit pad leidt naar het Olifantenpaleis, realiseer je je. De schapen hebben alle olifanten behalve Earin, de olifantenkoningin, opgegeten.
Earin is nu misschien alleen, maar nog steeds heel sterk en moeilijk te verslaan.
Weet je zeker dat je het grondgebied van de olifanten wil betreden? Eenmaal daar kan je niet zomaar terug.
1. ja
2. nee
Kies 1 of 2''')
        elif EngiOmgekocht:
            print('''Engi staat plotseling voor je en je botst bijna tegen haar op.
    "Dit is het pad naar het Olifantenpaleis! Je zult het niet overleven als je het via de hoofdingang betreedt, maar ik ken een achteringang. Je moet dan nog wel langs Earin, de olifantenkoningin, maar verder is het veilig"
Je schat in dat, aangezien je Engi hebt omgekocht, ze te vertrouwen is. Je bent wel een beetje nerveus door het vooruitzicht om tegen Earin te moeten vechten: ze is erg sterk en moeilijk te verslaan.
Volg je Engi het paleis in? Eenmaal daar kan je niet zomaar terug.
1. ja
2. nee
Kies 1 of 2''')
        elif olifantenDoorMuizenDood:
            print('''Je herkent het pad naar het Olifantenpaleis. De muizen kijken je verwachtingsvol aan. Je twijfelt, als je het paleis betreedt, zul je het moeten opnemen tegen Earin.
Wil je het Olifantenpaleis betreden? Eenmaal daar kun je niet zomaar terug.
1. ja
2. nee
Kies 1 of 2''')
        elif len(muizenGevonden) == 5 and not DreisGesproken:
            print('''   "Dit leidt naar het Olifantenpaleis!" zegt Maas.
    "Ze hebben Thyen!" zegt Tuen.
Voor je iets kan zeggen, rennen Tuen, Maas, Dreis en Ziza weg.
    "Wacht hier!" roept Dreis nog, voor ze uit het zicht verdwijnen.

Even later komen ze terug.
    "We hebben alle olifaten verjaagd! Ze renden zo het moeras in. Dus, waar wachten we op? Alleen Earin, de olifantenkoningin, is er nog. Maar die kun jij wel aan, toch?", zegt Ziza.
Je kijkt haar stomverbaasd aan. Je had nooit gedacht dat vier muizen een heleboel olifanten zouden kunnen verslaan.
Ze kijken je allemaal verwachtingsvol aan. Je twijfelt. Earin is misschien alleen, maar wel heel sterk en moeilijk te verslaan.
Wil je het Olifantenpaleis betreden? Eenmaal daar kan je niet zomaar terug.
1. ja
2. nee
Kies 1 of 2''')
            olifantenDoorMuizenDood = True
        else:
            print('''Je loopt het pad op, aangetrokken door de gouden gloed. Dan wordt de gouden gloed door een olifant geblokkeerd. Geschrokken duik je in de bosjes.
Het goud dat je zag was de muur van het Olifantenpaleis! Weet je zeker dat je het grondgebied van de olifanten wil betreden? Het is er erg gevaarlijk, en eenmaal daar kan je niet zomaar terug.
1. ja
2. nee
Kies 1 of 2.''')
        nietGekozen = True
        while nietGekozen:
            antwoord = input()
            clearInp()
            if antwoord == '1':
                locatiesBezocht.append(locaties[8])
                if olifantenVerdreven:
                    print('''Je loopt het pad op naar het Olifantenpaleis.
Het paleis is helemaal gemaakt van massief goud. Eromheen hangt allemaal rook. Er is geen olifant te bekennnen.
Je loopt naar de grote dubbele deuren, die wijd open staan.
Ook binnen zijn er geen olifanten. Je vraagt je af waar Earin is. Lang hoef je je dat niet af te vragen: binnen de kortste keren hoor je een luide strijdkreet. Er komt een olifant de hoek om, gekleed in koninklijke gewaden.
In paniek realiseer je je dat dit Earin is, en dat ze op het punt staat je aan te vallen.''')
                elif schapenEten:
                    print('''Je loopt het pad op naar het Olifantenpaleis.
Het paleis zelf is helemaal gemaakt van massief goud. Het gazon ervoor ligt vol met olifanten lijken en bloed. Het ruikt verschrikkelijk.
Je rent het paleis in, op de vlucht voor die lugubere beelden.
Je vraagt je af waar Earin is. Lang hoef je je dat niet af te vragen: binnen de kortste keren hoor je een luide strijdkreet. Er komt een olifant de hoek om, gekleed in koninklijke gewaden.
In paniek realiseer je je dat dit Earin is, en dat ze op het punt staat je aan te vallen.''')
                elif EngiOmgekocht:
                    print('''Engi leidt je naar een luik, verborgen in de struiken. Ze trekt het met luid gekreun open. En springt erin.
    "Kom je nog?", vraagt ze. Je hoopt maar dat je niet in de val loopt en gaat haar achterna.

Jullie lopen door een vieze, donkere tunnel. Het plafond is zo laag dat je gebogen moet lopen.
Het enige geluid is afkomstig van jullie voetstappen en Engi, die hardop aan het tellen is.
    "... negenveertig...vijftig!"
Opeens blijft Engi stilstaan.
    "Hier is het!"
Ze strekt haar poot uit omhoog. Eerst lijkt er niet te gebeuren, maar dat opent er een luik boven je. Engi trekt zich omhoog uit het gat en daarna helpt ze jou ook eruit te komen.
    "Welkom in het Olifantenpaleis", zegt ze.
Dan klinkt er een luide strijdkreet.
    "En maak kennis met de koningin: Earin"
Er komt een olifant de hoek om, gekleed in koninklijke gewaden.
In paniek realiseer je je dat dit Earin is, en dat ze op het punt staat je aan te vallen.''')
                elif olifantenDoorMuizenDood:
                    print('''Je loopt samen met de muizen het pad op naar het Olifantenpaleis.
Het paleis is helemaal gemaakt van massief goud. Ervoor is een groot gazon. Er is geen olifant te bekennnen.
Jullie lopen naar de grote dubbele deuren, die de vijf muizen (Engi onder dwang) samen open duwen.

Ook binnen zijn er geen olifanten. Je vraagt je af waar Earin is. Lang hoef je je dat niet af te vragen: binnen de kortste keren hoor je een luide strijdkreet. Er komt een olifant de hoek om, gekleed in koninklijke gewaden.
In paniek realiseer je je dat dit Earin is, en dat ze op het punt staat je aan te vallen.''')
                else:
                    print('Vol vertrouwen loop je het pad uit. Je ziet nog net het gouden paleis, voor een olifant je platstampt.')
                    eindSpel('gameOver')
                print()
                nietGekozen = False
                olifantenpaleis.Earin()
            elif antwoord == '2':
                print("De dreiging van de olifanten is je te veel en je gaat terug naar " + locatie + ".")
                nietGekozen = False
                print()
                vertelLocatie()
            else:
                print('''Dat was geen optie. Kies opnieuw: wil je het Olifantenpaleis betreden?
1. ja
2. nee
Kies 1 of 2.''')
                nietGekozen = True

    def Earin(): #het gevecht met de 'eindbaas'
        global rugzak, locatie, EarinVerslagen, muizenGevonden, EngiOmgekocht, locatiesBezocht, locaties
        locatiesBezocht.append(locaties[8])
        #inventariseer welke wapens de speler tot zijn beschikking heeft:
        wapens = []
        if 'Excalibur' in rugzak:
            wapens.append('Excalibur, een machtig zwaard waarmee je Earin kunt doden')
        if 'stinkbom' in rugzak:
            wapens.append('een stinkbom, waarmee je Earin buiten westen kunt proberen te brengen.')
        if "paddenstoelen die een walgelijke geur afstoten" in rugzak:
            wapens.append('paddenstoelen die een walgelijke geur afstoten om Earin op afstand te houden')
        if 'stoelpoot' in rugzak:
            wapens.append('een stoelpoot om als een wapen te gebruiken')

        nietGekozen =True
        while nietGekozen:
            if len(wapens) == 0:
                print('''Je graait door je rugzak, maar er is niks wat je zou kunnen gebruiken om Earin te verslaan. Het is een hopeloze zaak. Earin stormt op je af loopt zo over je heen.''')
                nietGekozen = False
                eindSpel('gameOver')
            elif len(wapens) == 1:
                print('Je hebt 1 ding waarmee je Earin kunt proberen te verslaan:')
                for w in wapens:
                    print(w)
            else:
                print('Je hebt de volgende dingen waarmee je Earin kunt proberen te verslaan:')
                for w in wapens:
                    print(str(wapens.index(w) + 1) + '.', w)
                print('Kies tussen de getallen 1 t/m', len(wapens))
                print()
                print('Wat wil je gebruiken?')
                try:
                    antwoord = wapens[int(input()) - 1]
                    clearInp()
                except (ValueError, IndexError) as e:
                    print('Dat was geen optie.')
                    nietGekozen = True
            #elk wapen heeft een andere gebeurtenis tot gevolg:
            if antwoord == 'Excalibur, een machtig zwaard waarmee je Earin kunt doden': #de speler doodt Earin en wint
                print('Earin stromt op je af en je houdt Excalibur recht voor je uit. Het zwaard doorboort Earin, die dood op de grond valt.')
                EarinVerslagen = True
                nietGekozen = False
            elif antwoord == 'een stinkbom, waarmee je Earin buiten westen kunt proberen te brengen.': #Earin doodt de speler
                print('Je gooit de stinkbom, maar zij gooit hem terug, recht in je gezicht. De stank is zo overweldigend, dat je hart het begeeft.')
                nietGekozen = False
                eindSpel('gameOver')
            elif antwoord == 'paddenstoelen die een walgelijke geur afstoten om Earin op afstand te houden': #de speler moet iets anders probere
                print('Je houdt de paddenstoelen voor je. Earin steekt haar slurf uit en pakt de paddenstoelen uit je hand en eet ze op. Wat nu?')
                wapens.remove('paddenstoelen die een walgelijke geur afstoten om Earin op afstand te houden')
                rugzak.remove('paddenstoelen die een walgelijke geur afstoten')
                nietGekozen = True
            elif antwoord == 'een stoelpoot om als een wapen te gebruiken': #de speler moet iets anders proberen
                print('Earin omklemt met haar slurf de stoelpoot en trekt hem uit je hand. Ze gooit hem buiten je bereik. Wat nu?')
                wapens.remove('een stoelpoot om als een wapen te gebruiken')
                rugzak.remove('stoelpoot')
                nietGekozen = True

        print('''Je juicht. Earin is verslagen! Je probeert Excalibur weer uit haar lijk te trekken, maar het zit vast.
Dan hoor je een gepiep.
    "Ik zit hier! Hallo?"
Je rent naar het geluid toe. Het is Thyen!

Hij zit in een grote, gouden kooi. Thyen kijkt je opgelucht aan.
    "Je hebt me gevonden! Vlug, maak de kooi open! Heb je een sleutel?"

Dan begint het paleis te rommelen. Het staat op instorten!
Je pakt de kooi en rent  snel terug naar''', locatie)

        print('Eenmaal daar zet je de kooi neer en je zoekt in je rugzak naar een sleutel.')
        if 'verroeste sleutel' in rugzak: #je hebt de sleutel nodig om Thyen te bevrijden/vinden
            nietGekozen = True
            while nietGekozen:
                print('''Je hebt een verroeste sleutel! Wil je proberen hiermee de kooi te openen?
1. ja
2. nee
Kies 1 of 2''')
                antwoord = input()
                clearInp()
                if antwoord == '1':
                    nietGekozen = False
                    rugzak.remove('verroeste sleutel')
                    muisVinden('Thyen')
                elif antwoord == '2':
                    print('Je zegt tegen Thyen dat je geen sleutel hebt, maar je belooft hem dat je zijn kooi mee zal nemen op je zoektocht, zodat je de kooi open kunt maken als je dat wilt.')
                    nietGekozen = False
                else:
                    print('Dat was geen optie.')
                    nietGekozen = True
        else:
            print('Je zegt tegen Thyen dat je geen sleutel hebt, maar je belooft hem dat je zijn kooi mee zal nemen op je zoektocht, zodat je de kooi open kunt maken als je dat wilt.')

        #speciaal stukje voor Engi's verhaallijn:
        if 'Engi' in muizenGevonden and not EngiOmgekocht:
            print('''
Engi laat een glimlach zien waarvan je je afvraagt of die echt gemeend is, en ze zegt:
    "Het spijt me dat ik me zo... impulsief heb gedragen, maar... alles is vergeven?"
Je haalt je schouders op.
    "Dat mag Gran Famka bepalen", zeg je.
Engi draait zich chagrijnig weer om.''')
        print()

        print('Het olifantenpaleis is nu niet meer een bezoekbare locatie. Het gebied is onbegaanbaar.')
        clear()
        vertelLocatie()

reset()
