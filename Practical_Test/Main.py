from Class_Enemy import Enemy
from Class_Heroes import Hero

strength=Enemy.EnemyMap
energy=Hero.HeroMap



if (len(strength) != len(energy)):
    raise Exception("Number of heroes and enemies don't match")
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

compareStrength(strength,energy)
