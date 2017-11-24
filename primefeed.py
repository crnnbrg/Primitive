import click 
import requests
import sys


@click.command()
@click.option("--view_feed", is_flag=True, help="View posts.")

def cli(view_feed):
    if view_feed:
        resp = requests.get('https://jsonplaceholder.typicode.com/posts')
        if resp.status_code == 200:
            for post in resp.json():
                print("" * 20)
                print("Title: " + post['title'])
                print("" * 20)
                print("Body " + post['body'])

@click.command()
@click.argument("title")
@click.argument("body")
def cli(title, body):
    """Submit a new post."""
    post_title = sys.argv[1]
    post_body = sys.argv[2]
    data = {
        "title": post_title,
        "body": post_body
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", data=data)
    print(response.status_code)
