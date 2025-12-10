from Minesweeper.tile import Tile
from Miscellaneous.board_entry import Entry

import csv

def readLeaderboard():
    """Reads the leaderboard and saves it to a list."""
    users = []

    with open('jf_CP3_final/Infinite Minesweeper/Miscellaneous/leaderboard.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)

        for entry in reader:
            users.append(Entry(entry[0], int(entry[1]), float(entry[2]), int(entry[3])))
        
    return sorted(users, key=lambda u: u.score, reverse=True)

def writeLeaderboard(user, tiles, time, mines):
    """Writes to the leaderboard save."""
    with open('jf_CP3_final/Infinite Minesweeper/Miscellaneous/leaderboard.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(user, tiles, time, mines)

def readGame():
    tiles = {}

    with open('jf_CP3_final/Infinite Minesweeper/Miscellaneous/saved_game.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)

        try:
            seed, tilecount, time, mines, x, y = next(reader)
        except StopIteration:
            return {}

        for row in reader:
            tiles[(int(row[0]), int(row[1]))] = Tile(int(row[0]), int(row[1]), bool(int(row[2])), bool(int(row[3])), bool(int(row[4])))

    return tiles, seed, int(tilecount), float(time), int(mines), (int(x), int(y))

def writeGame(tiles, seed, tilecount, time, mines, origin):
    """Writes to the board save."""
    with open('jf_CP3_final/Infinite Minesweeper/Miscellaneous/saved_game.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["x", "y", "mine", "revealed", "flagged"])
        writer.writerow([seed, tilecount, time, mines, origin[0], origin[1]])
        for tile in tiles.values():
            writer.writerow([tile.x, tile.y, int(tile.mine), int(tile.revealed), int(tile.flagged)])

def clearGame():
    """Clears the saved game."""
    with open('jf_CP3_final/Infinite Minesweeper/Miscellaneous/saved_game.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["x", "y", "mine", "revealed", "flagged"])