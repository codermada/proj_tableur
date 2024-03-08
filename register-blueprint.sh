echo """
from app.$1 import $1 as $1_blueprint
    app.register_blueprint($1_blueprint, url_prefix='/$1')
"""