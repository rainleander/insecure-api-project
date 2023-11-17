from app import app, db, User

# Set up an application context
with app.app_context():
    db.create_all()

    # Add sample users
    db.session.add(User(username='user1', password='password1', is_admin=False))
    db.session.add(User(username='admin', password='adminpass', is_admin=True))

    db.session.commit()

