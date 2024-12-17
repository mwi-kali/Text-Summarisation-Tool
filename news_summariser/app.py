from app import create_app
from database.models import db

app = create_app()

if __name__ == "__main__":
    # Initialize the database schema
    with app.app_context():
        db.create_all()
        print("Database tables created successfully.")
    app.run(debug=True)