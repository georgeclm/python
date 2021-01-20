def breakingRecords(scores):
    breakhigh = 0
    breaklow = 0
    maxscore = scores[0]
    minscore = scores[0]
    for i in scores:
        if i > maxscore:
            breakhigh += 1
            maxscore = i
        elif i < minscore:
            breaklow += 1
            minscore = i
    return breakhigh, breaklow
