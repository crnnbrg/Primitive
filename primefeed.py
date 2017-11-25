import click
import requests
import sys


@click.group()
def cli():
    pass


@cli.command()
def view_feed():
    """View posts from the feed."""
    resp = requests.get('https://jsonplaceholder.typicode.com/posts')
    if resp.status_code == 200:
        for post in resp.json():
            click.echo("" * 20)
            click.echo("Title: " + post['title'])
            click.echo("" * 20)
            click.echo("Body " + post['body'])


@cli.command()
@click.argument("title")
@click.argument("body")
def post(title, body):
    """Submit a new post to the feed."""
    post_title = sys.argv[1]
    post_body = sys.argv[2]
    data = {
        "title": post_title,
        "body": post_body
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", data=data)
    click.echo("Response: " + str(response.status_code))
    click.echo(data)
