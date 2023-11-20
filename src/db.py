from tinydb import TinyDB, Query
from src.value_type import get_type


def _get_database():
    db = TinyDB('db.json')
    return db


db = _get_database()


def get_form(document):
    form = {}
    document = dict(document)
    document.pop('name', None)

    for key in document:
        form[key] = get_type(document[key])
    return form


def _insert(db, document):
    form = get_form(document)
    db.insert(form)
    return form


def _update(db, document):
    form = get_form(document)
    q = Query()
    db.update(form, getattr(q, 'name') == document['name'])
    return form


def insert_db(document):
    if not 'name' in document:
        return f"document without name for Template"
        
    q = Query()
    r = db.search(q.name == document['name'])
    if len(r) > 0:
        return f"Template \"{document['name']}\" exists in collection"

    form = _insert(db, document)
    return f"Template {form} inserted in collection from {document}"
    

def read_db(document):
    q = Query()
    form = get_form(document)

    res = db.search(q.fragment(form))
    return res[0]['name']


def update_db(document):
    if not 'name' in document:
        return f"document without name for Template"
        
    q = Query()
    r = db.search(q.name == document['name'])
    if len(r) == 0:
        form = _insert(db, document)
        return f"Template {form} inserted in collection from {document}"
    elif len(r) == 1:
        form = _update(db, document)
        return f"Template updated to {form} in collection from {document}"
    else:
        raise Exception(f'Many templates with name {document["name"]}')