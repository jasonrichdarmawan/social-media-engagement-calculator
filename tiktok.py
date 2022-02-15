import sys
import time
from TikTokApi import TikTokApi

api = TikTokApi.get_instance()

postscount = 20

tiktoks = api.by_username(sys.argv[2], count=postscount, custom_verifyFp=sys.argv[1])

num_followers = tiktoks[0]['authorStats']['followerCount']
total_num_likes = 0
total_num_comments = 0
total_num_shares = 0
total_num_views = 0
total_num_posts = 0

counter = 0
for post in tiktoks:
  if (counter >= postscount):
    break
  stats = post['stats']
  total_num_likes += stats['diggCount']
  total_num_comments += stats['commentCount']
  total_num_shares += stats['shareCount']
  total_num_views += stats['playCount']
  total_num_posts += 1
  counter += 1

avg_likes = total_num_likes / total_num_posts
avg_comments = total_num_comments / total_num_posts
avg_shares = total_num_shares / total_num_posts
avg_views = total_num_views / total_num_posts

er = (total_num_likes + total_num_comments + total_num_shares) / total_num_views

print(f"avg. likes: {avg_likes:,.0f}, avg. comments: {avg_comments:,.0f}, avg. shares: {avg_shares:,.0f}, avg. views: {avg_views:,.0f}, views: {total_num_views:,.0f}, followers: {num_followers:,.0f}, er: {er:.2%}")