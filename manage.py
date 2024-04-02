from flask_script import Manager, Shell
from flask_migrate import migrate, upgrade, init, Migrate

from app import create_app, db
from app.models import Formula, Table

app = create_app('devConf')
manager = Manager(app)
migration = Migrate(app, db)

@app.template_filter('to2D')
def to2D(the_list, nb_col):
    result = []
    row = []
    j = 0
    nb_col = int(nb_col)
    for element in the_list:
        row.append(element)
        j += 1
        if j == nb_col:
            result.append(row)
            row = []
            j = 0
    return result

@app.template_filter('reverse')
def reverse(the_list):
    result = the_list[::-1]
    return result

def shell_context():
    return dict(db=db, Formula=Formula, Table=Table)

def migration_context():
    return dict(i=init, u=upgrade, m=migrate)

manager.add_command('shell', Shell(make_context=shell_context))
manager.add_command('db', Shell(make_context=migration_context))

if __name__ == '__main__':
    manager.run()