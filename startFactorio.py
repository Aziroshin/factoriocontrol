#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import config
from lib import Server
from subprocessing import Popen
import os

server = Server(sys.argv[1])
