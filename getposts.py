import click
import requests

@click.command()
@click.option("view_feed")
def get_posts(view_feed):
    resp = requests.get('https://jsonplaceholder.typicode.com/posts')
    if resp.status_code == 200:
         for post in resp.json():
             print("" * 20)
             print(post['title'])
             print("" * 20)
             print(post['body'])