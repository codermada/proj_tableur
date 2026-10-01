from flask_script import Manager, Shell
from flask_migrate import migrate, upgrade, init, Migrate
from flask_restful import Api


from app import create_app, db
from app.models import Formula, Collection, Table, Cell

app = create_app('devConf')
manager = Manager(app)
migration = Migrate(app, db)
api = Api(app)

from api.resources import TableResource, CellColumnResource, CellRowResource
from utilities import to2D, reverse
api.add_resource(TableResource, "/api/table-cells")
api.add_resource(CellColumnResource, "/api/table-column")
api.add_resource(CellRowResource, "/api/table-row")
app.jinja_env.filters['to2D'] = to2D
app.jinja_env.filters['reverse'] = reverse

def shell_context():
    return dict(db=db, Formula=Formula, Collection=Collection, Table=Table, Cell=Cell)

def migration_context():
    return dict(i=init, u=upgrade, m=migrate)

manager.add_command('shell', Shell(make_context=shell_context))
manager.add_command('db', Shell(make_context=migration_context))


if __name__ == '__main__':
    manager.run()