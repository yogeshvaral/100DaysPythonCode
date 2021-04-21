fruits = ["Apple","Pear","Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as error:
        print(f" {error}")
    else:
        print(fruit)

make_pie(1)

# Challenge 2

facebook_posts = [
    {'Likes':21,'Comments':2},
    {'Likes':13,'Comments':2},
    {'Likes':31,'Comments':8,'share':3},
    {'share':21,'Comments':2},
    {'share':12,'Comments':2},
    {'Likes':19,'Comments':2}
]

total_likes = 0;
for post in facebook_posts:
    try:
        likes = post['Likes']
    except KeyError:
        total_likes = total_likes + 0
    else:
        total_likes = total_likes + likes

print(total_likes)