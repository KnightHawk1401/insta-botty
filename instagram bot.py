

import random
from instapy import InstaPy
from instapy.util import smart_run

# login credentials
insta_username = 'kevlxr'
insta_password = 'rene7465'

dont_likes = ['gay']

friends = ['']

like_tag_list = ['vegan', 'veganfoodshare', 'veganfood', 'whatveganseat',
                 'veganfoodie', 'veganism', 'govegan',
                 'veganism', 'vegansofig', 'veganfoodshare', 'veganfit',
                 'veggies' , 'sex', 'nude', 'naked', 'beef', 'pork', 'seafood',
              'egg', 'chicken', 'cheese', 'sausage', 'lobster',
              'fisch', 'schwein', 'lamm', 'rind', 'kuh', 'meeresfrüchte',
              'schaf', 'ziege', 'hummer', 'yoghurt', 'joghurt', 'dairy',
              'meal', 'food', 'eat', 'pancake', 'cake', 'dessert',
              'protein', 'essen', 'mahl', 'breakfast', 'lunch',
              'dinner', 'turkey', 'truthahn', 'plate', 'bacon',
              'sushi', 'burger', 'salmon', 'shrimp', 'steak',
              'schnitzel', 'goat', 'oxtail', 'mayo', 'fur', 'leather',
              'cream', 'hunt', 'gun', 'shoot', 'slaughter', 'pussy',
              'breakfast', 'dinner', 'lunch' , 'memes' , 'wholesome' , 'fortnite' , 'instagram' , 'dankmemes' , 'likeforfollow' , 'followforfollow' , 'trending' ,'like' , 'follow' , 'trump' , 'donaldtrump' , 'fortnite' , 'pubg' , 'minecraft']

# prevent posts that contain some plantbased meat from being skipped
ignore_list = ['vegan', 'veggie', 'plantbased']

accounts = ['accounts with similar content']

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)

with smart_run(session):
    # settings
    session.set_relationship_bounds(enabled=True,
                                    max_followers=100000)

    session.set_dont_include(friends)
    session.set_dont_like(dont_likes)
    session.set_ignore_if_contains(ignore_list)

    session.set_user_interact(amount=15, randomize=True, percentage=100)
    session.set_do_follow(enabled=True, percentage=100)
    session.set_do_like(enabled=True, percentage=100)

    # activity
    session.like_by_tags(random.sample(like_tag_list, 75),
                         amount=random.randint(50, 100), interact=True)

    session.unfollow_users(amount=random.randint(75, 150),
                           InstapyFollowed=(True, "all"), style="FIFO",
unfollow_after=90 * 60 * 60, sleep_delay=501)
