__author__ = 'joe'

import requests
import click
from .random import get_random_id


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
			  help='The person to greet.')
def add_comment(self, post_id, title, body):
	# This method will make an API call to add a comment to a given post
	self.post_id = get_random_id()

	data = {"id": post_id, "title": title, "body": body}
	try:
		resp = requests.post('/comments', json=data)
		if resp.status_code == 200:
			# this means the post was made successfully
			return {"content": resp.content,
					"message": "post added successfully"}
		else:
			return {"content": resp.content,
					"message": "failed to add a comment"}

	except requests.exceptions.RequestException as e:
		return {"content": None, "message": "Error: {}".format(e)}
