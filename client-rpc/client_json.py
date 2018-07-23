import json
import random
import urllib2

HOST = 'http://odoo.local'
DB = '**'
USER = '**'
PASS = '**'
ROOT = '{host}/jsonrpc/'.format(host=HOST)


def json_rpc(url, method, params):
    data = {
        'jsonrpc': '2.0',
        'method': method,
        'params': params,
        'id': random.randint(0, 100000000)
    }
    req = urllib2.Request(url=url, data=json.dumps(data), headers={
        "Content-Type": "application/json",
    })
    reply = json.load(urllib2.urlopen(req))
    if reply.get("error"):
        raise Exception(reply["error"])
    return reply["result"]


def call(url, service, method, *args):
    return json_rpc(url, "call", {"service": service, "method": method, "args": args})


# Login
uid = call(ROOT, 'common', 'login', DB, USER, PASS)
print("Logged in as {} (uid:{})".format(USER, uid))

# Read sessions
sessions = call(ROOT, 'object', 'execute', DB, uid, PASS, 'openacademy.session', 'search_read')
for session in sessions:
    print("Session {} ({} seats)".format(session['name'], session['seats']))

# Create new session
course_id = call(
    ROOT, 'object', 'execute', DB, uid, PASS, 'openacademy.course', 'search', [('name', 'ilike', 'Course 0')])[0]
session_id = call(
    ROOT, 'object', 'execute', DB, uid, PASS, 'openacademy.session', 'create', {
        'name': 'My session 2',
        'course_id': course_id,
    })
print("Session {} created".format(session_id))
