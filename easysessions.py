from bottle import run, route, request, response
import random

sesje = {}

def session_check():
    session_number = request.get_cookie('sesja', secret=32167)
    if session_number in sesje:
        return sesje[session_number]
    else:
        return False

def session_start(username):
    session_number = random.randint(10000000000, 9999999999999999)
    sesje[session_number] = username
    response.set_cookie('sesja', session_number, secret=32167, path='/')

def session_end():
    session_number = request.get_cookie('sesja', secret=32167)
    sesje.pop(session_number)
    response.delete_cookie('sesja')

@route('/')
def index():
    if session_check():
        imie = session_check()
        return imie
    else:
        return ':0'

@route('/login/<imie>')
def login(imie):
    session_start(imie)
    return 'ok %s, sesja trwa' % imie

@route('/logout')
def logout():
    try:
        session_end()
        return 'wylogowano'
    except:
        return 'nie jestes zalogowany'



run(debug=True)

