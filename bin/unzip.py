#!/usr/bin/env python

import sys
import zipfile
from cStringIO import StringIO

z = StringIO(sys.stdin.read())


with zipfile.ZipFile(z) as zipin:
	zipin.extractall()


