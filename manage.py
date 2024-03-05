from flask_script import Manager, Shell
from flask_migrate import migrate, upgrade, init, Migrate

from app import create_app, db
from app.models import Cell

app = create_app('devConf')
manager = Manager(app)
migration = Migrate(app, db)

def shell_context():
    return dict(db=db, Cell=Cell)

def migration_context():
    return dict(i=init, u=upgrade, m=migrate)

manager.add_command('shell', Shell(make_context=shell_context))
manager.add_command('db', Shell(make_context=migration_context))

if __name__ == '__main__':
    manager.run()