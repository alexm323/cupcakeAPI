"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


# class SampleDepartment(db.Model):
#     """Department Model"""

#     __tablename__ = "departments"

#     dept_code = db.Column(db.Text, primary_key=True)
#     dept_name = db.Column(db.Text, nullable=False, unique=True)
#     phone = db.Column(db.Text)

#     def __repr__(self):
#         return f"<Department {self.dept_code} {self.dept_name} {self.phone} >"

class Cupcake(db.Model):
    """Cupcake Model"""
