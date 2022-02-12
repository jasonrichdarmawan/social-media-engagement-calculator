import sys
from instaloader import Instaloader, Profile, exceptions
loader = Instaloader()

if(len(sys.argv) > 2):
  loader.load_session_from_file(sys.argv[1])

  if loader.test_login is None:
    print("logging in")
    loader.login(sys.argv[1], sys.argv[2])
    loader.save_session_to_file()

try:
  profile = Profile.from_username(loader.context, sys.argv[3] if len(sys.argv) > 2 else sys.argv[1])
except exceptions.ProfileNotExistsException:
  print("This username does not exist.")
  exit()

num_followers = profile.followers
total_num_likes = 0
total_num_comments = 0
total_num_posts = 0

counter = 0
postscount = 20
for post in profile.get_posts():
  if(counter >= postscount):
    break
  total_num_likes += post.likes
  total_num_comments += post.comments
  total_num_posts += 1
  counter=counter+1

avg_likes = total_num_likes / total_num_posts
avg_comments = total_num_comments / total_num_posts
er = (avg_comments + avg_likes) / num_followers * 100

print("avg. likes: %d, avg. comments: %d, followers: %d, er: %.2f%%" % (avg_likes, avg_comments, num_followers, er))