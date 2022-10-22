from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False,unique=True) 
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    content = db.Column(db.String(500), nullable=False) 


    @classmethod
    def create(cls, title,content):
            post = Post(title=title, content=content)
            return post.save()

    def save(self):
            try:
                    db.session.add(self)
                    db.session.commit()

                    return self
            except:
                    return False

    def json(self):
            return {
                'id': self.id,
                'tite': self.title,
                'content':self.content,
                'created_at': self.created_at
            }

    def update(self):
            self.save()

    def delete(self):
            try:
                    db.session.delete(self)
                    db.session.commit()

                    return True
            except:
                    return False
