
# Inputs for case 1
scores = [100, 100, 50, 40, 40, 20, 10]
alice = [5, 25, 50, 120]

def climbingLeaderboard(scores, alice):

    unique_scores = list(reversed(sorted(set(scores))))

    score_index = len(alice) - 1
    position = 0
    places = []

    while score_index >= 0:
        if position >= len(unique_scores) or unique_scores[position] <= alice[score_index]:
            places.append(position + 1)
            score_index -= 1
        else:
            position += 1

    return reversed(places)


if __name__ == '__main__':
    result = climbingLeaderboard(scores, alice)

    print(*result, sep='\n')

