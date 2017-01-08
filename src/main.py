#!/usr/bin/python

import os, sys

from upsilon import logger, amqp, sql
from config import RuntimeConfig
from MessageHandler import MessageHandler

logger.log("upsilon-reactor")

config = RuntimeConfig()

messageHandler = MessageHandler()

mysqlConnection = sql.newSqlConnection(config.dbUser, config.dbPass)
messageHandler.setMySqlConnection(mysqlConnection)

amqpConnection = amqp.Connection(config.amqpHost, config.amqpQueue, config.amqpExchange);
amqpConnection.setPingReply("reactor", "devel", "db, amqp, reactor");
amqpConnection.startHeartbeater();

messageHandler.setAmqpConnection(amqpConnection)

try:
    messageHandler.start();
except KeyboardInterrupt as e:
    print e

print "stop"
