from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]
users
sorted(users, key=lambda u: u.user_id)

sorted(users, key=attrgetter('user_ud'))

by_name = sorted(users, key=attrgetter('last_name', 'first_name'))

min(users, key=attrgetter('user_id'))
max(users, key=attrgetter('user_id'))

