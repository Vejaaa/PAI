import random

class Crossword:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]
        self.words = []

    def add_word(self, word):
        word = word.upper()
        if len(word) > max(self.height, self.width):
            print(f"Word '{word}' is too long to fit in the grid.")
            return

        self.words.append(word)
        placed = False

        while not placed:
            direction = random.choice(['across', 'down'])
            if direction == 'across':
                x = random.randint(0, self.width - len(word))
                y = random.randint(0, self.height - 1)
                if self.check_fit(word, x, y, 1, 0):
                    self.place_word(word, x, y, 1, 0)
                    placed = True
            else:
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - len(word))
                if self.check_fit(word, x, y, 0, 1):
                    self.place_word(word, x, y, 0, 1)
                    placed = True

    def check_fit(self, word, x, y, dx, dy):
        for i in range(len(word)):
            if self.grid[y][x] not in [' ', word[i]]:
                return False
            x += dx
            y += dy
        return True

    def place_word(self, word, x, y, dx, dy):
        for i in range(len(word)):
            self.grid[y][x] = word[i]
            x += dx
            y += dy

    def display(self):
        for row in self.grid:
            print(' '.join(row))


def main():
    crossword = Crossword(12, 12)
    words = ["PYTHON", "ALGORITHM", "PROGRAMMING", "COMPUTER", "LANGUAGE"]
    for word in words:
        crossword.add_word(word)

    crossword.display()


if __name__ == "__main__":
    main()
