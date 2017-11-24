
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
    
@click.command()
@click.argument('post_id')

def view_post(post_id):
	response = (requests='https://jsonplaceholder.typicode.com/comments?postId='+f(post_id))
	click.echo(response)
