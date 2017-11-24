from flask import Flask, jsonify

app = Flask(__name__)


comment = input("Stuff: ")
@app.route('/post/<postid>/comment/<commentid>' methods=['GET'])
def view_post():
	jsonify comment



















if __name__== '__main__':
    app.run(debug=True)
