def compareStrength(strength,energy):
    if (energy == strength):
        return "Both are equal"

    else:
        count=0
        for i in range(len(energy)):
            if (energy[i] >= strength[i]):
                count += 1

        if (count == len(energy)):
            return "Result - WIN"

        else:
            return "Result - LOSE"

