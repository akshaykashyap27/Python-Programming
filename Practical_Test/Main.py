from Class_Enemy import Enemy
from Class_Heroes import Hero

strength=Enemy.EnemyMap
energy=Hero.HeroMap

count=0

if (len(strength) != len(energy)):
    raise Exception("Number of heroes and enemies don't match")

else:
    if (energy == strength):
        print("Both are equal")

    else:
        for i in range(len(energy)):
            if (energy[i] >= strength[i]):
                count+=1


        if(count==len(energy)):
            print("Result - WIN")

        else:
            print("Result - LOSE")

