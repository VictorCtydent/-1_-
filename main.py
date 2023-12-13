from flask import Flask
from routes.tax_fetch import tax_fetch_blueprint
from routes.tax_post import tax_post_blueprint

app = Flask(__name__)

app.register_blueprint(tax_fetch_blueprint)
app.register_blueprint(tax_post_blueprint)

if __name__ == '__main__':
    app.run()

