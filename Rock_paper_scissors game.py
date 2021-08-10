while True:
    p1 = input("Input choice of p1:")
    p2 = input("Input choice of p2:")
    if p1 == p2:
        print("It's a tie!")
    elif p1 == "rock":
        if p2 == "scissors":
            print("p1 wins!!!")

        else:
            print("p2 wins!!!")

    elif p1 == "paper":
        if p2 == "rock":
            print("p1 wins!!!")

        else:
            print("p2 wins!!!")
    elif p1 == "scissors":
        if p2 == "paper":
            print("p1 wins!!!")
        else:
            print("p2 wins!!!")
    new_game = input("Do you want to play a new game? (y/n): ")
    if(new_game!='y'):
        break