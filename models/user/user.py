from database.database import get_last_id


class User:

    CLASS_VERSION = "1.0.0"

    # TODO: replace with a better id generation mechanism

    user_id_counter = get_last_id('data/users.csv')

    def __init__(self, name, age, skill, job=None):
        self.id = User.user_id_counter
        User.user_id_counter += 1
        self.name = name
        self.age = age
        self.skill = skill
        self.job = job

