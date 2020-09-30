#happybirthday.py
#Rodas T Gebreslassie
#This program asks the user to input there name,
#and show a bouncing ball sing-along to 'Happy Birthday"
from graphics import *
import time
def main():
    win = GraphWin("song", 600,600)
    win.setCoords(0,0,400,400)
    win.setBackground("light green")

    #creat GUI and get input
    entryLine = Text(Point(150,250),"Please enter your name:")
    entryLine.setFill("white")
    entryLine.setStyle("bold")
    entryLine.draw(win)

    input = Entry(Point(300,250), 8)
    input.setFill("white")
    input.draw(win)

    enter = Text(Point(200,150), "Enter")
    enter.setFill("white")
    enter.setStyle("bold")
    enter.draw(win)

    enterCirc = Circle(Point(200,150),40)
    enterCirc.setOutline("white")
    enterCirc.setWidth(5)
    enterCirc.draw(win)

    #undraw after mouse click
    win.getMouse()
    entryLine.undraw()
    input.undraw()
    enter.undraw()
    enterCirc.undraw()

    circ = Circle(Point(43, 280), 10)
    circ.setFill("white")
    circ.draw(win)

    line = Text(Point(200,200),"Happy Birthday to You")
    line.setFill("white")
    line.setStyle("bold")
    line.setSize(36)
    line.draw(win)


    for i in range(2):
        for i in range(20):
            circ.move(1, -3)
            time.sleep(0.015)
        for i in range(20):
            circ.move(1,3)
            time.sleep(0.015)

    for i in range(20):
        circ.move(2,-3)
        time.sleep(0.015)
    for i in range(20):
        circ.move(1.7,3)
        time.sleep(0.015)
    for i in range(20):
        circ.move(2.1,-3)
        time.sleep(0.015)

    for i in range(20):
        circ.move(1.4,3)
        time.sleep(0.015)
    for i in range(20):
        circ.move(1.4,-3)
        time.sleep(0.015)
    for i in range(20):
        circ.move(1.7,3)
        time.sleep(0.015)

    for i in range(20):
        circ.move(1.2,-3)
        time.sleep(0.015)
    for i in range(20):
        circ.move(1.1,3)
        time.sleep(0.015)


    line.undraw()
    circ.undraw()



    line2 = Text(Point(200,200),"Happy Birthday to You")
    line2.setFill("white")
    line2.setStyle("bold")
    line2.setSize(36)
    line2.draw(win)


    circ2 = Circle(Point(43,280),10)
    circ2.setFill("white")
    circ2.draw(win)





    for i in range(2):
        for i in range(20):
            circ2.move(1,-3)
            time.sleep(0.015)
        for i in range(20):
            circ2.move(1, 3)
            time.sleep(0.015)

    for i in range(20):
        circ2.move(2, -3)
        time.sleep(0.015)
    for i in range(20):
        circ2.move(1.7, 3)
        time.sleep(0.015)
    for i in range(20):
        circ2.move(2.1,-3)
        time.sleep(0.015)

    for i in range(20):
        circ2.move(1.4, 3)
        time.sleep(0.015)
    for i in range(20):
        circ2.move(1.4,-3)
        time.sleep(0.015)
    for i in range(20):
        circ2.move(1.7, 3)
        time.sleep(0.015)

    for i in range(20):
        circ2.move(1.2, -3)
        time.sleep(0.015)
    for i in range(20):
        circ2.move(1.1, 3)
        time.sleep(0.015)


    line2.undraw()
    circ2.undraw()


    a = Text(Point(200,200), "Happy Birthday")
    a.setFill("white")
    a.setSize(36)
    a.setStyle("bold")
    a.draw(win)

    circ4 = Circle(Point(83,280),10)
    circ4.setFill("white")
    circ4.draw(win)


    for i in range(2):
        for i in range(20):
            circ4.move(1.5,-3)
            time.sleep(0.015)
        for i in range(20):
            circ4.move(1.3, 3)
            time.sleep(0.015)

    for i in range(20):
        circ4.move(1.5, -3)
        time.sleep(0.015)
    for i in range(20):
        circ4.move(1.5, 3)
        time.sleep(0.015)
    for i in range(20):
        circ4.move(1.5, -3)
        time.sleep(0.015)




    a.undraw()
    circ4.undraw()


    b = Text(Point(200,200), "Happy Birthday")
    b.setSize(36)
    b.setFill("white")
    b.setStyle("bold")
    b.draw(win)

    circ5 = Circle(Point(83,280), 10)
    circ5.setFill("white")
    circ5.draw(win)


    for i in range(2):
        for i in range(20):
            circ5.move(1.5, -3)
            time.sleep(0.015)
        for i in range(20):
            circ5.move(1.3, 3)
            time.sleep(0.015)

    for i in range(20):
        circ5.move(1.5, -3)
        time.sleep(0.015)
    for i in range(20):
        circ5.move(1.5, 3)
        time.sleep(0.015)
    for i in range(20):
        circ5.move(1.5, -3)
        time.sleep(0.015)



    circ5.undraw()
    b.undraw()



    inputName = input.getText()
    line3 = Text(Point(150,200),"Happy Birthday Dear")
    line3.setStyle("bold")
    line3.setFill("white")
    line3.setSize(27)
    line3.draw(win)

    line4 = Text(Point(335, 200), " "+inputName)
    line4.setFill("white")
    line4.setSize(27)
    line4.setStyle("bold")
    line4.draw(win)

    line5 = Text(Point(200,50),"click to continue")


    circ3 = Circle(Point(43,280),10)
    circ3.setFill("white")
    circ3.draw(win)


    for i in range(2):
        for i in range(20):
            circ3.move(0.7, -3)
            time.sleep(0.015)
        for i in range(20):
            circ3.move(0.7, 3)
            time.sleep(0.015)

    for i in range(20):
        circ3.move(1.5,-3)
        time.sleep(0.015)
    for i in range(20):
        circ3.move(1, 3)
        time.sleep(0.015)
    for i in range(20):
        circ3.move(1.5,-3)
        time.sleep(0.015)

    for i in range(20):
        circ3.move(2, 3)
        time.sleep(0.015)
    for i in range(20):
        circ3.move(1.9,-3)
        time.sleep(0.015)
    for i in range(20):
        circ3.move(1, 3)
        time.sleep(0.015)

    for i in range(20):
        circ3.move(1.2,-3)
        time.sleep(0.015)
    for i in range(20):
        circ3.move(1.2, 3)
        time.sleep(0.015)
    line5.draw(win)
    for i in range(20):
        circ3.move(1.3,-3)
        time.sleep(0.015)
    for i in range(20):
        circ3.move(1.3,3)
        time.sleep(0.015)

    win.getMouse()
    line3.undraw()
    line4.undraw()
    line5.undraw()
    circ3.undraw()

    rect5 = Rectangle(Point(100, 80), Point(300, 180))
    rect5.setFill("light cyan")
    rect5.draw(win)

    rect1 = Rectangle(Point(100, 80), Point(300, 110))
    rect1.setOutline("light cyan")
    rect1.setFill("light cyan")
    rect1.draw(win)

    oval1 = Oval(Point(100, 50), Point(300, 110))
    oval1.setFill("pink4")
    oval1.draw(win)

    oval2 = Oval(Point(100, 60), Point(300, 120))
    oval2.setFill("light cyan")
    oval2.draw(win)

    rect2 = Rectangle(Point(100, 90), Point(300, 130))
    rect2.setFill("light cyan")
    rect2.setOutline("light cyan")
    rect2.draw(win)

    line1 = Line(Point(100, 80), Point(100, 180))
    line1.draw(win)

    line2 = Line(Point(300, 80), Point(300, 180))
    line2.draw(win)

    oval3 = Oval(Point(100, 150), Point(300, 210))
    oval3.setFill("pink4")
    oval3.draw(win)

    oval4 = Oval(Point(105, 155), Point(295, 205))
    oval4.setFill("light pink")
    oval4.draw(win)

    c1 = Polygon(Point(130, 180), Point(130, 225), Point(135, 235), Point(140, 225), Point(140, 180))
    c1.setFill("yellow")
    c1.draw(win)

    c2 = Polygon(Point(170, 170), Point(170, 215), Point(175, 225), Point(180, 215), Point(180, 170))
    c2.setFill("yellow")
    c2.draw(win)

    c3 = Polygon(Point(210, 180), Point(210, 225), Point(215, 235), Point(220, 225), Point(220, 180))
    c3.setFill("yellow")
    c3.draw(win)

    c4 = Polygon(Point(250, 170), Point(250, 215), Point(255, 225), Point(260, 215), Point(260, 170))
    c4.setFill("yellow")
    c4.draw(win)

    line = Text(Point(200, 300), "Happy Birthday")
    line.setFill("light cyan")
    line.setSize(36)
    line.setStyle("bold")
    line.draw(win)

    l4 = Text(Point(200,10),"Click to quit")
    l4.draw(win)

    #wait for click and then quit
    win.getMouse()
    win.close()
main()