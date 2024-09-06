import instaloader
import csv

L = instaloader.Instaloader()

# Login (optional)
# L.login("your_username", "your_password")

# Load profile
profile = instaloader.Profile.from_username(L.context, "ndrfindia")

with open('instagram_posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Caption', 'URL']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for post in profile.get_posts():
        writer.writerow({'Caption': post.caption, 'URL': post.url})
