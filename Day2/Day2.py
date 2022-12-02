# Problem 1
selectedScoreDict = {"X": 1, "Y": 2, "Z": 3}

winningDict = {
    "A": ["Y", "Z"], #Rock - [loses to paper, wins to scissors]
    "B": ["Z", "X"], #Paper - [loses to scissors, wins to rock]
    "C": ["X", "Y"]  #Scissors - [loses to Rock, wins to Paper]
    }

def outcomeScore(first, second):
    #Win
    if second == winningDict[first][0]:
        return 6
    #Lost
    elif second == winningDict[first][1]:
        return 0
    #Draw
    else:
        return 3

totalScore = 0
with open('/Users/christiangrinling/Desktop/AOC2022/Day2/Day2Data.txt', 'r') as f:
    for line in f:
        selectedScore = selectedScoreDict[line[2]]
        outcomeScoreValue = outcomeScore(line[0], line[2])
        totalScore += outcomeScoreValue + selectedScore

print(totalScore)

#Problem 2
totalScore2 = 0
outcomes = {
    "A X":3, "A Y":4, "A Z":8,
    "B X":1, "B Y":5, "B Z":9,
    "C X":2, "C Y":6, "C Z":7
}    
 #X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
data = open('/Users/christiangrinling/Desktop/AOC2022/Day2/Day2Data.txt', 'r').read().split('\n')
for line in data:
    totalScore2 += outcomes[line]
    
print(totalScore2)