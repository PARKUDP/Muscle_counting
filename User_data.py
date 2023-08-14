import User
import sqlite3

class data():
    def __init__(self, dbname='User.db'):
        self.dbname = dbname
        self.con = sqlite3.connect(self.dbname)
        self.cur = self.con.cursor()
        self.DATA_SET

    def DATA_SET(self):
        try:
            self.cur.execute(
                'CREATE TABLE Userdata (training STRING, rep INTEGER, number_set INTEGER, rest_time INTEGER)')
            self.con.commit()

        except sqlite3.OperationalError:
            pass

    def DATA_IN(self, training, rep, number_set, rest_time):
        try:
            self.cur.execute('INSERT INTO Userdata VALUES(?, ?, ?, ?)',
                             (training, rep, number_set, rest_time))
            self.con.commit()

        except sqlite3.OperationalError:
            pass

    def DATA_REMOVE_ALL(self):
        try:
            self.cur.execute('DELETE FROM Userdata')
            self.con.commit()

        except sqlite3.OperationalError:
            pass

    def data_remove_select(self, name):
        try:
            self.cur.execute('DELETE FROM Userdata WHERE training = ?', (name,))
            self.con.commit()

        except sqlite3.OperationalError:
            pass

    def get_all_data(self):
        try:
            self.cur.execute('SELECT * FROM Userdata')
            return self.cur.fetchall()
        except sqlite3.OperationalError:
            return []

    def set_complete(self, count, name):
        count -= 1
        self.cur.execute(
            "UPDATE  Userdata SET number_set = ? WHERE training = ?", (count, name))
        self.con.commit()

    def define_data(self, training, rep, num_set, reset_time):
        self.cur.execute(
            "UPDATE Userdata SET rep = ?, number_set = ?, rest_time = ? WHERE training = ?", (rep, num_set, reset_time, training))
        self.con.commit()
        
    def __del__(self):
        self.cur.close()
        self.con.close()