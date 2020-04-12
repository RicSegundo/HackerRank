
n = 9
scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]


def breakingRecords(scores):
    max_score = scores[0]
    min_score = scores[0]
    max_score_beaten = 0
    min_score_beaten = 0

    for score in scores[1:]:
        if score > max_score:
            max_score = score
            max_score_beaten += 1
        elif score < min_score:
            min_score = score
            min_score_beaten += 1

    return [max_score_beaten, min_score_beaten]


print(breakingRecords(scores))

