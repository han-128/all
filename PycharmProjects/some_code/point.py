#def score(dice):

dice = [5, 1, 3, 4, 1]
score = 0
one = 10
dice = sorted(dice)
score += dice.count(1) % 3 *100
score += dice.count(5) % 3 *50
for x in range(1, 7):
    t = dice.count(x) 
    score += t//3 * x * 100 * one
    one = 1
print(score)

#    return score
