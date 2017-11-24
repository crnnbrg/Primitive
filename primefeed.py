import click 
import requests
import sys

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

