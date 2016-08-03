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
    try:
        session_number = request.get_cookie('sesja', secret=32167)
        sesje.pop(session_number)
        response.delete_cookie('sesja')
    except:
        pass
