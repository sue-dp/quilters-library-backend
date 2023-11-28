import sys

from db import db
from models.users import Users
from .user_demo_data import add_user_demo_data
from .org_demo_data import add_org_demo_data
from .role_demo_data import add_role_demo_data


def run_demo_data():
    user_query = db.session.query(Users).filter(Users.first_name == 'Sue').first()

    if len(sys.argv) > 1 and sys.argv[1] == 'demo-data':
        if user_query == None:
            print('Creating demo data...')
            add_user_demo_data()
            add_org_demo_data()
            add_role_demo_data()
        else:
            print('Demo data found.')