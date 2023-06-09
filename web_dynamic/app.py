from web_dynamic.pages import page_views
from web_dynamic.api import api_views
from os import environ
from models import storage
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.json.compact
app.register_blueprint(page_views)
app.register_blueprint(api_views)

cors = CORS(app, resources={r"/api/v1/*": {"origins": "web-02.reinhardservices.tech"}})
app.secret_key = 'my_secret_key'



@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)

def return_app():
    return app

if __name__ == "__main__":
    """ Main Function """
    app.run()
