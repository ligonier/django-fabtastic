"""
Various database-related utility functions.
"""
import datetime
from django.conf import settings

def get_db_setting(db_setting, db_alias='default'):
    """
    Gets a database setting from settings.py.
    
    db_setting: (str) One of the database setting names.
        For example, 'NAME', 'PORT', 'HOST'.
    db_alias: (str) In the case of settings in Django 1.2 format, get settings
                    for a DB other than the default.
    """
    return settings.DATABASES[db_alias].get(db_setting, '')
    
def get_db_setting_dict(db_alias='default'):
    """
    Returns a dict of DB settings, as per the Django 1.2 DATABASE settings.py
    dict. This can be used as a compatibility measure for Django 1.1 and
    earlier.
    """
    return {
        'ENGINE': get_db_setting('ENGINE', db_alias=db_alias),
        'NAME': get_db_setting('NAME', db_alias=db_alias),
        'HOST': get_db_setting('HOST', db_alias=db_alias),
        'PORT': get_db_setting('PORT', db_alias=db_alias),
        'USER': get_db_setting('USER', db_alias=db_alias),
        'PASSWORD': get_db_setting('PASSWORD', db_alias=db_alias),
    }
    
def get_db_dump_filename(db_alias='default'):
    """
    Returns a generic DB dump file name for use with backup/restore scripts.
    Fabric commands share this function with the management commands.
    """
    today = datetime.datetime.today()
    database_dict = get_db_setting_dict(db_alias)

    dump_filename = "%s-%s.sql.tar.bz2" %  (
        database_dict['NAME'], 
        today.strftime("%Y_%m_%d-%H%M"),
    )
    return dump_filename