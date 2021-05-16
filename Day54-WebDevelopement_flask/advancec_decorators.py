class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_user(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])

    return wrapper


@is_authenticated_user
def create_blog_post(user: User):
    print(f"this blog post of {user.name}'s ")


user: User = User("Yogesh")
user.is_logged_in = True

create_blog_post(user)
