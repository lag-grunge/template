from functools import partial
import re
from datetime import datetime

def check_date(string):
    for fmt in ['%Y-%m-%d', '%d.%m.%Y']:
        try:
            datetime.strptime(string, fmt)
            return True
        except ValueError:
            pass
    return False

check_email = partial(re.match, pattern=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
check_phone = partial(re.match, pattern=r'^\+7 [0-9]{3,} [0-9]{3,} [0-9]{2,} [0-9]{2,}$')

TYPES = { 'email': check_email,
            'phone': check_phone,
            'date': check_date,
            'text': None
        }

def get_type(value):
    for _type in ['email', 'phone', 'date']:
        if TYPES[_type](string=value):
            return _type
    return 'text'
