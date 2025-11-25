import os

class Config:
    SECRET_KEY = "SUPER-CLAVE-VIP-2025-COORDINACION-VOX-ALICANTE"

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://coordinacion_user:ClaveSegura123!@localhost/coordinacion"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = os.environ.get(
        "UPLOAD_FOLDER",
        os.path.join(os.path.dirname(__file__), "uploads")
    )
