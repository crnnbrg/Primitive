import click
import requests


@click.command()
@click.argument('post_id')

def view_post(post_id):
	response = (requests='https://jsonplaceholder.typicode.com/comments?postId='+f(post_id))
	click.echo(response)








