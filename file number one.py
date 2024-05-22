class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level


class Admin(User):
    def __init__(self, user_id, name, access_level='admin'):
        super().__init__(user_id, name, access_level)
        self.__users = []

    def add_user(self, user):
        self.__users.append(user)

    def remove_user(self, user):
        if user in self.__users:
            self.__users.remove(user)
        else:
            print("User not found in the list.")

    def get_users(self):
        return self.__users


# Пример использования
user1 = User(1, "Alice")
user2 = User(2, "Bob")
user3 = User(3, "Eve")

admin = Admin(0, "Admin")

admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)

admin.remove_user(user2)

print("Admin users:")
for user in admin.get_users():
    print(user.get_name())