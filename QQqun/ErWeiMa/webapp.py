# -*- coding:utf-8 -*-

import qrcode
import web

urls = (
    '/','Index',
)
render = web.template.render('templates')

class Index(object):
    def GET(self):
        return render.index()

if __name__ == '__main__':
     web.application(urls,globals()).run()