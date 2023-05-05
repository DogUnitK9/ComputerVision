import PIL.Image, PIL.ImageOps, PIL.ImageFilter
import zipfile
import numpy
import cv2
def main():
    while(1):
        card = input("Specify a card (format: R#.png) or type Exit :")
        if card == "Exit":
            return
        cards = zipfile.ZipFile('rcards.zip', 'r')
        imagedata = cards.open(card)
        cnts = findContours(imagedata)
        ranks = computeShapes(cnts)
        suits = computeSuits(cnts)
        print(ranks, "of", suits)
    
def findContours(file):
    img = PIL.Image.open(file)
    img = numpy.asarray(img)
    A = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _,B = cv2.threshold( src=A, thresh=0, maxval=255,
        type=(cv2.THRESH_BINARY | cv2.THRESH_OTSU) )
    #E = cv2.Canny(B, 100, 25, 3)

    cnts,hierarchy = cv2.findContours(B, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    return cnts
    #cv2.drawContours(img, cnts, -1, (0,0,255), 3)
    #cv2.imshow('ContoursOri', img)

def defineContours(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _,thresh2 = cv2.threshold(gray, 0, 255, type=(cv2.THRESH_BINARY | cv2.THRESH_OTSU))
    cnts2,hierarchy = cv2.findContours(thresh2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(img, cnts2[0], -1, (0,0,255), 3)
    #cv2.imshow("card", img)
    return cnts2[0]
def defineContours2(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _,thresh2 = cv2.threshold(gray, 0, 255, type=(cv2.THRESH_BINARY | cv2.THRESH_OTSU))
    cnts2,hierarchy = cv2.findContours(thresh2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(img, cnts2[1], -1, (0,0,255), 3)
    #cv2.imshow("card", img)
    return cnts2[1]
def defineContours3(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _,thresh2 = cv2.threshold(gray, 0, 255, type=(cv2.THRESH_BINARY | cv2.THRESH_OTSU))
    cnts2,hierarchy = cv2.findContours(thresh2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(img, cnts2[2], -1, (0,0,255), 3)
    #cv2.imshow("card", img)
    return cnts2[2]
def computeShapes(cnts):
    num2 = cv2.imread('2.png')
    num3 = cv2.imread('3.png')
    num4 = cv2.imread('4.png')
    num5 = cv2.imread('5.png')
    num6 = cv2.imread('6.png')
    num7 = cv2.imread('7.png')
    num8 = cv2.imread('8.png')
    num9 = cv2.imread('9.png')
    num10 = cv2.imread('10.png')
    club = cv2.imread('club.png')
    diamond = cv2.imread('diamond.png')
    heart = cv2.imread('heart.png')
    spade = cv2.imread('spade.png')
    cnt2 = defineContours(num2)
    cnt3 = defineContours(num3)
    cnt4 = defineContours2(num4)
    cnt5 = defineContours(num5)
    cnt6 = defineContours2(num6)
    cnt7 = defineContours(num7)
    cnt8 = defineContours3(num8)
    cnt9 = defineContours2(num9)
    cnt10 = defineContours(num10)
    cntC = defineContours(club)
    cntD = defineContours(diamond)
    cntH = defineContours(heart)
    cntS = defineContours(spade)

    value = {}
    distList = []
    for cnt in cnts:
        dist = cv2.matchShapes(cnt, cnt2, 1, 0)
        distList.append(dist)   
    value["2"] = (min(distList))

    distList = []               
    for cnt in cnts:
        dist = cv2.matchShapes(cnt, cnt3, 1, 0)
        distList.append(dist)
    value["3"] = (min(distList))

    distList = []               
    for cnt in cnts:
        dist = cv2.matchShapes(cnt, cnt4, 1, 0)
        distList.append(dist)
    value["4"] = (min(distList))

    distList = []               
    for cnt in cnts:
        dist = cv2.matchShapes(cnt, cnt5, 1, 0)
        distList.append(dist)
    value["5"] = (min(distList))

    distList = []               
    for cnt in cnts:
        dist = cv2.matchShapes(cnt, cnt6, 1, 0)
        distList.append(dist)
    value["6"] = (min(distList))

    distList = []               
    for cnt in cnts:
        dist = cv2.matchShapes(cnt, cnt7, 1, 0)
        distList.append(dist)
    value["7"] = (min(distList))

    distList = []               
    for cnt in cnts:
        dist = cv2.matchShapes(cnt, cnt8, 1, 0)
        distList.append(dist)
    value["8"] = (min(distList))

    distList = []               
    for cnt in cnts:
        dist = cv2.matchShapes(cnt, cnt9, 1, 0)
        distList.append(dist)
    value["9"] = (min(distList))

    distList = []               
    for cnt in cnts:
        dist = cv2.matchShapes(cnt, cnt10, 1, 0)
        distList.append(dist)
    value["10"] = (min(distList))

    rank = min(value, key=value.get)
    if rank == "6" or rank == "9":
        if len(cnts) == 26:
            rank = "6"
        if len(cnts) > 26:
            rank = "9"
    return rank

def computeSuits(cnts):
    club = cv2.imread('club.png')
    diamond = cv2.imread('diamond.png')
    heart = cv2.imread('heart.png')
    spade = cv2.imread('spade.png')
    
    cntC = defineContours(club)
    cntD = defineContours(diamond)
    cntH = defineContours(heart)
    cntS = defineContours(spade)

    value = {}
    distList = []
    for cnt in cnts:
        dist = cv2.matchShapes(cnt, cntC, 1, 0)
        distList.append(dist)   
    value["Clubs"] = (min(distList))

    distList = []               
    for cnt in cnts:
        dist = cv2.matchShapes(cnt, cntD, 1, 0)
        distList.append(dist)
    value["Diamonds"] = (min(distList))

    distList = []               
    for cnt in cnts:
        dist = cv2.matchShapes(cnt, cntH, 1, 0)
        distList.append(dist)
    value["Hearts"] = (min(distList))

    distList = []               
    for cnt in cnts:
        dist = cv2.matchShapes(cnt, cntS, 1, 0)
        distList.append(dist)
    value["Spades"] = (min(distList))
    return min(value, key=value.get)

main()
