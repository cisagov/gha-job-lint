#!/usr/bin/env python

"""A file designed to fail pre-commit checks.
This should cause multiple failures based on our pre-commit configuration."""

import subprocess

proc = subprocess.run(["echo", "Hello, World!"], shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print(proc.stdout.decode())
