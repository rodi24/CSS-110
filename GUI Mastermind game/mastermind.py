#mastermind.py
#Rodas T Gebreslassie
#This program allows the user to play the game Mastermind against the computer.


import time
from graphics import *
from random import *
def drawBoard(win,gl,sl):
    circ = Circle(Point(50, 40), 25)
    circ.setFill("red")
    circ.draw(win)

    l = Text(Point(50, 40), "R")
    l.draw(win)


    x = 78.57
    colors = ["red", "Green", "Yellow", "purple", "Orange", "Cyan"]
    labels = ["R", "G", "Y", "P", "O", "C"]

    for i in range(1, 6):
        circ2 = circ.clone()
        circ2.move(x, 0)
        circ2.setFill(colors[i])
        circ2.draw(win)
        l2 = l.clone()
        l2.setText(labels[i])
        l2.move(x, 0)
        l2.draw(win)
        x = x + 78.57

    line1 = Line(Point(0, 100), Point(520, 100))
    line1.draw(win)

    label = Text(Point(150, 80), "Choose from this Colors")
    label.setFill("blue")
    label.draw(win)

    c = Circle(Point(50, 137.5), 25)
    c.setFill(gl[0])
    c.draw(win)

    x = 78.57
    a = 1

    # first player raw
    for i in range(3):
        c2 = c.clone()
        c2.setFill(gl[a])
        c2.move(x, 0)
        c2.draw(win)
        time.sleep(0.08)
        x = x + 78.57
        a = a + 1
    # first Raw samall
    xs = 30
    time.sleep(0.5)
    cs = Circle(Point(360.25, 137.5), 10)
    cs.setFill(sl[0])
    cs.draw(win)
    b = 1

    for i in range(3):
        cs2 = cs.clone()
        cs2.move(xs, 0)
        cs2.setFill(sl[b])
        cs2.draw(win)
        xs = xs + 30
        b = b + 1

    # second player raw
    c3 = Circle(Point(50, 212.5), 25)
    c3.draw(win)
    x = 78.5
    for i in range(3):
        c4 = c3.clone()
        c4.move(x, 0)
        c4.draw(win)
        x = x + 78.5
        a = a + 1
    # second raw small
    xs = 30
    cs = Circle(Point(360.25, 212.5), 10)
    cs.draw(win)

    for i in range(3):
        cs2 = cs.clone()
        cs2.move(xs, 0)
        cs2.draw(win)
        xs = xs + 30

    # third player raw
    c5 = Circle(Point(50, 287.5), 25)
    c5.draw(win)
    x = 78.57
    for i in range(3):
        c6 = c5.clone()
        c6.move(x, 0)
        c6.draw(win)
        x = x + 78.57
    # third raw small
    xs = 30
    cs = Circle(Point(360.25, 287.5), 10)
    cs.draw(win)

    for i in range(3):
        cs2 = cs.clone()
        cs2.move(xs, 0)
        cs2.draw(win)
        xs = xs + 30

    # 4th player raw
    c7 = Circle(Point(50, 362.5), 25)
    c7.draw(win)
    x = 78.57
    for i in range(3):
        c8 = c7.clone()
        c8.move(x, 0)
        c8.draw(win)
        x = x + 78.57
    # 4th raw small
    xs = 30
    cs = Circle(Point(360.25, 362.5), 10)
    cs.draw(win)

    for i in range(3):
        cs2 = cs.clone()
        cs2.move(xs, 0)
        cs2.draw(win)
        xs = xs + 30

    # 5th player raw
    c9 = Circle(Point(50, 437.5), 25)
    c9.draw(win)
    x = 78.57
    for i in range(3):
        c10 = c9.clone()
        c10.move(x, 0)
        c10.draw(win)
        x = x + 78.57
    # 5th raw small
    xs = 30
    cs = Circle(Point(360.25, 437.5), 10)
    cs.draw(win)

    for i in range(3):
        cs2 = cs.clone()
        cs2.move(xs, 0)
        cs2.draw(win)
        xs = xs + 30

    # 6th player raw
    c11 = Circle(Point(50, 512.5), 25)
    c11.draw(win)
    x = 78.57
    for i in range(3):
        c12 = c11.clone()
        c12.move(x, 0)
        c12.draw(win)
        x = x + 78.57
    # 6th raw small
    xs = 30
    cs = Circle(Point(360.25, 512.5), 10)
    cs.draw(win)

    for i in range(3):
        cs2 = cs.clone()
        cs2.move(xs, 0)
        cs2.draw(win)
        xs = xs + 30

    # 7th player raw
    c13 = Circle(Point(50, 587.5), 25)
    c13.draw(win)
    x = 78.57
    for i in range(3):
        c14 = c13.clone()
        c14.move(x, 0)
        c14.draw(win)
        x = x + 78.57
    # 7th raw samll
    xs = 30
    cs = Circle(Point(360.25, 587.5), 10)
    cs.draw(win)

    for i in range(3):
        cs2 = cs.clone()
        cs2.move(xs, 0)
        cs2.draw(win)
        xs = xs + 30

    # 8th player raw
    c15 = Circle(Point(50, 662.5), 25)
    c15.draw(win)
    x = 78.57
    for i in range(3):
        c16 = c15.clone()
        c16.move(x, 0)
        c16.draw(win)
        x = x + 78.57
    # 8th raw small
    xs = 30
    cs = Circle(Point(360.25, 662.5), 10)
    cs.draw(win)

    for i in range(3):
        cs2 = cs.clone()
        cs2.move(xs, 0)
        cs2.draw(win)
        xs = xs + 30



def drawGuess(win):
    circ = Circle(Point(50, 40), 25)
    circ.setFill("red")
    circ.draw(win)


    l = Text(Point(50, 40), "R")
    l.draw(win)

    x = 78.57
    colors = ["red", "Green", "Yellow", "purple", "Orange", "Cyan"]
    labels = ["R", "G", "Y", "P", "O", "C"]

    for i in range(1, 6):
        circ2 = circ.clone()
        circ2.move(x, 0)
        circ2.setFill(colors[i])
        circ2.draw(win)
        l2 = l.clone()
        l2.setText(labels[i])
        l2.move(x, 0)
        l2.draw(win)
        x = x + 78.57

    line1 = Line(Point(0, 100), Point(520, 100))
    line1.draw(win)

    label = Text(Point(150, 80), "Choose from this Colors")
    label.setFill("blue")
    label.draw(win)

    c = Circle(Point(50, 137.5), 25)
    #c.setFill(gl[0])
    c.draw(win)

    x = 78.57
    a = 1

    # first player raw
    for i in range(3):
        c2 = c.clone()
        #c2.setFill(gl[a])
        c2.move(x, 0)
        c2.draw(win)
        x = x + 78.57
        a = a + 1
    # first Raw samall
    xs = 30
    cs = Circle(Point(360.25, 137.5),10)
    cs.draw(win)

    for i in range(3):
        cs2 = cs.clone()
        cs2.move(xs, 0)
        cs2.draw(win)
        xs = xs + 30

    # second player raw
    c3 = Circle(Point(50, 212.5), 25)
    c3.draw(win)
    x = 78.5
    for i in range(3):
        c4 = c3.clone()
        c4.move(x, 0)
        c4.draw(win)
        x = x + 78.5
    # second raw small
    xs = 30
    cs = Circle(Point(360.25, 212.5), 10)
    cs.draw(win)

    for i in range(3):
        cs2 = cs.clone()
        cs2.move(xs, 0)
        cs2.draw(win)
        xs = xs + 30

    # third player raw
    c5 = Circle(Point(50, 287.5), 25)
    c5.draw(win)
    x = 78.57
    for i in range(3):
        c6 = c5.clone()
        c6.move(x, 0)
        c6.draw(win)
        x = x + 78.57
    # third raw small
    xs = 30
    cs = Circle(Point(360.25, 287.5), 10)
    cs.draw(win)

    for i in range(3):
        cs2 = cs.clone()
        cs2.move(xs, 0)
        cs2.draw(win)
        xs = xs + 30

    # 4th player raw
    c7 = Circle(Point(50, 362.5), 25)
    c7.draw(win)
    x = 78.57
    for i in range(3):
        c8 = c7.clone()
        c8.move(x, 0)
        c8.draw(win)
        x = x + 78.57
    # 4th raw small
    xs = 30
    cs = Circle(Point(360.25, 362.5), 10)
    cs.draw(win)

    for i in range(3):
        cs2 = cs.clone()
        cs2.move(xs, 0)
        cs2.draw(win)
        xs = xs + 30

    # 5th player raw
    c9 = Circle(Point(50, 437.5), 25)
    c9.draw(win)
    x = 78.57
    for i in range(3):
        c10 = c9.clone()
        c10.move(x, 0)
        c10.draw(win)
        x = x + 78.57
    # 5th raw small
    xs = 30
    cs = Circle(Point(360.25, 437.5), 10)
    cs.draw(win)

    for i in range(3):
        cs2 = cs.clone()
        cs2.move(xs, 0)
        cs2.draw(win)
        xs = xs + 30

    # 6th player raw
    c11 = Circle(Point(50, 512.5), 25)
    c11.draw(win)
    x = 78.57
    for i in range(3):
        c12 = c11.clone()
        c12.move(x, 0)
        c12.draw(win)
        x = x + 78.57
    # 6th raw small
    xs = 30
    cs = Circle(Point(360.25, 512.5), 10)
    cs.draw(win)

    for i in range(3):
        cs2 = cs.clone()
        cs2.move(xs, 0)
        cs2.draw(win)
        xs = xs + 30

    # 7th player raw
    c13 = Circle(Point(50, 587.5), 25)
    c13.draw(win)
    x = 78.57
    for i in range(3):
        c14 = c13.clone()
        c14.move(x, 0)
        c14.draw(win)
        x = x + 78.57
    # 7th raw samll
    xs = 30
    cs = Circle(Point(360.25, 587.5), 10)
    cs.draw(win)

    for i in range(3):
        cs2 = cs.clone()
        cs2.move(xs, 0)
        cs2.draw(win)
        xs = xs + 30

    # 8th player raw
    c15 = Circle(Point(50, 662.5), 25)
    c15.draw(win)
    x = 78.57
    for i in range(3):
        c16 = c15.clone()
        c16.move(x, 0)
        c16.draw(win)
        x = x + 78.57
    # 8th raw small
    xs = 30
    cs = Circle(Point(360.25, 662.5), 10)
    cs.draw(win)

    for i in range(3):
        cs2 = cs.clone()
        cs2.move(xs, 0)
        cs2.draw(win)
        xs = xs + 30

    input = Entry(Point(350, 80), 7)
    input.setFill("light blue")
    input.draw(win)

    rect = Rectangle(Point(390,73),Point(450,87))
    rect.setFill("light blue")
    rect.draw(win)

    text = Text(Point(420, 80), "Check")
    text.setStyle("bold")
    text.setSize(11)
    text.setFill("Blue")
    text.draw(win)

    win.getMouse()


    value = input.getText()
    guess = value.upper()
    input.setText("")
    return guess





def guessList(guess):
    guessList = []
    for i in guess:
        if i == "R":
            guessList.append("Red")
        elif i == "G":
            guessList.append("Green")
        elif i == "Y":
            guessList.append("Yellow")
        elif i == "P":
            guessList.append("Purple")
        elif i == "O":
            guessList.append("Orange")
        elif i == "C":
            guessList.append("Cyan")
    return (guessList)

def generateSecret():
    colors = ["R","G","Y","P","O","C"]
    secret = []
    for i in range(4):
        secret.append(colors[randrange(0,5)])

    return secret

def evaluate(secret,guess):
    exact = 0
    find = 0
    tempList = []
    gList = []
    for i in range(4):
        tempList.append(secret[i])
        gList.append(guess[i])
    for i in range(len(secret)):

        if guess[i] == secret[i]:
            exact = exact + 1
            tempList[i] = "L"
            gList[i] = "k"

    for i in range(len(secret)):
        for j in range(4):
            if gList[j] == tempList[i]:
                find = find + 1
                tempList[i] = "l"
    return (exact, find)


def smallCircle(e,f):
    val = 4 - (e + f)
    list = []
    for i in range(e):
        list.append("black")
    for i in range(f):
        list.append("white")
    for i in range(val):
        list.append("light cyan")

    return list

def drawBoard2(win, gl2, sl2):
    # second player raw

    c3 = Circle(Point(50, 212.5), 25)
    c3.setFill(gl2[0])
    c3.draw(win)
    x = 78.5
    a = 1
    for i in range(3):
        c4 = c3.clone()
        c4.move(x, 0)
        c4.setFill(gl2[a])
        c4.draw(win)
        time.sleep(0.08)
        x = x + 78.5
        a = a + 1
    # second raw small
    time.sleep(0.5)
    xs = 30
    cs = Circle(Point(360.25, 212.5), 10)
    cs.setFill(sl2[0])
    cs.draw(win)
    b = 1

    for i in range(3):
        cs2 = cs.clone()
        cs2.move(xs, 0)
        cs2.setFill(sl2[b])
        cs2.draw(win)
        xs = xs + 30
        b = b + 1



def drawBoard3(win,gl3,sl3):


    # third player raw
    c5 = Circle(Point(50, 287.5), 25)
    c5.setFill(gl3[0])
    c5.draw(win)
    x = 78.57
    a = 1
    for i in range(3):
        c6 = c5.clone()
        c6.move(x, 0)
        c6.setFill(gl3[a])
        c6.draw(win)
        x = x + 78.57
        a = a + 1
        time.sleep(0.08)
    # third raw small
    time.sleep(0.5)
    xs = 30
    cs = Circle(Point(360.25, 287.5), 10)
    cs.setFill(sl3[0])
    cs.draw(win)
    b = 1

    for i in range(3):
        cs2 = cs.clone()
        cs2.move(xs, 0)
        cs2.setFill(sl3[b])
        cs2.draw(win)
        xs = xs + 30
        b = b + 1



def drawBoard4(win,gl4,sl4):

    # 4th player raw
    c7 = Circle(Point(50, 362.5), 25)
    c7.setFill(gl4[0])
    c7.draw(win)
    x = 78.57
    a = 1
    for i in range(3):
        c8 = c7.clone()
        c8.move(x, 0)
        c8.setFill(gl4[a])
        c8.draw(win)
        x = x + 78.57
        a = a + 1
        time.sleep(0.08)
    # 4th raw small
    time.sleep(0.5)
    xs = 30
    cs = Circle(Point(360.25, 362.5), 10)
    cs.setFill(sl4[0])
    cs.draw(win)
    b = 1

    for i in range(3):
        cs2 = cs.clone()
        cs2.move(xs, 0)
        cs2.setFill(sl4[b])
        cs2.draw(win)
        xs = xs + 30
        b = b + 1

def drawBoard5(win,gl5,sl5):

    # 5th player raw
    c9 = Circle(Point(50, 437.5), 25)
    c9.setFill(gl5[0])
    c9.draw(win)
    x = 78.57
    a = 1
    for i in range(3):
        c10 = c9.clone()
        c10.move(x, 0)
        c10.setFill(gl5[a])
        c10.draw(win)
        x = x + 78.57
        a = a + 1
        time.sleep(0.08)
    # 5th raw small
    time.sleep(0.5)
    xs = 30
    cs = Circle(Point(360.25, 437.5), 10)
    cs.setFill(sl5[0])
    cs.draw(win)
    b = 1

    for i in range(3):
        cs2 = cs.clone()
        cs2.move(xs, 0)
        cs2.setFill(sl5[b])
        cs2.draw(win)
        xs = xs + 30
        b = b + 1



def drawBoard6(win,gl6,sl6):

    # 6th player raw
    c11 = Circle(Point(50, 512.5), 25)
    c11.setFill(gl6[0])
    c11.draw(win)
    x = 78.57
    a = 1
    for i in range(3):
        c12 = c11.clone()
        c12.move(x, 0)
        c12.setFill(gl6[a])
        c12.draw(win)
        x = x + 78.57
        a = a + 1
        time.sleep(0.08)
    # 6th raw small
    time.sleep(0.5)
    xs = 30
    cs = Circle(Point(360.25, 512.5), 10)
    cs.setFill(sl6[0])
    cs.draw(win)
    b = 1

    for i in range(3):
        cs2 = cs.clone()
        cs2.move(xs, 0)
        cs2.setFill(sl6[b])
        cs2.draw(win)
        xs = xs + 30
        b = b + 1


def drawBoard7(win,gl7,sl7):

    # 7th player raw
    c13 = Circle(Point(50, 587.5), 25)
    c13.setFill(gl7[0])
    c13.draw(win)
    x = 78.57
    a = 1
    for i in range(3):
        c14 = c13.clone()
        c14.move(x, 0)
        c14.setFill(gl7[a])
        c14.draw(win)
        x = x + 78.57
        a = a + 1
        time.sleep(0.08)
    # 7th raw samll
    time.sleep(0.5)
    xs = 30
    cs = Circle(Point(360.25, 587.5), 10)
    cs.setFill(sl7[0])
    cs.draw(win)
    b = 1

    for i in range(3):
        cs2 = cs.clone()
        cs2.move(xs, 0)
        cs2.setFill(sl7[b])
        cs2.draw(win)
        xs = xs + 30
        b = b + 1

def drawBoard8(win,gl8,sl8):

    # 8th player raw
    c15 = Circle(Point(50, 662.5), 25)
    c15.setFill(gl8[0])
    c15.draw(win)
    x = 78.57
    a = 1
    for i in range(3):
        c16 = c15.clone()
        c16.move(x, 0)
        c16.setFill(gl8[a])
        c16.draw(win)
        x = x + 78.57
        a = a + 1
        time.sleep(0.08)
    # 8th raw small
    time.sleep(0.5)
    xs = 30
    cs = Circle(Point(360.25, 662.5), 10)
    cs.setFill(sl8[0])
    cs.draw(win)
    b = 1

    for i in range(3):
        cs2 = cs.clone()
        cs2.move(xs, 0)
        cs2.setFill(sl8[b])
        cs2.draw(win)
        xs = xs + 30
        b = b + 1
    time.sleep(0.4)


def winBoard(win,e):
    if e == 4:
        time.sleep(0.8)
        win.delete("all")

        star1 = Polygon(Point(100,450),Point(130,470),Point(160,450),Point(130,510))
        star1.setFill("Yellow")
        star1.setOutline("yellow")
        star1.draw(win)

        star2 = Polygon(Point(130,470),Point(100,490),Point(160,490))
        star2.setFill("Yellow")
        star2.setOutline("yellow")
        star2.draw(win)

        star3 = star1.clone()
        star3.move(120,30)
        star3.draw(win)

        star4 = star2.clone()
        star4.move(120,30)
        star4.draw(win)

        star5 = star3.clone()
        star5.move(120, -30)
        star5.draw(win)

        star6 = star4.clone()
        star6.move(120, -30)
        star6.draw(win)



        label = Text(Point(250,400),"You Win")
        label.setSize(36)
        label.setStyle("bold")
        label.setFill("Red4")
        label.draw(win)

        circ1 = Circle(Point(80, 220), 20)
        circ1.setFill("light blue")
        circ1.setOutline("light blue")
        circ1.draw(win)

        target = Rectangle(Point(80,200),Point(180,240))
        target.setOutline("light blue")
        target.setFill("light blue")
        target.draw(win)

        circ2 = Circle(Point(180,220),20)
        circ2.setFill("light blue")
        circ2.setOutline("light blue")
        circ2.draw(win)


        target2 = Rectangle(Point(320,200),Point(420,240))
        target2.setOutline("light blue")
        target2.setFill("light blue")
        target2.draw(win)

        circ3 = Circle(Point(320,220),20)
        circ3.setFill("light blue")
        circ3.setOutline("light blue")
        circ3.draw(win)

        circ4 = Circle(Point(420,220),20)
        circ4.setFill("light blue")
        circ4.setOutline("light blue")
        circ4.draw(win)

        text = Text(Point(130,220),"Play again")
        text.setFill("red4")
        text.setSize(15)
        text.setStyle("bold")
        text.draw(win)

        text2 = Text(Point(370,220),"Exit")
        text2.setFill("red4")
        text2.setSize(15)
        text2.setStyle("bold")
        text2.draw(win)

        click = win.getMouse()
        win.delete("all")
        x = click.getX()
        y = click.getY()

        if 60 < x < 200 and 180 < y < 260:

            win.delete("all")

            win.setBackground("light cyan")
            s = generateSecret()
            g = drawGuess(win)
            e, f = evaluate(s, g)
            gl = guessList(g)
            sl = smallCircle(e, f)

            drawBoard(win, gl, sl)
            winBoard(win, e)

            g2 = drawGuess(win)
            gl2 = guessList(g2)
            e, f = evaluate(s, g2)
            sl2 = smallCircle(e, f)

            drawBoard2(win, gl2, sl2)
            winBoard(win, e)

            g3 = drawGuess(win)
            gl3 = guessList(g3)
            e, f = evaluate(s, g3)
            sl3 = smallCircle(e, f)

            drawBoard3(win, gl3, sl3)
            winBoard(win, e)

            g4 = drawGuess(win)
            gl4 = guessList(g4)
            e, f = evaluate(s, g4)
            sl4 = smallCircle(e, f)

            drawBoard4(win, gl4, sl4)
            winBoard(win, e)

            g5 = drawGuess(win)
            gl5 = guessList(g5)
            e, f = evaluate(s, g5)
            sl5 = smallCircle(e, f)

            drawBoard5(win, gl5, sl5)
            winBoard(win, e)

            g6 = drawGuess(win)
            gl6 = guessList(g6)
            e, f = evaluate(s, g6)
            sl6 = smallCircle(e, f)

            drawBoard6(win, gl6, sl6)
            winBoard(win, e)

            g7 = drawGuess(win)
            gl7 = guessList(g7)
            e, f = evaluate(s, g7)
            sl7 = smallCircle(e, f)

            drawBoard7(win, gl7, sl7)
            winBoard(win, e)

            g8 = drawGuess(win)
            gl8 = guessList(g8)
            e, f = evaluate(s, g8)
            sl8 = smallCircle(e, f)

            drawBoard8(win, gl8, sl8)
            winBoard(win, e)
        elif 300  < x < 440 and 180 < y < 260:
            win.close()
        else:
            win.close()


def startBoard(win):
    l = Text(Point(70, 450), "M")
    l.setFill("black")
    l.setSize(36)
    l.setFace("courier")
    l.setStyle("bold")
    l.draw(win)

    a = Text(Point(110, 450), "A")
    a.setFill("red4")
    a.setSize(36)
    a.setFace("courier")
    a.setStyle("bold")
    a.draw(win)

    s = Text(Point(150, 450), "S")
    s.setFill("black")
    s.setSize(36)
    s.setFace("courier")
    s.setStyle("bold")
    s.draw(win)

    t = Text(Point(190, 450), "T")
    t.setSize(36)
    t.setFill("red4")
    t.setFace("courier")
    t.setStyle("bold")
    t.draw(win)

    e = Text(Point(230, 450), "E")
    e.setSize(36)
    e.setFace("courier")
    e.setStyle("bold")
    e.draw(win)

    r = Text(Point(270, 450), "R")
    r.setSize(36)
    r.setFill("red4")
    r.setFace("courier")
    r.setStyle("bold")
    r.draw(win)

    c = Text(Point(310, 450), "M")
    c.setSize(36)
    c.setFace("courier")
    c.setStyle("bold")
    c.draw(win)

    p = Text(Point(350, 450), "I")
    p.setSize(36)
    p.setFill("red4")
    p.setFace("courier")
    p.setStyle("bold")
    p.draw(win)

    n = Text(Point(390, 450), "N")
    n.setSize(36)
    n.setFace("courier")
    n.setStyle("bold")
    n.draw(win)

    z = Text(Point(430, 450), "D")
    z.setSize(36)
    z.setFill("red4")
    z.setFace("courier")
    z.setStyle("bold")
    z.draw(win)

    line = Line(Point(0, 490), Point(520, 490))
    line.setWidth(5)
    line.draw(win)

    line3 = Line(Point(0, 499), Point(520, 499))
    line3.setWidth(4)
    line3.draw(win)

    line4 = Line(Point(0, 510), Point(520, 510))
    line4.setWidth(3)
    line4.draw(win)

    line5 = Line(Point(0, 521), Point(520, 521))
    line5.setWidth(2)
    line5.draw(win)

    line6 = Line(Point(0, 531), Point(520, 531))
    line6.setWidth(1)
    line6.draw(win)

    line2 = Line(Point(0, 420), Point(520, 420))
    line2.setWidth(5)
    line2.draw(win)

    line7 = Line(Point(0, 411), Point(520, 411))
    line7.setWidth(4)
    line7.draw(win)

    line8 = Line(Point(0, 401), Point(520, 401))
    line8.setWidth(3)
    line8.draw(win)

    line9 = Line(Point(0, 390), Point(520, 390))
    line9.setWidth(2)
    line9.draw(win)

    line10 = Line(Point(0, 380), Point(520, 380))
    line10.setWidth(1)
    line10.draw(win)

    label = Text(Point(250, 250), "Play")
    label.setFace("courier")
    label.setStyle("bold")
    label.setFill("red4")
    label.setSize(20)
    label.draw(win)

    ball = Circle(Point(250, 250), 50)
    ball.setOutline("red4")
    ball.setWidth(5)
    ball.draw(win)

    i = "Red4"

    line.setFill(i)
    line2.setFill(i)
    line3.setFill(i)
    line4.setFill(i)
    line5.setFill(i)
    line6.setFill(i)
    line7.setFill(i)
    line8.setFill(i)
    line9.setFill(i)
    line10.setFill(i)
    time.sleep(0.25)

    win.getMouse()
    win.delete("all")

def gameOver(win):
    win.delete("all")
    label = Text(Point(250, 400), "Game Over")
    label.setSize(36)
    label.setStyle("bold")
    label.setFill("Red4")
    label.draw(win)

    circ1 = Circle(Point(80, 220), 20)
    circ1.setFill("light blue")
    circ1.setOutline("light blue")
    circ1.draw(win)

    target = Rectangle(Point(80, 200), Point(180, 240))
    target.setOutline("light blue")
    target.setFill("light blue")
    target.draw(win)

    circ2 = Circle(Point(180, 220), 20)
    circ2.setFill("light blue")
    circ2.setOutline("light blue")
    circ2.draw(win)

    target2 = Rectangle(Point(320, 200), Point(420, 240))
    target2.setOutline("light blue")
    target2.setFill("light blue")
    target2.draw(win)

    circ3 = Circle(Point(320, 220), 20)
    circ3.setFill("light blue")
    circ3.setOutline("light blue")
    circ3.draw(win)

    circ4 = Circle(Point(420, 220), 20)
    circ4.setFill("light blue")
    circ4.setOutline("light blue")
    circ4.draw(win)

    text = Text(Point(130, 220), "Play again")
    text.setFill("red4")
    text.setSize(15)
    text.setStyle("bold")
    text.draw(win)

    text2 = Text(Point(370, 220), "Exit")
    text2.setFill("red4")
    text2.setSize(15)
    text2.setStyle("bold")
    text2.draw(win)

    click = win.getMouse()
    win.delete("all")
    x = click.getX()
    y = click.getY()

    if 60 < x < 200 and 180 < y < 260:

        win.delete("all")

        win.setBackground("light cyan")
        s = generateSecret()
        g = drawGuess(win)
        e, f = evaluate(s, g)
        gl = guessList(g)
        sl = smallCircle(e, f)

        drawBoard(win, gl, sl)
        winBoard(win, e)

        g2 = drawGuess(win)
        gl2 = guessList(g2)
        e, f = evaluate(s, g2)
        sl2 = smallCircle(e, f)

        drawBoard2(win, gl2, sl2)
        winBoard(win, e)

        g3 = drawGuess(win)
        gl3 = guessList(g3)
        e, f = evaluate(s, g3)
        sl3 = smallCircle(e, f)

        drawBoard3(win, gl3, sl3)
        winBoard(win, e)

        g4 = drawGuess(win)
        gl4 = guessList(g4)
        e, f = evaluate(s, g4)
        sl4 = smallCircle(e, f)

        drawBoard4(win, gl4, sl4)
        winBoard(win, e)

        g5 = drawGuess(win)
        gl5 = guessList(g5)
        e, f = evaluate(s, g5)
        sl5 = smallCircle(e, f)

        drawBoard5(win, gl5, sl5)
        winBoard(win, e)

        g6 = drawGuess(win)
        gl6 = guessList(g6)
        e, f = evaluate(s, g6)
        sl6 = smallCircle(e, f)

        drawBoard6(win, gl6, sl6)
        winBoard(win, e)

        g7 = drawGuess(win)
        gl7 = guessList(g7)
        e, f = evaluate(s, g7)
        sl7 = smallCircle(e, f)

        drawBoard7(win, gl7, sl7)
        winBoard(win, e)

        g8 = drawGuess(win)
        gl8 = guessList(g8)
        e, f = evaluate(s, g8)
        sl8 = smallCircle(e, f)

        drawBoard8(win, gl8, sl8)
        winBoard(win, e)
    elif 300 < x < 440 and 180 < y < 260:
        win.close()
    else:
        win.close()







def main():
    win = GraphWin("game", 500, 700)
    win.setCoords(0, 0, 500, 700)
    win.setBackground("light cyan")

    startBoard(win)

    s = generateSecret()
    g = drawGuess(win)
    e,f = evaluate(s,g)
    gl = guessList(g)
    sl = smallCircle(e,f)

    drawBoard(win, gl, sl)
    winBoard(win, e)

    g2 = drawGuess(win)
    gl2 = guessList(g2)
    e,f = evaluate(s,g2)
    sl2 = smallCircle(e,f)

    drawBoard2(win,gl2,sl2)
    winBoard(win,e)

    g3 = drawGuess(win)
    gl3 = guessList(g3)
    e,f = evaluate(s,g3)
    sl3 = smallCircle(e,f)

    drawBoard3(win, gl3, sl3)
    winBoard(win, e)

    g4 = drawGuess(win)
    gl4 = guessList(g4)
    e,f = evaluate(s,g4)
    sl4 = smallCircle(e,f)

    drawBoard4(win,gl4,sl4)
    winBoard(win, e)

    g5 = drawGuess(win)
    gl5 = guessList(g5)
    e,f = evaluate(s,g5)
    sl5 = smallCircle(e,f)

    drawBoard5(win,gl5,sl5)
    winBoard(win, e)

    g6 = drawGuess(win)
    gl6 = guessList(g6)
    e,f = evaluate(s,g6)
    sl6 = smallCircle(e,f)

    drawBoard6(win,gl6,sl6)
    winBoard(win, e)

    g7 = drawGuess(win)
    gl7 = guessList(g7)
    e,f = evaluate(s,g7)
    sl7 = smallCircle(e,f)

    drawBoard7(win,gl7,sl7)
    winBoard(win, e)

    g8 = drawGuess(win)
    gl8 = guessList(g8)
    e,f = evaluate(s,g8)
    sl8 = smallCircle(e,f)

    drawBoard8(win,gl8,sl8)
    winBoard(win, e)

    gameOver(win)
main()
