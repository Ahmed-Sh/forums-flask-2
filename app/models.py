########################################
# Models
########################################
import datetime

class member:
    def __init__(self, name, age):
        self.id = 0
        self.name = name
        self.age = age
        self.posts = []

    def __repr__(self):
        return """Name: {} , Age: {}""".format(self.name, self.age)

    def __dict__(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "posts": self.posts,
        }

class post:
    def __init__(self, title, content, member_id=0):
        self.id = 0
        self.title = title
        self.content = content
        self.member_id = member_id
        self.date = datetime.datetime.now()

    def __repr__(self):
        return """Title: {} , Content: {}""".format(self.title, self.content)

    def __dict__(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "member_id": self.member_id,
        }
