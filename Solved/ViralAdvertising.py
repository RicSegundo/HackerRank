import math

n = 5


def viralAdvertising(n: int) -> int:
    likes = 0
    people = 5
    for day in range(1, n+1):
        likes += math.floor(people/2)
        people = math.floor(people/2) * 3
    
    return likes


print(viralAdvertising(n))

