import os
import sqlite3

# Delete old database
db_path = 'instance/app.db'

if os.path.exists(db_path):
    os.remove(db_path)
    print("Old database deleted")

# Import app
from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():

    # Create tables
    db.create_all()
    print("✅ Tables created")

    # Check admin exists
    existing_admin = User.query.filter_by(
        email='admin@lifelink.com'
    ).first()

    if not existing_admin:

        admin = User(
            email='admin@lifelink.com',
            first_name='Super',
            last_name='Admin',
            user_type='admin',
            is_active=True
        )

        admin.set_password('Admin@123')

        db.session.add(admin)
        db.session.commit()

        print("✅ Admin created")

    else:
        print("⚠️ Admin already exists")

    print("\n" + "=" * 50)
    print("ADMIN LOGIN:")
    print("Email: admin@lifelink.com")
    print("Password: Admin@123")
    print("=" * 50)

print("\n✅ Setup complete! Run: python run.py")