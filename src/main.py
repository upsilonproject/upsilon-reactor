#!/usr/bin/python

import os, sys

from upsilon import logger, amqp
from config import RuntimeConfig
from MessageHandler import MessageHandler
from time import sleep

logger.log("upsilon-reactor")

config = RuntimeConfig()

messageHandler = MessageHandler()

try: 
  while True:
    amqpConnection = amqp.Connection(config.amqpHost, config.amqpQueue, config.amqpExchange);
    amqpConnection.setPingReply("upsilon-reactor", "development", "db, amqp, reactor");
    amqpConnection.startHeartbeater();

    messageHandler.setAmqpConnection(amqpConnection)

    try:
        messageHandler.start();
    except KeyboardInterrupt as e:
        heartbeater.stop()
        print e

  sleep(20)
  print "conn retry"
except:
  print "reactor exception"

print "reactor stopped"
