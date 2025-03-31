from models.user.user import User
from utils.verifiers import person_verifiers
from database.database_config import user_db


class UserService:


    @staticmethod
    def create_user(name, age, skill, job=None):
        person = User(name, age, skill, job)
        person_verifiers.verify_person(person)
        user_db.append([person.__dict__.values()])
        return person

    @staticmethod
    def update_user(user_id, name, age, skill, job):
        user = user_db.read()
        for person in user:
            if person[0] == user_id:
                person[1] = name
                person[2] = age
                person[3] = skill
                person[4] = job
                user_db.delete()
                user_db.append(person)
                return True
        return False

    @staticmethod
    def delete_user(user_id):
        user_db.delete(user_id)
        return True
