########################################
# Stores
########################################
import itertools
import copy

class BaseStore():

    def __init__(self, data_provider, last_id):
        self._data_provider = data_provider
        self._last_id = last_id

    def get_all(self):
        return self._data_provider

    def add(self, item_instance):
        item_instance.id = self._last_id
        self._data_provider.append(item_instance)
        self._last_id += 1

    def get_by_id(self, id):
        all_members = self.get_all()
        member = None
        for m in all_members:
            if m.id == id:
                member = m
        return member

    def update(self, item_instance):
        result = item_instance
        all_instances = self.get_all()

        for index, current_post in enumerate(all_instances):
            if current_post.id == item_instance.id:
                all_instances[index] = item_instance
                break

        return result

    def delete(self, id):
        member = self.get_by_id(id)
        if member is not None:
            self._data_provider.remove(member)

    def entity_exists(self, item_instance):
        result = None
        result = self.get_by_id(item_instance.id)
        return result


class MemberStore(BaseStore):

    members = []
    last_id = 1

    def __init__(self):
        super().__init__(MemberStore.members, MemberStore.last_id)

    def get_by_name(self, name):
        all_members = self.get_all()

        for member in all_members:
            if member.name == name:
                yield member

    def get_members_with_posts(self, all_posts):
        all_members = copy.deepcopy(self.get_all())
        for member, post in itertools.product(all_members, all_posts):
                if (member.id == post.member_id):
                    member.posts.append(post)

        for member in all_members:
            yield member

    def get_top_two(self, all_posts):
        top_number = 2
        member_with_posts = self.get_members_with_posts(all_posts)
        member_with_posts_sorted = sorted(member_with_posts, key=lambda member_with_posts: len(member_with_posts.posts), reverse=True)
        return member_with_posts_sorted[0:top_number]

    def __repr__(self):
        return """Members: {}""".format(self.members)

class PostStore(BaseStore):

    posts = []

    def get_posts_by_date(self):
        all_posts = self.get_all()
        all_posts_sorted = sorted(all_posts, key=lambda all_posts: all_posts.date, reverse=True)
        return all_posts_sorted

    def __init__(self):
        super().__init__(PostStore.posts,0)

    def __repr__(self):
        return """Posts: {}""".format(self.posts)
