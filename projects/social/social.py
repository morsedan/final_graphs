import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        for i in range(0, num_users):
            self.add_user(f"User {i}")
        # Add users
        #
        # for user_id in self.users:
        #     users_copy = self.users.copy()
        #     del users_copy[user_id]
        #     num = random.randint(0,num_users-1)
        #     friend = f"User {num}"

        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        random.shuffle(possible_friendships)
        # Create friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        visited = self.fbft(user_id)
        return visited

    # def bft(self, start):
    #     v = set()
    #     q = Queue()
    #     path = [start]
    #     paths = {}
    #
    #     q.enqueue([start])
    #     while q.size() > 0:
    #         path = q.dequeue()
    #         end = path[-1]
    #         if end not in v:
    #             paths[end] = path
    #             # print(end, path)  # instead of printing I want to do a bfs
    #             paths[end] = path
    #             v.add(end)
    #             for neighbor in self.friendships[end]:
    #                 if neighbor not in v:
    #                     new_path = path.copy() + [neighbor]
    #                     q.enqueue(new_path)
    #     return paths

    def fbft(self, start):
        q = Queue()
        paths = {}

        q.enqueue([start])
        while q.size() > 0:
            path = q.dequeue()
            end = path[-1]
            if end not in paths:
                paths[end] = path
                for neighbor in self.friendships[end]:
                    if neighbor not in paths:
                        new_path = path.copy() + [neighbor]
                        q.enqueue(new_path)
        return paths

    # def bfs(self, start, finish):



if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    print(sg.friendships)
    connections = sg.get_all_social_paths(3)
    print(connections)
    print(f"Users in extended social network: {len(connections)-1}")

    total_social_paths = 0
    for user_id in connections:
        total_social_paths += len(connections[user_id])
    print(f"Avg length of social path: {total_social_paths / len(connections)}")