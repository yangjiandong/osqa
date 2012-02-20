from django.db import connection, models

class MY_UTIL():
    '''
    Its pretty clean and nice way to define stored procedures inside the class, especially models.py 
    (I hope someone will write a automatic generation for all stored procedure calls soon.)
    '''
    def log_mesage(self, control_in, message_in):
        cursor = conection.cursor()
        ret = cursor.callproc("db_stproc", (control_in, message_in))#call procedure
        cursor.close()
        return ret
#use
#my_util = MY_UTIL()
#ret = my_util.log_message(request.POST['email'], request.POST['subject'])    
    
def call_an_sp(self, var):
    cursor = connection.cursor()
    cursor.callproc("fn_sp_name", (var,))
    return self.fn_generic(cursor)

def fn_generic(self, cursor):
    msg = cursor.fetchone()[0]
    cursor.execute('FETCH ALL IN "%s"' % msg)
    thing = create_dict_from_cursor(cursor)
    cursor.close()
    return thing

def create_dict_from_cursor(cursor):
    rows = cursor.fetchall()
    # DEBUG settings (used to) affect what gets returned. 
    if DEBUG:
        desc = [item[0] for item in cursor.cursor.description]
    else:
        desc = [item[0] for item in cursor.description]
    return [dict(zip(desc, item)) for item in rows]

#https://docs.djangoproject.com/en/dev/topics/db/sql/
def my_custom_sql():
    from django.db import connection, transaction
    cursor = connection.cursor()

    # Data modifying operation - commit required
    cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
    transaction.commit_unless_managed()

    # Data retrieval operation - no commit required
    cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
    row = cursor.fetchone()

    return row
   
#If you are using more than one database you can use django.db.connections to obtain the connection (and cursor) for a specific database. django.db.connections is a dictionary-like object that allows you to retrieve a specific connection using its alias:
#
#from django.db import connections
#cursor = connections['my_db_alias'].cursor()
## Your code here...
#transaction.commit_unless_managed(using='my_db_alias')    

#By default, the Python DB API will return results without their field names, which means you end up with a list of values, rather than a dict. At a small performance cost, you can return results as a dict by using something like this:
#
#def dictfetchall(cursor):
#    "Returns all rows from a cursor as a dict"
#    desc = cursor.description
#    return [
#        dict(zip([col[0] for col in desc], row))
#        for row in cursor.fetchall()
#    ]
#Here is an example of the difference between the two:
#
#>>> cursor.execute("SELECT id, parent_id from test LIMIT 2");
#>>> cursor.fetchall()
#((54360982L, None), (54360880L, None))
#
#>>> cursor.execute("SELECT id, parent_id from test LIMIT 2");
#>>> dictfetchall(cursor)
#[{'parent_id': None, 'id': 54360982L}, {'parent_id': None, 'id': 54360880L}]
