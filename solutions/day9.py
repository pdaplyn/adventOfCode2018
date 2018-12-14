"""
>>> # 9 players; last marble is worth   25 points: high score is 32
>>> game = Circle(9)
>>> game.play(25)
>>> game.high_score()
32
>>> #10 players; last marble is worth 1618 points: high score is 8317
>>> game = Circle(10)
>>> game.play(1618)
>>> game.high_score()
8317
>>> #13 players; last marble is worth 7999 points: high score is 146373
>>> game = Circle(13)
>>> game.play(7999)
>>> game.high_score()
146373
>>> #17 players; last marble is worth 1104 points: high score is 2764
>>> game = Circle(17)
>>> game.play(1104)
>>> game.high_score()
2764
>>> #21 players; last marble is worth 6111 points: high score is 54718
>>> game = Circle(21)
>>> game.play(6111)
>>> game.high_score()
54718
>>> #30 players; last marble is worth 5807 points: high score is 37305
>>> game = Circle(30)
>>> game.play(5807)
>>> game.high_score()
37305
"""


class Circle:
    def __init__(self, players):
        self.current_player = -1
        self.scores = [0 for x in range(players)]
        self.marbles = [0]
        self.current = 0

    def high_score(self):
        return max(self.scores)

    def place(self, value):
        self.next()
        if not value % 23 == 0:
            self.current = self.find_next_place(2)
            self.marbles.insert(self.current, value)
        else:
            self.current = self.find_next_place(-7)
            removed = self.marbles.pop(self.current)
            if self.current >= len(self.marbles):
                self.current = 0
            self.scores[self.current_player] += value
            self.scores[self.current_player] += removed

    def next(self):
        self.current_player = (self.current_player + 1) % len(self.scores)

    def find_next_place(self, change):
        new_index = self.current + change
        if new_index > len(self.marbles):
            new_index -= len(self.marbles)
        elif new_index < 0:
            new_index += len(self.marbles)
        return new_index

    def print(self):
        display = "[" + str(self.current_player+1) + "] "
        for i in range(len(self.marbles)):
            value = str(self.marbles[i])
            if len(value) == 2:
                display = display.rstrip()
            if i == self.current:
                display += "(" + value + ")"
            else:
                display += " " + value + " "
        print(display)

    def play(self, up_to):
        for i in range(1,up_to+1):
            self.place(i)
            #self.print()


# 452 players; last marble is worth 70784 points
game = Circle(452)
game.play(70784)
print("High score:", game.high_score())


if __name__ == "__main__":
    import doctest
    doctest.testmod()
