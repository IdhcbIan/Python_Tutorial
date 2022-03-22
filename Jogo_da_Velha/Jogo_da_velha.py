

#           // Jogo Da Velha  //


hoese = ""
moves = 1
win = 0
c1 = "-"
c2 = "-"
c3 = "-"
c4 = "-"
c5 = "-"
c6 = "-"
c7 = "-"
c8 = "-"
c9 = "-"


while not moves >= 9 and win != 1:

    print()
    print("|", c1, "|", c2, "|", c3, "|")
    print("--------------")
    print("|", c4, "|", c5, "|", c6, "|")
    print("--------------")
    print("|", c7, "|", c8, "|", c9, "|")
    print()
    print()
    print("|", "c1", "|", "c2", "|", "c3", "|")
    print("--------------")
    print("|", "c4", "|", "c5", "|", "c6", "|")
    print("--------------")
    print("|", "c7", "|", "c8", "|", "c9", "|")
    print()
    # ///////////////////////////////////// Player 1 ////////////////////////////////////////////////////////////

    if win == 0:
        print("player 1")
        housex = input("enter a house:")

        if housex == "c1":
            c1 = "x"
        if housex == "c2":
            c2 = "x"
        if housex == "c3":
            c3 = "x"
        if housex == "c4":
            c4 = "x"
        if housex == "c5":
            c5 = "x"
        if housex == "c6":
            c6 = "x"
        if housex == "c7":
            c7 = "x"
        if housex == "c8":
            c8 = "x"
        if housex == "c9":
            c9 = "x"

        print()
        print("|", c1, "|", c2, "|", c3, "|")
        print("--------------")
        print("|", c4, "|", c5, "|", c6, "|")
        print("--------------")
        print("|", c7, "|", c8, "|", c9, "|")
        print()
        print()
        print("|", "c1", "|", "c2", "|", "c3", "|")
        print("--------------")
        print("|", "c4", "|", "c5", "|", "c6", "|")
        print("--------------")
        print("|", "c7", "|", "c8", "|", "c9", "|")
        print()
        if c1 == "x" and c2 == "x" and c3 == "x":
            print("player1 wins")
            win = 1
        if c1 == "x" and c4 == "x" and c7 == "x":
            print("player1 wins")
            win = 1
        if c1 == "x" and c5 == "x" and c9 == "x":
            print("player1 wins")
            win = 1
        if c3 == "x" and c6 == "x" and c9 == "x":
            print("player1 wins")
            win = 1
        if c7 == "x" and c8 == "x" and c9 == "x":
            print("player1 wins")
            win = 1
            win == 2
        if c2 == "x" and c5 == "x" and c8 == "x":
            print("player1 wins")
            win = 1
        if c1 == "x" and c5 == "x" and c9 == "x":
            print("player1 wins")
            win = 1
        if c3 == "x" and c5 == "x" and c7 == "x":
            print("player1 wins")
            win = 1
        else:
            win == 2

        moves += 1

    # ///////////////////////////////////// Player 2 ////////////////////////////////////////////////////////////

    if win == 0:
        print("player 2")
        housey = input("enter a house:")

        if housey == "c1":
            c1 = "o"
        if housey == "c2":
            c2 = "o"
        if housey == "c3":
            c3 = "o"
        if housey == "c4":
            c4 = "o"
        if housey == "c5":
            c5 = "o"
        if housey == "c6":
            c6 = "o"
        if housey == "c7":
            c7 = "o"
        if housey == "c8":
            c8 = "o"
        if housey == "c9":
            c9 = "o"

        print()
        print("|", c1, "|", c2, "|", c3, "|")
        print("--------------")
        print("|", c4, "|", c5, "|", c6, "|")
        print("--------------")
        print("|", c7, "|", c8, "|", c9, "|")
        print()

        moves += 1

        if c1 == "o" and c2 == "o" and c3 == "o":
            print("player2 wins")
            win = 1
        if c1 == "o" and c4 == "o" and c7 == "o":
            print("player2 wins")
            win = 1
        if c1 == "o" and c5 == "o" and c9 == "o":
            print("player2 wins")
            win = 1
        if c3 == "o" and c6 == "o" and c9 == "o":
            print("player2 wins")
            win = 1
        if c7 == "o" and c8 == "o" and c9 == "o":
            print("player2 wins")
            win = 1
        if c2 == "o" and c5 == "o" and c8 == "o":
            print("player2 wins")
            win = 1
        if c3 == "o" and c5 == "o" and c7 == "o":
            print("player2 wins")
            win = 1
        else:

            # /////////////////////////////////////////////////////
            print()
