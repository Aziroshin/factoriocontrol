#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import config
from pathlib import Path
from subprocess import Popen, PIPE

class Server(object):
	def __init__(self, name):
		self.name = name
		self.serverDir = Path(config.serversDir, self.name)
	def start(self):
		Popen([])
	def stop(self):
		Popen([])
