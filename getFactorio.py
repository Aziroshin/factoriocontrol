#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import config
from urllib import request
from pathlib import Path
import sys
version=sys.argv[1]
print("Downloading:", config.downloadUrlTemplate.format(version=version), "to", Path(config.versionsDir, "{version}.tar.gz".format(version=version)))
request.urlretrieve(config.downloadUrlTemplate.format(version=version), Path(config.versionsDir, "{version}.tar.gz".format(version=version)))
