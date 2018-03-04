########################################
# Main
########################################

import models
import stores
from time import sleep

member_store = stores.MemberStore()
post_store = stores.PostStore()

def create_members():

    member1 = models.member("Mohammed", 20)
    member2 = models.member("Omar", 22)
    member3 = models.member("Abdo", 25)
    print(member1)
    print(member2)
    print(member3)
    print("=" * 30)

    return member1, member2, member3


def add_models_to_store(members_instances, member_store):

    for member in members_instances:
        member_store.add(member)


def print_all_members(member_store):
    print("=" * 30)

    for member in member_store.get_all():
        print(member)

    print("=" * 30)

def test_update(member_store, member3):
    member3_copy = models.member(member3.name, member3.age)
    member3_copy.id = 3

    if member3_copy is not member3:
        print("member3 and member3_copy are not the same !")

    print(member3_copy)
    member3_copy.name = "Ahmed"
    member3_copy.age = "26"
    member_store.update(member3_copy)
    print(member_store.get_by_id(member3.id))

def test_get_by_name(member_store, name):
    print("=" * 30)
    member = member_store.get_by_name(name)
    print(member)

def catch_exception_when_deleting():
    try:
        member_store.delete(5)
    except ValueError:
        print("It should be an existence entity before deleting !")


# ========= Posts =================================================

def create_posts(members_instances):

    post1 = models.post("Agriculture", "Agriculture is amazing", members_instances[0].id)
    sleep(5)
    post2 = models.post("Engineering", "I love engineering", members_instances[0].id)

    post3 = models.post("Medicine", "Medicine is great", members_instances[1].id)
    sleep(5)
    post4 = models.post("Architecture", "Spectacular art", members_instances[1].id)
    post5 = models.post("Astronomy", "Space is awesome", members_instances[1].id)

    post6 = models.post("Geology", "Earth is our friend", members_instances[2].id)
    post7 = models.post("ComputerSci", "Our passion", members_instances[2].id)
    sleep(5)
    post8 = models.post("Algorithms", "Yeah, more of that", members_instances[2].id)
    post9 = models.post("Operating Systems", "Ewww", members_instances[2].id)

    print(post1)
    print(post2)
    print(post3)
    print("=" * 30)

    return post1, post2, post3, post4, post5, post6, post7, post8, post9


def store_should_add_posts(posts_instances, post_store):
    for member in posts_instances:
        post_store.add(member)


def store_should_get_members_with_posts(member_store, post_store):
    members_with_posts = member_store.get_members_with_posts(post_store.get_all())

    for member_with_posts in members_with_posts:
        print(f"{member_with_posts} has posts:")
        for post in member_with_posts.posts:
            print(f"\t{post}")

        print("=" * 10)


def store_should_get_top_two(member_store, post_store):
    top_two_members = member_store.get_top_two(post_store.get_all())

    for member_with_posts in top_two_members:
        print(f"{member_with_posts} has posts:")
        for post in member_with_posts.posts:
            print(f"\t{post}")

def store_should_get_posts_by_date(post_store):
    for post in post_store.get_posts_by_date():
        print(post, post.date ,'\n')


# ====== Test Members ====================
members_instances = create_members()
member1, member2, member3 = members_instances

add_models_to_store(members_instances, member_store)

#print_all_members(member_store)

#test_update(member_store, member3)

#test_get_by_name(member_store, 'Mohammed')

# ====== Test Posts ====================
posts_instances = create_posts(members_instances)
post1, post2, post3, post4, post5, post6, post7, post8, post9 = posts_instances

store_should_add_posts(posts_instances, post_store)

store_should_get_members_with_posts(member_store, post_store)

store_should_get_top_two(member_store, post_store)

store_should_get_posts_by_date

