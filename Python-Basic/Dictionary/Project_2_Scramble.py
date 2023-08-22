'''
Scrabble
In this project, you will process some data from a group of friends playing scrabble.
You will use dictionaries to organize players, words, and points.
'''

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1,
          3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {k: v for k, v in zip(letters, points)}

letter_to_points[' '] = 0


def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter, 0)
    return point_total


brownie_points = score_word('BROWNIE')
print(brownie_points)

player_to_words = {
    'player1': ['BLUE', 'TENNIS', 'EXIT'],
    'wordNerd': ['EARTH', 'EYES', 'MACHINE'],
    'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'],
    'Prof Reader': ['ZAP', 'COMA', 'PERIOD'],
}

player_to_points = {}

for k, v in player_to_words.items():
    player_points = 0
    for val in v:
        player_points += score_word(val)
    player_to_points[k] = player_points

print(player_to_points)
