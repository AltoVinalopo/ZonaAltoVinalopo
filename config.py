import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "cambia-esto-por-un-secreto-largo-y-seguro")

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(BASE_DIR, "coordinacion.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
