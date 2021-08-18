def compareStrength(strength,energy):
    if (energy == strength):
        print("Both are equal")

    else:
        count=0
        for i in range(len(energy)):
            if (energy[i] >= strength[i]):
                count += 1

        if (count == len(energy)):
            print("Result - WIN")

        else:
            print("Result - LOSE")

