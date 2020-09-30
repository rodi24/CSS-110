#milestokm.py
#Rodas T Gebreslassie
#This program uses GUI to get distance in miles from
#the user, and convert it to kilometers.

from graphics import *
def main():
    win = GraphWin("mile to km", 400,400)
    win.setCoords(0,0,400,400)
    win.setBackground("light blue")

    #creat GUI and get input
    line1 = Text(Point(100,300), "Distance in Miles:")
    line1.setStyle("bold")
    line1.draw(win)

    line2 = Text(Point(120,100), "Distance in Kilometers:")
    line2.setStyle("bold")
    line2.draw(win)

    input = Entry(Point(300,300), 5)
    input.setFill("white")
    input.setText("0.0")
    input.draw(win)

    rect = Rectangle(Point(270, 90), Point(320, 110))
    rect.setFill("white")
    rect.setOutline("grey")
    rect.draw(win)

    l1 = Line(Point(0,200), Point(150,200))
    l1.setWidth(5)
    l1.setFill("white")
    l1.draw(win)

    l2 = Line(Point(250,200), Point(410,200))
    l2.setWidth(5)
    l2.setFill("white")
    l2.draw(win)

    output = Text(Point(290,100),"")
    output.draw(win)

    button = Text(Point(200,200),"Convert")
    button.setStyle("bold")
    button.draw(win)

    circ = Circle(Point(200,200), 50)
    circ.setWidth(5)
    circ.setOutline("white")
    circ.draw(win)

    win.getMouse()

    #convert input
    mile = eval(input.getText())
    km = 1.6093 * mile
    output.setText(round(km,2))
    button.setText("Click to Quit")

    #wait for click and then quit
    win.getMouse()
    win.close()
main()
