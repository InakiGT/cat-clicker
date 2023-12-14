from flask import Flask
from controllers.cat_controller import CatController

app = Flask(__name__)

app.add_url_rule('/cat', view_func=CatController.index, methods=['GET', 'PUT'])

if __name__ == '__main__':
    app.run(debug=True)