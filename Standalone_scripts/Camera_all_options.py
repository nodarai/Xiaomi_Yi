#! /usr/bin/env python
# encoding: windows-1250
#
# Res Andy

import os, re, sys, time, socket

from settings import camaddr
from settings import camport
from helpers import get_token

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.connect((camaddr, camport))

srv.send('{"msg_id":257,"token":0}')

token = get_token(srv)

tosend = '{"msg_id":3,"token":%s}' %token
srv.send(tosend)

while 1:
	conf = srv.recv(4096)
	if "param" in conf:
		break

print(conf)
import json
conf = json.loads(conf)
import pprint
pprint.pprint(conf["param"])
# conf = conf[37:]

# myconf = conf.split(",")

for mytag in conf["param"]:
	print(mytag)
	paramname = mytag.keys()[0]
	print(paramname)
	tosend = '{"msg_id":3,"token":%s,"param":"%s"}' %(token, paramname)
	srv.send(tosend)
	print srv.recv(8192)


print "_____________________________________________"
print
print "press CTRL+C to close"

while 1:
	time.sleep(1)
