from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate(db=db)

def init_ext(app):
    migrate.init_app(app)

    db.init_app(app)

    sess = Session()

    sess.init_app(app)
