from app import create_app, db
from modelos.user import User

app = create_app()

with app.app_context():
    admin = User(
        username="admin",
        role="ADMIN_GENERAL"
    )
    admin.set_password("admin1234")
    db.session.add(admin)
    db.session.commit()
    print(">>> Usuario admin creado correctamente")
