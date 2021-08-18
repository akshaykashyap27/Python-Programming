class Enemy:
    enemy = input("Enter the strength of enemies(values seperated by space):").split()
    EnemyMap = list(map(int, enemy))
    EnemyMap.sort()



