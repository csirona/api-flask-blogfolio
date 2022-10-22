from flask import Flask, request,jsonify
import json
from config import config

from flask_cors import CORS
from models import db, Post

def create_app(enviroment):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(enviroment)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app


env = config['development']
app = create_app(env)

@app.route('/api/v1/posts', methods=['GET'])
def get_posts():
    posts = [post.json() for post in Post.query.all()]
    return jsonify({'posts': posts})


@app.route('/api/v1/posts/<id>', methods=['GET'])
def get_post(id):
    post = Post.query.filter_by(id=id).first()
    if post is None:
        return jsonify({'message': 'Post does not exists'}), 404

    return jsonify({'post': post.json()})


@app.route('/api/v1/posts/', methods=['POST'])
def create_post():
    r = request.get_json(force=True)

    jsonString = json.dumps(r)
    p= json.loads(jsonString)

    if p[0]['title'] is None:
        return jsonify({'message': 'Bad request'}), 400
    
    if Post.query.filter_by(title=p[0]['title'] ).first():
        return jsonify({'message': 'Post title is already taken'}), 404

    post = Post.create(p[0]['title'],p[0]['content'])

    return jsonify({'post': post.json()})


@app.route('/api/v1/posts/<id>', methods=['PUT'])
def update_post(id):
    post = Post.query.filter_by(id=id).first()


    if post is None:
        return jsonify({'message': 'Post does not exists'}), 404

    r = request.get_json(force=True)
    jsonString = json.dumps(r)
    p= json.loads(jsonString)

    if p[0]['title'] is None:
        return jsonify({'message': 'Bad request'}), 400

    post.title = p[0]['title']
    post.content = p[0]['content']

    post.update()

    return jsonify({'post': post.json()})


@app.route('/api/v1/posts/<id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.filter_by(id=id).first()
    if post is None:
        return jsonify({'message': 'Post does not exists'}), 404

    post.delete()

    return jsonify({'post': post.json() })

if __name__ == '__main__':
    app.run(debug=True)
