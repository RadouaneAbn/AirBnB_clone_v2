#!/usr/bin/python3
""" Test
"""
from models.engine.file_storage import FileStorage

try:
    if FileStorage.delete.__doc__ is None or len(FileStorage.delete.__doc__) < 5:
        print("Missing documentation for the method `delete`")
        exit(1)

    print("OK", end="")
except:
    print("Impossible to validate documentation of the method `delete`")
    exit(1)
