from database.database_config import user_db


class UserRepository:

    @staticmethod
    def get_all_users():
        return user_db.read()

    @staticmethod
    def get_user_by_id(user_id):
        user = user_db.read()
        for user in user:
            if user[0] == user_id:
                return user
        return None

    @staticmethod
    def get_users_by_name(name):
        users = user_db.read()
        users_by_name = []
        for user in users:
            if name in user[1]:
                users_by_name.append(user)
        return users_by_name

    @staticmethod
    def get_users_by_age(age):
        users = user_db.read()
        users_by_age = []
        for user in users:
            if age in user[2]:
                users_by_age.append(user)
        return users_by_age

    @staticmethod
    def get_users_by_skill(skill):
        users = user_db.read()
        user_by_skill = []
        for user in users:
            if skill in user[3]:
                user_by_skill.append(user)
        return user_by_skill

    @staticmethod
    def get_users_by_job(job):
        users = user_db.read()
        users_by_job = []
        for user in users:
            if job in user[4]:
                users_by_job.append(user)
        return users_by_job

    @staticmethod
    def get_user_skills(user_id):
        users = user_db.read()
        for user in users:
            if user[0] == user_id:
                return user[3]
        return None
