from Minesweeper.tile import Tile

import csv

def readLeaderboard():
    users = []

    with open('Infinite Minesweeper/Miscellaneous/leaderboard.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)

def writeLeaderboard(leaderboard):
    with open('Infinite Minesweeper/Miscellaneous/leaderboard.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["user", "tiles", "time", "mines"])

def readGame():
    tiles = {}

    with open('Infinite Minesweeper/Miscellaneous/savedgame.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader) # skip the header

        for row in reader:
            tiles[(int(row[0]), int(row[1]))] = (Tile(int(row[0]), int(row[1]), bool(int(row[2]))))

        return tiles

def writeGame(tiles):
    with open('Infinite Minesweeper/Miscellaneous/savedgame.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["x", "y", "mine"])
        for tile in tiles.values():
            writer.writerow([tile.x, tile.y, int(tile.mine)])