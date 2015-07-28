import turtle


def turtle_calc():
    print("1: Addition | 2: Subtraction | 3: Multiplication | 4: Division")
    sel = input("Pick one: ")
    num1 = input("First Number: ")
    num2 = input("Second Number: ")
    answer = 0
    if sel == "1":
        answer = (int(num1) + int(num2))
    elif sel == "2":
        answer = (int(num1) - int(num2))
    elif sel == "3":
        answer = (int(num1) * int(num2))
    elif sel == "4":
        answer = (int(num1) // int(num2))
        print("Our turtle does not do remainders")
    wn = turtle.Screen()
    tess = turtle.Turtle()
    tess.shape("turtle")
    tess.color("blue")
    tess.pensize(5)
    tess.penup()
    tess.goto(-190, 0)

    def draw0():
        tess.pendown()
        tess.forward(50)
        tess.left(90)
        tess.forward(100)
        tess.left(90)
        tess.forward(50)
        tess.left(90)
        tess.forward(100)
        tess.penup()
        tess.left(90)
        tess.forward(75)

    def draw1():
        tess.pendown()
        tess.left(90)
        tess.forward(100)
        tess.penup()
        tess.right(180)
        tess.forward(100)
        tess.left(90)
        tess.forward(25)

    def draw2():
        tess.pendown()
        tess.forward(50)
        tess.right(180)
        tess.forward(50)
        tess.right(90)
        tess.forward(50)
        tess.right(90)
        tess.forward(50)
        tess.left(90)
        tess.forward(50)
        tess.left(90)
        tess.forward(50)
        tess.penup()
        tess.left(90)
        tess.forward(100)
        tess.left(90)
        tess.forward(75)

    def draw3():
        tess.pendown()
        tess.forward(50)
        tess.left(90)
        tess.forward(50)
        tess.left(90)
        tess.forward(50)
        tess.left(180)
        tess.forward(50)
        tess.left(90)
        tess.forward(50)
        tess.left(90)
        tess.forward(50)
        tess.penup()
        tess.left(90)
        tess.forward(100)
        tess.left(90)
        tess.forward(75)

    def draw4():
        tess.forward(50)
        tess.pendown()
        tess.left(90)
        tess.forward(100)
        tess.left(180)
        tess.forward(50)
        tess.right(90)
        tess.forward(50)
        tess.right(90)
        tess.forward(50)
        tess.penup()
        tess.left(180)
        tess.forward(100)
        tess.left(90)
        tess.forward(75)

    def draw5():
        tess.pendown()
        tess.forward(50)
        tess.left(90)
        tess.forward(50)
        tess.left(90)
        tess.forward(50)
        tess.right(90)
        tess.forward(50)
        tess.right(90)
        tess.forward(50)
        tess.penup()
        tess.right(90)
        tess.forward(100)
        tess.left(90)
        tess.forward(25)

    def draw6():
        tess.pendown()
        tess.forward(50)
        tess.left(90)
        tess.forward(50)
        tess.left(90)
        tess.forward(50)
        tess.left(90)
        tess.forward(50)
        tess.left(180)
        tess.forward(100)
        tess.right(90)
        tess.forward(50)
        tess.penup()
        tess.right(90)
        tess.forward(100)
        tess.left(90)
        tess.forward(25)

    def draw7():
        tess.forward(50)
        tess.pendown()
        tess.left(90)
        tess.forward(100)
        tess.left(90)
        tess.forward(50)
        tess.penup()
        tess.left(90)
        tess.forward(100)
        tess.left(90)
        tess.forward(75)

    def draw8():
        tess.pendown()
        tess.forward(50)
        tess.left(90)
        tess.forward(50)
        tess.left(90)
        tess.forward(50)
        tess.left(180)
        tess.forward(50)
        tess.left(90)
        tess.forward(50)
        tess.left(90)
        tess.forward(50)
        tess.left(90)
        tess.forward(100)
        tess.penup()
        tess.left(90)
        tess.forward(75)

    def draw9():
        tess.pendown()
        tess.forward(50)
        tess.left(90)
        tess.forward(50)
        tess.left(90)
        tess.forward(50)
        tess.left(180)
        tess.forward(50)
        tess.left(90)
        tess.forward(50)
        tess.left(90)
        tess.forward(50)
        tess.left(90)
        tess.forward(50)
        tess.penup()
        tess.forward(50)
        tess.left(90)
        tess.forward(75)

    answer_string = str(answer)
    if len(answer_string) == 1:
        if answer_string[0] == "0":
            draw0()
        elif answer_string[0] == "1":
            draw1()
        elif answer_string[0] == "2":
            draw2()
        elif answer_string[0] == "3":
            draw3()
        elif answer_string[0] == "4":
            draw4()
        elif answer_string[0] == "5":
            draw5()
        elif answer_string[0] == "6":
            draw6()
        elif answer_string[0] == "7":
            draw7()
        elif answer_string[0] == "8":
            draw8()
        elif answer_string[0] == "9":
            draw9()
    if len(answer_string) == 2:
        if answer_string[0] == "0":
            draw0()
        elif answer_string[0] == "1":
            draw1()
        elif answer_string[0] == "2":
            draw2()
        elif answer_string[0] == "3":
            draw3()
        elif answer_string[0] == "4":
            draw4()
        elif answer_string[0] == "5":
            draw5()
        elif answer_string[0] == "6":
            draw6()
        elif answer_string[0] == "7":
            draw7()
        elif answer_string[0] == "8":
            draw8()
        elif answer_string[0] == "9":
            draw9()
    if len(answer_string) == 2:
        if answer_string[1] == "0":
            draw0()
        elif answer_string[1] == "1":
            draw1()
        elif answer_string[1] == "2":
            draw2()
        elif answer_string[1] == "3":
            draw3()
        elif answer_string[1] == "4":
            draw4()
        elif answer_string[1] == "5":
            draw5()
        elif answer_string[1] == "6":
            draw6()
        elif answer_string[1] == "7":
            draw7()
        elif answer_string[1] == "8":
            draw8()
        elif answer_string[1] == "9":
            draw9()
    if len(answer_string) == 3:
        if answer_string[0] == "0":
            draw0()
        elif answer_string[0] == "1":
            draw1()
        elif answer_string[0] == "2":
            draw2()
        elif answer_string[0] == "3":
            draw3()
        elif answer_string[0] == "4":
            draw4()
        elif answer_string[0] == "5":
            draw5()
        elif answer_string[0] == "6":
            draw6()
        elif answer_string[0] == "7":
            draw7()
        elif answer_string[0] == "8":
            draw8()
        elif answer_string[0] == "9":
            draw9()
    if len(answer_string) == 3:
        if answer_string[1] == "0":
            draw0()
        elif answer_string[1] == "1":
            draw1()
        elif answer_string[1] == "2":
            draw2()
        elif answer_string[1] == "3":
            draw3()
        elif answer_string[1] == "4":
            draw4()
        elif answer_string[1] == "5":
            draw5()
        elif answer_string[1] == "6":
            draw6()
        elif answer_string[1] == "7":
            draw7()
        elif answer_string[1] == "8":
            draw8()
        elif answer_string[1] == "9":
            draw9()
    if len(answer_string) == 3:
        if answer_string[2] == "0":
            draw0()
        elif answer_string[2] == "1":
            draw1()
        elif answer_string[2] == "2":
            draw2()
        elif answer_string[2] == "3":
            draw3()
        elif answer_string[2] == "4":
            draw4()
        elif answer_string[2] == "5":
            draw5()
        elif answer_string[2] == "6":
            draw6()
        elif answer_string[2] == "7":
            draw7()
        elif answer_string[2] == "8":
            draw8()
        elif answer_string[2] == "9":
            draw9()
    if len(answer_string) == 4:
        if answer_string[0] == "0":
            draw0()
        elif answer_string[0] == "1":
            draw1()
        elif answer_string[0] == "2":
            draw2()
        elif answer_string[0] == "3":
            draw3()
        elif answer_string[0] == "4":
            draw4()
        elif answer_string[0] == "5":
            draw5()
        elif answer_string[0] == "6":
            draw6()
        elif answer_string[0] == "7":
            draw7()
        elif answer_string[0] == "8":
            draw8()
        elif answer_string[0] == "9":
            draw9()
    if len(answer_string) == 4:
        if answer_string[1] == "0":
            draw0()
        elif answer_string[1] == "1":
            draw1()
        elif answer_string[1] == "2":
            draw2()
        elif answer_string[1] == "3":
            draw3()
        elif answer_string[1] == "4":
            draw4()
        elif answer_string[1] == "5":
            draw5()
        elif answer_string[1] == "6":
            draw6()
        elif answer_string[1] == "7":
            draw7()
        elif answer_string[1] == "8":
            draw8()
        elif answer_string[1] == "9":
            draw9()
    if len(answer_string) == 4:
        if answer_string[2] == "0":
            draw0()
        elif answer_string[2] == "1":
            draw1()
        elif answer_string[2] == "2":
            draw2()
        elif answer_string[2] == "3":
            draw3()
        elif answer_string[2] == "4":
            draw4()
        elif answer_string[2] == "5":
            draw5()
        elif answer_string[2] == "6":
            draw6()
        elif answer_string[2] == "7":
            draw7()
        elif answer_string[2] == "8":
            draw8()
        elif answer_string[2] == "9":
            draw9()
    if len(answer_string) == 4:
        if answer_string[3] == "0":
            draw0()
        elif answer_string[3] == "1":
            draw1()
        elif answer_string[3] == "2":
            draw2()
        elif answer_string[3] == "3":
            draw3()
        elif answer_string[3] == "4":
            draw4()
        elif answer_string[3] == "5":
            draw5()
        elif answer_string[3] == "6":
            draw6()
        elif answer_string[3] == "7":
            draw7()
        elif answer_string[3] == "8":
            draw8()
        elif answer_string[3] == "9":
            draw9()
    if len(answer_string) == 5:
        if answer_string[0] == "0":
            draw0()
        elif answer_string[0] == "1":
            draw1()
        elif answer_string[0] == "2":
            draw2()
        elif answer_string[0] == "3":
            draw3()
        elif answer_string[0] == "4":
            draw4()
        elif answer_string[0] == "5":
            draw5()
        elif answer_string[0] == "6":
            draw6()
        elif answer_string[0] == "7":
            draw7()
        elif answer_string[0] == "8":
            draw8()
        elif answer_string[0] == "9":
            draw9()
    if len(answer_string) == 5:
        if answer_string[1] == "0":
            draw0()
        elif answer_string[1] == "1":
            draw1()
        elif answer_string[1] == "2":
            draw2()
        elif answer_string[1] == "3":
            draw3()
        elif answer_string[1] == "4":
            draw4()
        elif answer_string[1] == "5":
            draw5()
        elif answer_string[1] == "6":
            draw6()
        elif answer_string[1] == "7":
            draw7()
        elif answer_string[1] == "8":
            draw8()
        elif answer_string[1] == "9":
            draw9()
    if len(answer_string) == 5:
        if answer_string[2] == "0":
            draw0()
        elif answer_string[2] == "1":
            draw1()
        elif answer_string[2] == "2":
            draw2()
        elif answer_string[2] == "3":
            draw3()
        elif answer_string[2] == "4":
            draw4()
        elif answer_string[2] == "5":
            draw5()
        elif answer_string[2] == "6":
            draw6()
        elif answer_string[2] == "7":
            draw7()
        elif answer_string[2] == "8":
            draw8()
        elif answer_string[2] == "9":
            draw9()
    if len(answer_string) == 5:
        if answer_string[3] == "0":
            draw0()
        elif answer_string[3] == "1":
            draw1()
        elif answer_string[3] == "2":
            draw2()
        elif answer_string[3] == "3":
            draw3()
        elif answer_string[3] == "4":
            draw4()
        elif answer_string[3] == "5":
            draw5()
        elif answer_string[3] == "6":
            draw6()
        elif answer_string[3] == "7":
            draw7()
        elif answer_string[3] == "8":
            draw8()
        elif answer_string[3] == "9":
            draw9()
    if len(answer_string) == 5:
        if answer_string[4] == "0":
            draw0()
        elif answer_string[4] == "1":
            draw1()
        elif answer_string[4] == "2":
            draw2()
        elif answer_string[4] == "3":
            draw3()
        elif answer_string[4] == "4":
            draw4()
        elif answer_string[4] == "5":
            draw5()
        elif answer_string[4] == "6":
            draw6()
        elif answer_string[4] == "7":
            draw7()
        elif answer_string[4] == "8":
            draw8()
        elif answer_string[4] == "9":
            draw9()
    if len(answer_string) > 5:
        tess.write("Check the Console!")
        tess.home()
        print("The answer is " + answer_string)
        print("Our turtle can not draw more than five digits")

    wn.mainloop()
