#!/usr/bin/env python3
import tornado.ioloop
import tornado.web

import rospy
import rospkg

rospack = rospkg.RosPack()
pkg_dir = rospack.get_path('tocabi_server')

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("rosweb.html",title="HELLO DYROS")

def make_app():
    
    return tornado.web.Application([
        (r"/EventEmitter2/(.*)", tornado.web.StaticFileHandler, {'path': pkg_dir+"/EventEmitter2/"}),
        (r"/roslibjs/(.*)", tornado.web.StaticFileHandler, {'path': pkg_dir+"/roslibjs/"}),
        (r"/mdl/(.*)", tornado.web.StaticFileHandler, {'path': pkg_dir+"/mdl/"}),
        (r"/roboto/(.*)", tornado.web.StaticFileHandler, {'path': pkg_dir+"/RobotoTTF/"}),
        (r"/css/(.*)", tornado.web.StaticFileHandler, {'path': pkg_dir+"/css/"}),
        (r"/getmdl-select/(.*)", tornado.web.StaticFileHandler, {'path': pkg_dir+"/getmdl-select/"}),
        (r"/material-design-icons/(.*)", tornado.web.StaticFileHandler, {'path': pkg_dir+"/material-design-icons/"}),
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()