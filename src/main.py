#!/usr/bin/python

import os, sys

from upsilon import logger, amqp, sql
from config import RuntimeConfig
from MessageHandler import MessageHandler

config = RuntimeConfig()

messageHandler = MessageHandler()

mysqlConnection = sql.newSqlConnection(config.dbUser, config.dbPass)
messageHandler.setMySqlConnection(mysqlConnection)

amqpConnection = amqp.Connection(config.amqpHost, config.amqpQueue, config.amqpExchange);
messageHandler.setAmqpConnection(amqpConnection)

logger.log("upsilon-node-alerter")

try:
    messageHandler.start();
except KeyboardInterrupt:
    messageHandler.amqp.close()
