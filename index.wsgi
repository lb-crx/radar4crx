# -*- coding: utf-8 -*-
VERSION = "radar4crx v12.7.3"
import sae
#import urllib2 as urilib
from bottle import Bottle, request, template, static_file

app = Bottle()


class Borg():
    '''base http://blog.youxu.info/2010/04/29/borg
        - 单例式配置收集类
    '''
    __collective_mind = {}
    def __init__(self):
        self.__dict__ = self.__collective_mind
cfg = Borg()



@app.route('/static/:filename')
def server_static(filename):
    return static_file(filename, root='map')

@app.route('/')
def index():
    return template('index.tpl'
        )

@app.route('/radar', method='POST')
def radar():
    e = request.forms.easy
    f = request.forms.func
    a = request.forms.acti
    b = request.forms.beau
    pli = e+f+a+b
    
    return template('map.tpl'
        ,pli=pli
        ,ptotal="%d"%((int(e)+int(f)+int(a)+int(b))*100/20)
        ,easy=e
        ,func=f
        ,acti=a
        ,beau=b
        )

application = sae.create_wsgi_app(app)
#from sae.ext.shell import ShellMiddleware
#application = sae.create_wsgi_app(ShellMiddleware(app, '1q2w3e4r5t')) 
