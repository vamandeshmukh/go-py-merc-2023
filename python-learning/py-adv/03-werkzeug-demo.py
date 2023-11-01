from werkzeug.wrappers import Request, Response

print('start')

def application(environ, start_response):
    request = Request(environ)
    print('hello')
    response = Response("Hello world!", content_type='text/plain')
    return response(environ, start_response)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    print('started')
    run_simple('localhost', 9999, application)

print('end')
