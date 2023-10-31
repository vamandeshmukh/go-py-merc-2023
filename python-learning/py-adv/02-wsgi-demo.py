
print('start')

def hello_wsgi_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    return [b"Hello world!"]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('', 8000, hello_wsgi_app)
    print("Serving on port 8000...")
    httpd.serve_forever()

print('end')
