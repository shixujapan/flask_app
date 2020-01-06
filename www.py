# ルーティング
from application import app
from controllers.index import index_page

from flask_debugtoolbar import DebugToolbarExtension
toolbar = DebugToolbarExtension( app )


from interceptors.Auth import *
from interceptors.errorHandler import *

app.register_blueprint(index_page, url_prefix = "/")