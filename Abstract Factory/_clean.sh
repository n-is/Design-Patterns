#!/bin/bash
#
if [ -f "Makefile" ] #
then #
        make clean #
        make cleanDep #
        rm -f Makefile #
fi #