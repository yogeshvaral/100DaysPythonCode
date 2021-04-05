

print("Hello Yogesh")
class User:
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    def follow(self,user):
        user.followers +=1
        self.following +=1


user1 = User(1,"Kaminee")
user2 = User(2,"Yogesh")
user1.follow(user2)
print(str(user1.followers) + "" + str(user1.following))
print(str(user2.followers) + "" +str(user2.following))

from DaySeventeen.data import question_data
from DaySeventeen.Question_model import Question

question_list = []
for entry in question_data:
    question_list.append(Question(entry.get("text"), entry.get("answer")))

for entry in question_list:
    print(entry.text+ entry.answer)



