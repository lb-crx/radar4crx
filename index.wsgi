# -*- coding: utf-8 -*-
VERSION = "radar4crx v12.7.3"
import sae
#import urllib2 as urilib
from bottle import Bottle, request

app = Bottle()

@app.route('/')
def hello():
    return '''Hollo, there! 
    - Bottle @ SAE 4 radar4crx!
    '''

class Borg():
    '''base http://blog.youxu.info/2010/04/29/borg
        - 单例式配置收集类
    '''
    __collective_mind = {}
    def __init__(self):
        self.__dict__ = self.__collective_mind
cfg = Borg()

@app.route('/chk/', method="POST")
@app.route('/chk', method="POST")
def chk():
    uri = request.forms.get('uri')
    result = _askCloud(cfg.APITYPE, uri)
    return "/chk:: %s"% cfg.PHISHTYPE[str(result)]

@app.route('/qchk/', method="POST")
@app.route('/qchk', method="POST")
def qchk():
    url = request.forms.get('uri').split("/")
    if 1 == len(url):
        uri = url[0]
    else:
        uri = url[2]
    #k = urlsafe_b64encode(uri)
    k = uri
    print k
    import sae.kvdb
    #print "kv.get_info() %s"% kv.get_info()
    kv = sae.kvdb.KVClient()
    v = kv.get(k)
    print "kv.get(k)~ type=%s var=%s"%(type(v),v)
    #return "dabugging.."
    if None == v:
        result = _askCloud(cfg.APITYPE, uri)
        kv.add(k, result)
        return "/qchk(KSC)::\t %s" % cfg.PHISHTYPE[str(result)]
    else:
        return "/qchk(KVDB)::\t %s" % cfg.PHISHTYPE[str(v)]

import base64
import time
from hashlib import md5
from base64 import urlsafe_b64encode
def _askCloud(api_path, url):
    args = __genQueryArgs(api_path, url)
    api_url = "http://%s%s?%s"% (cfg.OPEN_HOST, cfg.APITYPE ,args)
    print api_url
    result = eval(urilib.urlopen(api_url).read())
    print result
    if result['success'] == 1:
        return result['phish']
    else:
        return result

def __genQueryArgs(api_path, url):
    args = "appkey=" + cfg.APPKEY
    args += "&q=" + base64.urlsafe_b64encode(url)
    args += "&timestamp=" + "%.3f" % (time.time())
    sign_base_string = api_path + "?" + args
    args += "&sign=" + md5(sign_base_string + cfg.SECRET).hexdigest()
    return args

application = sae.create_wsgi_app(app)
#from sae.ext.shell import ShellMiddleware
#application = sae.create_wsgi_app(ShellMiddleware(app, '1q2w3e4r5t')) 
