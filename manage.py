from flask.cli import FlaskGroup
from src import app, db, User

cli = FlaskGroup(app)

def seed_users(db):
    db.session.add(User(username="farooq", email="farooq@teqniqly.com"))
    db.session.add(User(username="bubba", email="bubba@gmail.com"))

@cli.command("init-db")
def init_db():
    db.drop_all()
    db.create_all()
    seed_users(db)
    db.session.commit()

if __name__ == "__main__":
    cli()