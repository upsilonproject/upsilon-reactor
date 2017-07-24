#!/usr/bin/python

import os, sys

from upsilon import logger, amqp, sql
from config import RuntimeConfig
from MessageHandler import MessageHandler
from time import sleep

logger.log("upsilon-reactor")

config = RuntimeConfig()

messageHandler = MessageHandler()

while True:
  try: 
    mysqlConnection = sql.newSqlConnection(config.dbUser, config.dbPass)
    messageHandler.setMySqlConnection(mysqlConnection)

    amqpConnection = amqp.Connection(config.amqpHost, config.amqpQueue, config.amqpExchange);
    amqpConnection.setPingReply("upsilon-reactor", "development", "db, amqp, reactor");
    amqpConnection.startHeartbeater();

    messageHandler.setAmqpConnection(amqpConnection)

    try:
        messageHandler.start();
    except KeyboardInterrupt as e:
        heartbeater.stop()
        print e

    print "conn loop finished"
  except Exception as e:
    print "reactor exception", e

  print "sleeping for 20 seconds"
  sleep(20)

print "reactor stopped"
