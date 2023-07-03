# búum til hjálpar fall til að passa að notandinn svari rétt
def input_tolur_eða_takn(bidja_um_tolur):
    # athugum hvort við eigm að biðja um tölur eða tákn
    if bidja_um_tolur:
        # höldum endaluast áfram að spyrja þangað til við fáum tölu
        while True:
            svar = input("hvaða tölu viltu setja í reiknivélina? ")
            if svar.isdigit() != True:
                print("Þú mátt bara nota tölur hérna")
            else:
                return svar
    else:
        # höldum endaluast áfram að spyrja þangað til við fáum tákn
        while True:
            svar = input("hvaða tákn viltu setja á milla talnana")
            if svar not in ["+", "-", "*", "/"]:
                print("þú mátt bara nota eitt af þessum táknum, +, -, *, /")
            else:
                return svar

# biðjum notandan velkomin að nota reiknivélina okkar og segjum frá stöfunum sem má nota
print("Þú hefur fundið reiknivélina mína, settu inn tvö númer og eitthvað stærðfræðitákn á milli þeirra")

# notum fallið okkar til að spyrja notandann
tala1 = input_tolur_eða_takn(bidja_um_tolur = True)
tala2 = input_tolur_eða_takn(bidja_um_tolur = True)
takn = input_tolur_eða_takn(bidja_um_tolur = False)

#athugum hvaða tákn notandinn skrifaði og reiknum út útkomuna fyrir það tákn
if takn == "+":
    utkoma = int(tala1) + int(tala2)
    print("Útkoman er: " + str(utkoma))
elif takn == "-":
    utkoma = int(tala1) - int(tala2)
    print("Útkoman er: " + str(utkoma))
elif takn == "*":
    utkoma = int(tala1) * int(tala2)
    print("Útkoman er: " + str(utkoma))
elif takn == "/":
    utkoma = int(tala1) / int(tala2)
    print("Útkoman er: " + str(utkoma))