def create(Model, db, data):
    model = Model(**data)
    db.session.add(model)
    db.session.commit()

def update(Model, db, data, id):
    model = Model.query.get(int(id))
    for k, v in data.items():
        print(k, v)
        exec(f"model.{k}=\"\"\"{v}\"\"\"")
    db.session.add(model)
    db.session.commit()

def delete(Model, db, id):
    model = Model.query.get(int(id))
    db.session.delete(model)
    db.session.commit()