from Minesweeper.tile import Tile
from Miscellaneous.board_entry import Entry

import csv

def readLeaderboard():
    """Reads the leaderboard and saves it to a list."""
    users = []

    with open('Infinite Minesweeper/Miscellaneous/leaderboard.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)

        for entry in reader:
            users.append(Entry(entry[0], int(entry[1]), float(entry[2]), int(entry[3])))
        
    return sorted(users, key=lambda u: u.score, reverse=True)

def writeLeaderboard(leaderboard):
    """Writes to the leaderboard save."""
    with open('Infinite Minesweeper/Miscellaneous/leaderboard.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["user", "tiles", "time", "mines"])

        for entry in leaderboard:
            writer.writerow([entry.user, entry.tiles, entry.time, entry.mines])

def readGame():
    """Reads the current saved game and saves it to a dict."""
    tiles = {}

    with open('Infinite Minesweeper/Miscellaneous/saved_game.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader) # skip the header

        for row in reader:
            tiles[(int(row[0]), int(row[1]))] = (Tile(int(row[0]), int(row[1]), bool(int(row[2]))))

    return tiles

def writeGame(tiles):
    """Writes to the board save."""
    with open('Infinite Minesweeper/Miscellaneous/saved_game.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["x", "y", "mine"])
        for tile in tiles.values():
            writer.writerow([tile.x, tile.y, int(tile.mine)])