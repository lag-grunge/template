from tinydb import TinyDB, Query
from value_type import get_type


def _get_database():
    db = TinyDB('./data/db.json')
    return db


db = _get_database()


def get_form(document):
    form = {}

    if 'name' in document:
        form['name'] = document['name']
    for key in document:
        if key == 'name':
            continue
        form[key] = get_type(document[key])
    return form


def _insert(db, document):
    form = get_form(document)
    db.insert(form)
    return form


def _update(db, document):
    form = get_form(document)
    q = Query()
    db.update(form, getattr(q, 'name') == form['name'])
    return form


def insert_db(document):
    if not 'name' in document:
        return f"document without name for Template"
        
    q = Query()
    r = db.search(q.name == document['name'])
    if len(r) > 0:
        return f"Template \"{document['name']}\" exists in collection\n"

    form = _insert(db, document)
    return f"Template {form} inserted in collection from {document}\n"
    

def read_db(document):
    q = Query()
    form = get_form(document)

    res = db.search(q.fragment(form))
    if not res:
        if 'name' in form:
            # убрать имя если есть и нужно вывести только поля (подходящего шаблона нет)
            form.pop('name', None)
        return form
    elif len(res) > 1:
        # выбрать результат по макс числу полей
        return max(res, key=lambda x: len(x.keys()))['name']
    else: 
        return res[0]['name'] + '\n'


def update_db(document):
    if not 'name' in document:
        return f"document without name for Template"
        
    q = Query()
    r = db.search(q.name == document['name'])
    if len(r) == 0:
        form = _insert(db, document)
        return f"Template {form} inserted in collection from {document}\n"
    elif len(r) == 1:
        form = _update(db, document)
        return f"Template updated to {form} in collection from {document}\n"
    else:
        raise Exception(f'Many templates with name {document["name"]}')