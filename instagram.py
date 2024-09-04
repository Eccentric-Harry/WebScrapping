import instaloader
from datetime import datetime
import csv
import time

L = instaloader.Instaloader()


USERNAME = "_harinadh___"  
PASSWORD = ""  
L.login(USERNAME, PASSWORD)


csv_filename = 'instagram_profile_posts.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Post URL', 'Username', 'Caption', 'Date', 'Likes', 'Comments'])

def scrape_profile_posts(profile_name):
    profile = instaloader.Profile.from_username(L.context, profile_name)

    post_count = 0
    for post in profile.get_posts():
        post_count += 1
        print(f"{datetime.now()} - Scraping post {post_count}...")

        post_url = f"https://www.instagram.com/p/{post.shortcode}/"
        username = post.owner_username
        caption = post.caption
        post_date = post.date
        likes = post.likes
        comments = post.comments


        with open(csv_filename, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([post_url, username, caption, post_date, likes, comments])


        time.sleep(2)

    print(f"{datetime.now()} - Finished scraping {post_count} posts for profile: {profile_name}")

if __name__ == "__main__":
    try:
        profile_name = "ndrfindia"
        scrape_profile_posts(profile_name)
    except Exception as e:
        print(f"An error occurred: {e}")
