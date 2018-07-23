import functools
import xmlrpclib

HOST = 'http://odoo.local'
DB = '**'
USER = '**'
PASS = '**'
ROOT = '{host}/xmlrpc/'.format(host=HOST)

# Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB, USER, PASS)
print("Logged in as {} (uid:{})".format(USER, uid))

call = functools.partial(
    xmlrpclib.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS
)

# Read sessions
sessions = call('openacademy.session', 'search_read', [], ['name', 'seats'])
for session in sessions:
    print("Session {} ({} seats)".format(session['name'], session['seats']))

# Create new session
course_id = call('openacademy.course', 'search', [('name', 'ilike', 'Course 1')])[0]
session_id = call('openacademy.session', 'create', {
    'name': 'My session',
    'course_id': course_id,
})
print("Session {} created".format(session_id))
