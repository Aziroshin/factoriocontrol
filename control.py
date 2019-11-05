#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import config
from lib import Server
from subprocess import Popen, PIPE
import argparse
import os
from typing import NamedTuple

class RunningServerList(object):
	
	class PROCESS_INFO(NamedTuple):
		name: str
		id: str
		
	@property
	def screenSessionList(self):
		sessionsFound = []
		process = Popen(["screen", "-ls"], stdout=PIPE)
		stdout, stderr = process.communicate()
		screens = stdout.partition(b"There are screens on:")[-1].rpartition(b"3 Sockets")[0].split(b"\n\t")
		for screen in screens:
			if b"." in screen: # Filter out empty b'\r' at [0]
				screen = screen.decode()
				screenInfo = screen.partition(".")
				screenId = screenInfo[0]
				screenName = screenInfo[2].partition("\t")[0]
				sessionsFound.append(self.__class__.PROCESS_INFO(screenName, screenId))
		return sessionsFound
	
	@property
	def screenSessionListString(self):
		return "\n".join(["{name} ({id})".format(name=info.name, id=info.id) for info in self.screenSessionList])

class ScreenRunWrapper(object):
	
	"""Interface to a screen session and its process(s)."""
	
	def __init__(self, name):
		self.name = name
	
	def run(self, command):
		"""Run a command in screen.
		Takes:
			- command (list): Just like you'd pass to Popen."""
		Popen(["screen", "-d", "-m", "-S", "name"]+command)
		
	def stop(self):
		"""Stop the screen session."""
		Popen(["screen", "-S", self.name, "-X", "quit"])
		

class Action(object):
	
	@property
	def args(self):
		return self.actionParser.parse_args()
	
	@property
	def actionParser(self):
		"""Override in accordance with the command line args needed for this action."""
		parser = argparse.ArgumentParser(description="This action takes no command line arguments.")
		parser.add_argument("action")
		return parser
	
	def run(self):
		"""Override this to define what the action does."""
		pass#OVERRIDE
		
class Start(Action):
	
	@property
	def actionParser(self):
		parser = super().parser
		parser.add_argument("action", help="An action to perform, in this case start.")
		parser.add_argument("server", help="Name of the server to start.")
		return parser
	
	def run(self):
		"""Run the server."""
		pass#TODO #Something with Popen([])
		
class List(Action):
	
	def run(self):
		"""List all servers."""
		return RunningServerList().screenSessionListString

actions = {"list": List, "start": Start}
mainParser = argparse.ArgumentParser(description="Take an action and its arguments (start, stop).")
mainParser.add_argument("action", help="An action to perform, such as start or stop.")
args = mainParser.parse_args()

print(actions[args.action]().run())
