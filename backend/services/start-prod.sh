#!/bin/sh
exec ./ltedaemon.py prod&
exec ./matdaemon.py prod&
