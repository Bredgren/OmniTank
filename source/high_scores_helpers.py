
import time, sqlite3
from constants import HS_ENTRY_MAX_NAME_LENGTH, SCORES_DB

class Score:
    def __init__(self, name, points, level, date):
        self.name = name
        self.points = points
        self.level = level
        self.date = date

    def __eq__(self, other):
        return (self.name == other.name and self.points == other.points and
                self.level == other.level and self.date == other.date)

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
        date_size = 24
        # name - the players name
        # points - the players score
        # level - the maximum level achieved by the player
        # data - when the entry was made
        # synced - 0 if not in the global database, 1 if it is
        # A primary key does not make sense for this table
        self.cursor.execute('''
            CREATE TABLE scores (
            name VARCHAR(%d),
            points int,
            level int,
            date VARCHAR(%d),
            synced int
            )''' % (HS_ENTRY_MAX_NAME_LENGTH, date_size))

    def _connectdb(self):
        self.database = sqlite3.connect(SCORES_DB)
        self.cursor = self.database.cursor()

    def __del__(self):
        self.database.close()

    """ Returns the rank of the givien score, or 0 if the score doesn't exist """
    def getLocalRank(self, score):
        scores = []
        rows = self.cursor.execute('''
            SELECT *
            FROM scores
            ORDER BY points DESC''')
        for row in rows:
            scores.append(Score(row[0], row[1], row[2], row[3]))

        if score not in scores:
            return 0
        
        return scores.index(score) + 1

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
        data = time.ctime()
        row = (name, points, level, date)
        self.cursor.execute('''
            INSERT INTO scores
            VALUES(?, ?, ?, ?, 0)
        ''', row)
        self.database.commit()

        local_rank = self.getLocalRank(Score(name, points, level, date))
        global_rank = 0
        assert local_rank != 0 # We just added it so this would indicate a problem
        return local_rank, global_rank

# Gobal variable acts as Singleton
HighScores = HighScores()
