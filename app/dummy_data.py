from app import models

dummy_members = [
    models.member("Mohammed", 20),
    models.member("Mohammed", 22),
    models.member("Abdo", 25),
]

dummy_posts = [
    models.post("Agriculture", "Agriculture is amazing", dummy_members[0].id),
    models.post("Engineering", "I love engineering", dummy_members[0].id),

    models.post("Medicine", "Medicine is great", dummy_members[1].id),
    models.post("Architecture", "Spectacular art", dummy_members[1].id),
    models.post("Astronomy", "Space is awesome", dummy_members[1].id),

    models.post("Geology", "Earth is our friend", dummy_members[2].id),
    models.post("ComputerSci", "Our passion", dummy_members[2].id),
    models.post("Algorithms", "Yeah, more of that", dummy_members[2].id),
    models.post("Operating Systems", "Ewww", dummy_members[2].id),
]

def seed_stores(member_store, post_store):
    for member in dummy_members:
        member_store.add(member)

    for post in dummy_posts:
        post_store.add(post)
