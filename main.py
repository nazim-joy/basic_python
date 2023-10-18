print("Stylish font created by Nazim Ahmed")
name = input("Please enter your name: ")
for x in name:
    if x == 'A' or x == 'a':
        def A():

            block = ""
            for rows in range(0, 7):
                for column in range(0, 7):
                    if ((column == 1 or column == 5) and rows != 0) or ((rows == 0 or rows == 3) and (column>1 and column<5)):
                        block = block + "* "
                    else:
                        block = block + "  "
                block += "\n"
            print(block)

        A()
    elif x == 'B' or x == 'b':
        def B():

            block = ""
            for rows in range(0, 7):
                for column in range(0, 7):
                    if column == 1 or column == 5 and (rows != 0 and rows != 3 and rows != 6) or (rows == 0 or rows == 3 or rows == 6) and (column > 1 and column < 5):
                        block = block + "* "
                    else:
                        block = block + "  "
                block += "\n"
            print(block)

        B()
    elif x == 'C' or x == 'c':
        def C():

            block = ""
            for rows in range(0, 7):
                for column in range(0, 7):
                    if (column == 1 and (rows > 0 and rows < 6)) or (rows == 0 or rows == 6) and (column > 1 and column < 5) or (rows == 1 or rows == 5) and column == 5:
                        block = block + "* "
                    else:
                        block = block + "  "
                block += "\n"
            print(block)

        C()
    elif x == "D" or x == 'd':
        def D():
            block = ""
            for rows in range(0, 7):
                for column in range(0, 7):
                    if column == 1 or (column == 5 and (rows > 0 and rows < 6)) or (rows == 0 or rows == 6) and (column > 0 and column < 5):
                        block = block + "* "
                    else:
                        block = block + "  "
                block += "\n"
            print(block)


        D()
    elif x == "E" or x == 'e':
        def E():
            block = ""
            for rows in range(0, 7):
                for column in range(0, 7):
                    if column == 1 or ((rows == 0 or rows == 3 or rows == 6) and (column > 1 and column < 6)):
                        block = block + "* "
                    else:
                        block = block + "  "
                block += "\n"
            print(block)


        E()
    elif x == "F" or x =='f':
        def F():
            block = ""
            for rows in range(0, 7):
                for column in range(0, 7):
                    if column == 1 or ((rows == 0 or rows == 3) and (column > 1 and column < 6)):
                        block = block + "* "
                    else:
                        block = block + "  "
                block += "\n"
            print(block)


        F()
    elif x == 'G' or x == 'g':
        def G():

            block = ""
            for rows in range(0, 7):
                for column in range(0, 7):
                    if (column == 1 and (rows > 0 and rows < 6)) or (rows == 0 or rows == 6) and (column > 1 and column < 5) or (rows == 1 or rows == 4 or rows == 5) and column == 5 or (rows == 3 and (column ==5 or column ==4 or column ==3)):
                        block = block + "* "
                    else:
                        block = block + "  "
                block += "\n"
            print(block)
        G()
    elif x == 'H' or x == 'h':
        def H():

            block = ""
            for rows in range(0, 7):
                for column in range(0, 7):
                    if column == 1 or column == 5 or (rows == 3 and (column > 1 and column < 6)):
                        block = block + "* "
                    else:
                        block = block + "  "
                block += "\n"
            print(block)
        H()
    elif x == 'I' or x == 'i':
        def I():

            block = ""
            for rows in range(0, 7):
                for column in range(0, 7):
                    if column == 3 or (rows == 0 or rows == 6) and (column > 1 and column < 5):
                        block = block + "* "
                    else:
                        block = block + "  "
                block += "\n"
            print(block)
        I()
    elif x == 'J' or x == 'j':
        def J():

            block = ""
            for rows in range(0, 7):
                for column in range(0, 7):
                    if (column == 5 and rows < 6) or (rows == 0 and (column > 0 and column < 6)) or (column == 2 or column == 3 or column == 4) and (rows == 6 or column == 1 and rows == 4 or rows == 5)):
                        block = block + "* "
                    else:
                        block = block + "  "
                block += "\n"
            print(block)


        J()