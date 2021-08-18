from compareFunc import compareStrength
from Class_Enemy import Enemy
from Class_Heroes import Hero


strength=Enemy.EnemyMap
energy=Hero.HeroMap



if (len(strength) != len(energy)):
    raise Exception("Number of heroes and enemies don't match")

else:
    compareStrength(strength, energy)
    print(strength)
    print(energy)
