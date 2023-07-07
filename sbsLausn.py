# munum ap importa random
import random

# setjum mögulega valkost í lista og síðan í breyta ["skæri", "blað", "steinn"]
valkostir = ["skæri", "blað", "steinn"]

# núll stillum score fyrir tölvu og leikmann ef við viljum hafa score
tolvu_score = 0
leikmadur_score = 0

# bjóða leikmanninum velkomin í skæri, blað, steinn
print("Velkomin í Skæri, Blað, Steinn leikinn minn")
# segja leikmanninum valkostina
print("Notaðu (sk)æri, (bl)að eða (st)einn og ýtu á enter til að velja")

# byrjum while True lykkjuna okkar sem mun halda utan um leikinn okkar
while True:
    # notum while True lykkju til að halda áfram að spyrja notandann þangað til að hann gefur rétt svar
    while True:
        # notum input skipun til að spyrja leikmann um val
        leikmadur = input("Þitt val: ",)
        # athugum hvort valið hjá leikmanni sé skæri, blað eða steinn
        if leikmadur not in valkostir and leikmadur not in ["sk", "bl", "st"]:
            # prentum leiðbeiningu um að nota bara skæri, blað eða steinn
            print("Notaðu bara (sk)æri, (bl)að eða (st)einn")
            continue
        # notum else setningu til að hætta í lykkjunni ef notandinn gaf rétt svar
        else:
            #break
            break
    # notum random.choice() eða random.randint() til að láta tölvuna ákveða hvaða svar hún gefur
    tolva = random.choice(valkostir)
    # segjum notandanum að tölvan hafi valið
    print("Tölvan valdi: " + tolva)
    
    # ef leikmadurinn velur það sama og tölvan þá er jafntefli
    if leikmadur in tolva:
        # látum notandan vita af jafnteflinu
        print("Það var jafntefli")
    # notum elif til að athuga hvort leikmadur hafi giskað á skæri með valkostir[0]
    elif leikmadur in valkostir[0]:
        # látum leikmann vita um valið sitt
        print("Þú valdir... Skæri!")
        # notum if til að athuga hvort leikmadur hafi giskað á blað með valkostir[1]
        if tolva == valkostir[1]:
            # hækkum score hjá leikmanni ef við viljum nota score
            leikmadur_score = leikmadur_score + 1
            # prentum að leikmadur hafi unnið og segjum score ef við viljum nota það með str()
            print("Þú vannst og ert með: " + str(leikmadur_score) + "stig")
        # notum elif til að athuga hvort leikmadur hafi giskað á stein með valkostir[2]
        elif tolva == valkostir[2]:
            # hækkum score hjá tölvu ef við viljum nota score
            tolvu_score = tolvu_score + 1
            # prentum að tölva hafi unnið og segjum score ef við viljum nota það með str()
            print("Þú tapaðir, tölvan er með: " + str(tolvu_score) + "stig")
    # gerum þetta þrisvar sinnum með t.d. copy (Ctrl + c) og paste (Ctrl + v) og skiptum um tölurnar
    # tölur fyrir blað leikmadur 1 if tölva 2: leikmadur vinna, elif tölva 0: leikmadur tapa
    elif leikmadur in valkostir[1]:
        print("Þú valdir... Blað!")
        if tolva == valkostir[2]:
            leikmadur_score = leikmadur_score + 1
            print("Þú vannst og ert með: " + str(leikmadur_score) + "stig")
        elif tolva == valkostir[0]:
            tolvu_score = tolvu_score + 1
            print("Þú tapaðir, tölvan er með: " + str(tolvu_score) + "stig")
    # tölur fyrir stein leikmadur 2 if tölva 0: leikmadur vinna, elif tölva 1: leikmadur tapa
    elif leikmadur in valkostir[2]:
        print("Þú valdir... Stein!")
        if tolva == valkostir[0]:
            leikmadur_score = leikmadur_score + 1
            print("Þú vannst og ert með: " + str(leikmadur_score) + "stig")
        elif tolva == valkostir[1]:
            tolvu_score = tolvu_score + 1
            print("Þú tapaðir, tölvan er með: " + str(tolvu_score) + "stig")
    # spyrjum hvort leikmadur vilji spila aftur með input
    svar = input("Viltu halda áfram? (j) eða (n) ")
    if svar == "n":
        break