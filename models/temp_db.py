from models.models import User


class DataBaseManager:
    def __init__(self):
        self.users_db = []
        self._load_initial_data()

    def _load_initial_data(self):
        self.users_db.append(User(id=1, name="Alice", age=30, city="New York", email="alice@example.com"))
        self.users_db.append(User(id=2, name="Bob", age=25, city="Boston", email="bob@example.com"))
        self.users_db.append(User(id=3, name="Charlie", age=35, city="Chicago", email="charlie@example.com"))
        self.users_db.append(User(id=4, name="Bubka", age=43, city="Svishtov", email="bubka@example.com"))
