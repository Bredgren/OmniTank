
import time, sqlite3
from constants import SCORES_DB

class Score:
    def __init__(self, name, points, level, date):
        self.name = name
        self.points = points
        self.level = level
        self.date = date

#TODO: external database for global high scores (how to securely access?)
class HighScores:
    def __init__(self):
        # connect to database or set it up if it doesn't exist
        self.database = None
        self.cursor = None
        try:
            with open(SCORES_DB):
                self._connectdb()
        except IOError:
            self._setupdb()

    def _setupdb(self):
        self._connectdb()
        # name - the players name
        # points - the players score
        # level - the maximum level achieved by the player
        # data - when the entry was made
        # synced - 0 if not in the global database, 1 if it is
        # A primary key does not make sense for this table
        self.cursor.execute('''
            CREATE TABLE scores (
            name VARCHAR(10),
            points int,
            level int,
            date VARCHAR(24),
            synced int
            )''')

    def _connectdb(self):
        self.database = sqlite3.connect(SCORES_DB)
        self.cursor = self.database.cursor()

    def __del__(self):
        self.database.close()

    """ Gets the top n local high scores """
    def localTop(self, n):
        results = []
        rows = self.cursor.execute('''
            SELECT *
            FROM scores
            ORDER BY points DESC
            LIMIT ?''', (n,))
        for row in rows:
            results.append(Score(row[0], row[1], row[2], row[3]))
        return results

    """ Gets the top n global high scores """
    def globalTop(self, n):
        pass

    """ Addes rows from the local database to the global one if they haven't already """
    def updateGlobal(self):
        pass

    def newScore(self, name, points, level):
        row = (name, points, level, time.ctime())
        self.cursor.execute('''
            INSERT INTO scores
            VALUES(?, ?, ?, ?, 0)
        ''', row)
        self.database.commit()

# Gobal variable acts as Singleton
HighScores = HighScores()
