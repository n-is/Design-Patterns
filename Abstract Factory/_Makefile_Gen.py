from __future__ import print_function
from datetime import datetime
import os

'''
	This script creates a makefile named 'Makefile' in the directory this
	file resides in.

	Currently this script only creates makefile for c and cpp projects.

	To use :
	I)   Copy this script to your project directory.
	II)  Run the script using python3.
	III) Check if the script created is as you wanted.

	Change arguments just below to adjust compilers you like and the flags
	to pass to the compiler.
'''

TARGET_DIR = os.getcwd()

CC = 'gcc'
CXX = 'g++'
CFLAGS = ' -Wall -g -std=c99 -O1'
CXXFLAGS = ' -Wall -g -std=c++14 -O1'

CXXSRC = []
CSRC = []

def get_sources() :
        global CXXSRC, CSRC
        c_ext = '.c'
        cpp_ext = '.cpp'
        os.chdir(TARGET_DIR)
        for dirpath, dirname, filename in os.walk(os.getcwd()) :
                for f in filename :
                        source = os.path.relpath(os.path.join(dirpath, f))
                        ext = os.path.splitext(source)[1]
                        if ext == c_ext:
                                CSRC.append(source)
                        elif ext == cpp_ext :
                                CXXSRC.append(source)

        if not CSRC and not CXXSRC :
                raise Exception("No Source file in the project")

def get_datetime() :
        now = datetime.now();
        return "{month}/{day}/{year} {hour}:{minute}:{second}".format(
                        month = now.month,
                        day = now.day,
                        year = now.year,
                        hour = now.hour,
                        minute = now.minute,
                        second = now.second
                        )

def genMakefile(s) :
        get_sources()
        st = '''#
# -*- Makefile -*-\n#
# Created      : ''' + get_datetime() + '''
# Author       : n-is
# email        : 073bex422.nischal@pcampus.edu.np
#\n
'''
        with open(s, 'w') as m :
                m.writelines(st)
                dir_name = os.path.split(os.path.dirname(os.path.realpath(__file__)))[-1]
                target = '_'.join(dir_name.split(' '))
                m.writelines('TARGET = ' + target + '\n')
                m.writelines('\n')
                if CSRC :
                        m.writelines('CC = ' + CC + '\n')
                        m.writelines('CFLAGS = ' + CFLAGS + '\n')
                        m.writelines('\n')

                if CXXSRC :
                        m.writelines('CXX = ' + CXX + '\n')
                        m.writelines('CXXFLAGS = ' + CXXFLAGS + '\n')
                        m.writelines('\n')

                if CSRC :
                        if len(CSRC) == 1 :
                                m.writelines('CSRC = ' + CSRC[0] + '\n')
                                m.writelines('\n')
                        else :
                                m.writelines('CSRC = \\\n')
                                for i in range(len(CSRC)) :
                                        m.writelines('\t' + CSRC[i])
                                        if i != len(CSRC) - 1 :
                                                m.writelines(' \\')
                                        m.writelines('\n');
                                m.writelines('\n')

                if CXXSRC :
                        if len(CXXSRC) == 1 :
                                m.writelines('CXXSRC = ' + CXXSRC[0] + '\n')
                                m.writelines('\n')
                        else :
                                m.writelines('CXXSRC = \\\n')
                                for i in range(len(CXXSRC)) :
                                        m.writelines('\t' + CXXSRC[i])
                                        if i != len(CXXSRC) - 1 :
                                                m.writelines(' \\')
                                        m.writelines('\n');
                                m.writelines('\n')

                if CSRC :
                        m.writelines('OBJ = $(CSRC:.c=.o) ')
                        if CXXSRC :
                                m.writelines('$(CXXSRC:.cpp=.o)')
                        m.writelines('\n')
                elif CXXSRC :
                        m.writelines('OBJ = $(CXXSRC:.cpp=.o)\n')

                m.writelines('DEP = $(OBJ:.o=.d)')
                m.writelines('\n\n')

                m.writelines('all : $(TARGET)')
                m.writelines('\n\n')

                m.writelines('$(TARGET) : $(OBJ)\n')
                if CXXSRC :
                        m.writelines('\t$(CXX) $(CXXFLAGS) $^ -o $@\n')
                elif CSRC :
                        m.writelines('\t$(CC) $(CFLAGS) $^ -o $@\n')
                else :
                        raise Exception("There are no required source files")
                m.writelines('\t@ echo "\\n\\t\\tAll Done. Thank You\\n"')
                m.writelines('\n\n')

                if CSRC :
                        m.writelines('%.d : %.c\n')
                        m.writelines('\t$(CPP) $< $(CFLAGS) -MM -MT $(@:.d=.o) >$@')
                        m.writelines('\n\n')

                if CXXSRC :
                        m.writelines('%.d : %.cpp\n')
                        m.writelines('\t$(CPP) $< $(CXXFLAGS) -MM -MT $(@:.d=.o) >$@')
                        m.writelines('\n\n')

                m.writelines('-include $(DEP)')
                m.writelines('\n\n')

                m.writelines('.PHONY : clean CleanDep makeDebug syntax')
                m.writelines('\n\n')

                m.writelines('syntax :\n')
                if CSRC :
                        m.writelines('\t$(CC) $(CFLAGS) -fsyntax-only $(CSRC)\n')
                if CXXSRC :
                        m.writelines('\t$(CXX) $(CXXFLAGS) -fsyntax-only $(CXXSRC)\n')
                m.writelines('\t@ echo "\\n\\t\\tSyntax Checked\\n"')
                m.writelines('\n\n')

                m.writelines('clean :\n')
                m.writelines('\trm -f $(OBJ) $(TARGET)\n')
                m.writelines('\t@ echo "\\n\\t\\tEverything Cleaned Up\\n"')
                m.writelines('\n\n')

                m.writelines('cleanDep :\n')
                m.writelines('\trm -f $(DEP)\n')
                m.writelines('\t@ echo "\\n\\t\\tDependencies Cleaned Up\\n"')
                m.writelines('\n\n')

                m.writelines('makeDebug :\n')
                if CSRC :
                        m.writelines('\t@ echo $(CSRC)\n')
                if CXXSRC :
                        m.writelines('\t@ echo $(CXXSRC)\n')
                m.writelines('\t@ echo $(OBJ)\n')
                m.writelines('\t@ echo $(DEP)\n')


genMakefile('Makefile')
# os.system('make')
