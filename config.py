#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
from pathlib import Path
scriptsDir = Path(__file__).absolute().parent
baseDir = Path(scriptsDir).parent
serversDir = Path(baseDir, "servers").absolute()
filesDir = Path(baseDir, "files").absolute()
versionsDir = Path(filesDir, "versions").absolute()
downloadUrlTemplate = "https://www.factorio.com/get-download/{version}/headless/linux64"
gameName="factorio" # 
progPrefix="{0}-server".format(gameName) #Used for stuff like naming screen sessions.
