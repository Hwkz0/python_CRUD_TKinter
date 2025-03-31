import csv
import os


class Database:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
        return data

    def update_row(self, id, new_data):
        data = self.read()
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for row in data:
                if row[0] == id:
                    writer.writerow(new_data)
                else:
                    writer.writerow(row)

    def append(self, data):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def delete(self):
        open(self.filename, 'w').close()

    def delete(self, id):
        data = self.read()
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for row in data:
                if row[0] != id:
                    writer.writerow(row)

    @staticmethod
    def create(filename, headers):
        db = Database(f'data/{filename}.csv')
        db.append([headers])
        return db


def get_last_id(filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
            last_id = int(data[-1][0]) + 1
    except FileNotFoundError:
        last_id = 0
    return last_id

def initialize_databases():
    if not os.path.exists('data/jobs.csv'):
        Database.create('jobs', ['id', 'title', 'company', 'location', 'start_datetime',
                                 'end_datetime', 'skills_required'])
        print("successfully created jobs.csv")

    if not os.path.exists('data/users.csv'):
        Database.create('users', ['id', 'name', 'age', 'skill', 'job'])
        print("successfully created users.csv")

    if not os.path.exists('data/applications.csv'):
        Database.create('applications', ['id', 'job_id', 'user_id', 'status'])
        print("successfully created applications.csv")




