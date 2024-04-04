from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database_name.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)


# from routes.farmers import farmers_bp
# from routes.products import products_bp

# Register blueprints
app.register_blueprint()
app.register_blueprint()

if __name__ == '__main__':
    app.run(debug=True)