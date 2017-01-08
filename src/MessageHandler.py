#!/usr/bin/python

class MessageHandler():
    amqp = None
    mysql = None

    def setMySqlConnection(self, mysqlConnection):
        self.mysql = mysqlConnection
    
    def setAmqpConnection(self, amqpConnection):
        self.amqp = amqpConnection
        self.amqp.bindEverything()
        self.amqp.addMessageTypeHandler('HEARTBEAT', self.onHeartbeat)
        self.amqp.addMessageHandler(self.onMessage)

    def start(self):
        self.amqp.startConsuming()

    def onHeartbeat(self, channel, method, properties, body):
        print "Heartbeat"

        channel.basic_ack(delivery_tag = method.delivery_tag, multiple = False)

    def onMessage(self, channel, method, properties, body):
        print "msg"
        channel.basic_ack(delivery_tag = method.delivery_tag, multiple = False)
