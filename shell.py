import sae
from sae.ext.shell import ShellMiddleware

def urisaok(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ["Hello, world!"]

application = sae.create_wsgi_app(ShellMiddleware(urisaok, '1q2w3e4r'))
