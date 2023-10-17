class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("Tom", 1)
user2 = User("John", 2)

user1.follow(user2)

print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
