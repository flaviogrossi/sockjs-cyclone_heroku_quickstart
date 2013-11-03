import sys, os

import cyclone

from twisted.internet import reactor
from twisted.python import log

import sockjs.cyclone


class IndexHandler(cyclone.web.RequestHandler):
    """ Serve the main html page """

    def get(self):
        self.render('index.html')


class Connection(sockjs.cyclone.SockJSConnection):
    """ Main sockjs connection class """

    def connectionMade(self, info):
        log.msg('connected')
        self.sendMessage('Welcome!')

    def messageReceived(self, msg):
        log.msg('received %s' % msg)
        self.sendMessage('Server received "%s"' % msg)

    def connectionLost(self):
        log.msg('client disconnected')


if __name__ == "__main__":
    log.startLogging(sys.stdout)

    # setup urls: / for the main html page, /connection/.* for sockjs
    Router = sockjs.cyclone.SockJSRouter(Connection, '/connection')
    routed_urls = ( Router.urls + [ (r"/", IndexHandler), ] )

    # create cyclone app
    app = cyclone.web.Application(routed_urls)

    # run server
    port = int(os.environ.get("PORT", 5000))
    reactor.listenTCP(port, app)
    reactor.run()
