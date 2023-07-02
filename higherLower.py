# munum að importa random
import random
# búum til nýja lykkju sem leyfir notandanum að byrja aftur
while True:
    # tölvan býr til random tölu
    tala = random.randint(1, 100)
    # segjum notandanum smá frá leiknum
    print("Tölvan er búin að búa til tölu á bilinu 1 til 100")
    # búum til nýja lykkju sem keyrir þangað til að notandinn giskar á rétta tölu
    while True:
        # búum til nýja lykkju til að láta notandan giska þangað til að
        # giskið er bæði tala og á bilinu 1 til 100
        while True:
            # biðjum notandan um að giska á töluna
            gisk = input("reyndu nú bara að giska á hana ")
            # ef talan er ekki númer þá byrjar lykkjan upp á nýtt og við spyrjum aftur
            if gisk.isdigit() != True:
                print("þú mátt bara nota tölur")
                # þurfum ekki continue því að ef lykkjan klárast þá byrjar hún bara upp á nýtt
            # ef talan er ekki á bilinu 1 til 100 þá byrjar lykkjan upp á nýtt og við spyrjum aftur
            elif int(gisk) not in range(1, 101):
                print("þú mátt bara nota tölur á bilinu 1 - 100")
                # þurfum ekki continue því að ef lykkjan klárast þá byrjar hún bara upp á nýtt
            else:
                # ef talan er á réttu bili þá stoppum við lykkjuna
                break
        # athugum hvort talan sé hærri, lægri eða jöfn giskinu
        if tala > int(gisk):
            print("Talan hjá tölvunni er hærri en " + gisk)
            # þurfum ekki continue því að ef lykkjan klárast þá byrjar hún bara upp á nýtt
        elif tala < int(gisk):
            print("Talan hjá tölvunni er lægri en " + gisk)
            # þurfum ekki continue því að ef lykkjan klárast þá byrjar hún bara upp á nýtt
        else:
            print("Þú náðir töluni: " + gisk + " rétt")
            break
    # spyrjum notandann hvort notandinn vilju spila aftur
    svar = input("Viltu spila aftur? (j)")
    if svar not in ["j", "já", "ja", "yes", "y"]:
        # hættum ef svarið er ekki eitt af svörunum í listanum
        break