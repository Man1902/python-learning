class User:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User(1, "Alex")
user2 = User(2, "Prince")
user3 = User(3, "Zoho")
user4 = User(4, "Chrles")
user5 = User(5, "Peter")

user1.follow(user2)
user2.follow(user5)
user4.follow(user1)
user5.follow(user2)
user3.follow(user1)


print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
