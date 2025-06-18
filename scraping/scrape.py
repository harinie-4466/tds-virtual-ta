import requests
from bs4 import BeautifulSoup
import json
import csv

def scrape_discourse():
    base_url = "https://discourse.onlinedegree.iitm.ac.in"
    topic_ids = [155939]  # Add more topic IDs here
    posts = []
    for topic_id in topic_ids:
        url = f"{base_url}/t/{topic_id}.json"
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            for post in data['post_stream']['posts']:
                posts.append({
                    "topic_id": topic_id,
                    "content": post['cooked'],
                    "username": post['username']
                })
    return posts

if __name__ == "__main__":
    data = scrape_discourse()

    # Save as JSON
    with open("discourse_posts.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Save as CSV
    with open("discourse_posts.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["topic_id", "content", "username"])
        writer.writeheader()
        writer.writerows(data)

    print("Data saved as both JSON and CSV.")

