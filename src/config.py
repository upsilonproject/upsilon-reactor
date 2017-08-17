import os
import argparse

global args

argParser = argparse.ArgumentParser();
argParser.add_argument("--amqpHost", '-s')
args = argParser.parse_args()


import ConfigParser
global configParser
configParser = ConfigParser.ConfigParser()

configParser.add_section("amqp")
configParser.set("amqp", "host", "localhost")
configParser.set("amqp", "exchange", "ex_upsilon")
configParser.set("amqp", "queue", "")

if (os.path.isfile('/etc/upsilon-reactor/reactor.cfg')):
  configParser.readfp(open('/etc/upsilon-reactor/reactor.cfg'))

if (os.path.isfile("defaults.cfg")):
  configParser.readfp(open('defaults.cfg'))

class RuntimeConfig:
  amqpHost = None
  amqpExchange = None
  amqpQueue = None

  def __init__(self):
    self.applyConfig(configParser)
    self.applyArguments(args)

  def applyConfig(self, configParser):
    self.amqpHost = configParser.get('amqp', 'host')
    self.amqpExchange = configParser.get('amqp', 'exchange');
    self.amqpQueue = configParser.get('amqp', 'queue');

    print configParser.sections()

  def applyArguments(self, args):
    if args.amqpHost != None:
      self.amqpHost = args.amqpHost


