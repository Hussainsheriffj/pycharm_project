from user import User
from post import Post
user_1 = User("nn@gg.com", "sheriff", "pwd", "cloud engineer")
user_1.get_user_info()

user_1.change_job_title("devops trainer")
user_1.get_user_info()

user_2 = User("aa@bb.com", "hussain", "pwd2", "cloud dev")
user_2.get_user_info()

new_post = Post("On a secret mission today", user_2.name)
new_post.get_post_info()