from server.models.guest import Guest
from server.models.appearance import Appearance
from server.models.episode import Episode
from server import db

def seed():
    db.create_all()

    guests = [
        Guest(name='John', age=25, gender='Male'),
        Guest(name='Jane', age=30, gender='Female'),
        Guest(name='Bob', age=35, gender='Male'),
        Guest(name='Alice', age=28, gender='Female'),
    ]

    for guest in guests:
        db.session.add(guest)

    appearances = [
        Appearance(name='Blue', hex_code='#0000ff'),
        Appearance(name='Red', hex_code='#ff0000'),
        Appearance(name='Green', hex_code='#00ff00'),
    ]

    for appearance in appearances:
        db.session.add(appearance)

    episodes = [
        Episode(title='Episode 1', description='This is episode 1', air_date='2020-01-01'),
        Episode(title='Episode 2', description='This is episode 2', air_date='2020-01-02'),
        Episode(title='Episode 3', description='This is episode 3', air_date='2020-01-03'),
    ]

    for episode in episodes:
        db.session.add(episode)

    db.session.commit()

if __name__ == '__main__':
    seed()
