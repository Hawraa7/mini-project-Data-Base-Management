import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL", 'postgresql://neondb_owner:npg_q8iGc4HrQCXj@ep-steep-dust-a2sen6ew.eu-central-1.aws.neon.tech/patch_lash_truce_629825')
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri


db = SQLAlchemy(app)

from taskmanager import routes  # noqa
