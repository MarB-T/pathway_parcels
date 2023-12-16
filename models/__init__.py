#!/usr/bin/python3
from os import getenv
'''from web_flask.pathway import login_manager'''

storage_t = getenv('STORAGE_TYPE')

if storage_t == 'db':
    '''from models.engine.file_storage import FileStorage
    storage = FileStorage()'''
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

    '''@login_manager.user_loader
    def load_user(user_id):
        return storage.get(User, user_id)'''


else:
    '''from models.engine.db_storage import DBStorage
    storage = DBStorage()'''
    from models.engine.file_storage import FileStorage
    storage = FileStorage()


storage.reload()
