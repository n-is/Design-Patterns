#
# -*- Makefile -*-
#
# Created      : 10/27/2017 1:46:8
# Author       : n-is
# email        : 073bex422.nischal@pcampus.edu.np
#

TARGET = Abstract_Factory

CXX = g++
CXXFLAGS =  -Wall -g -std=c++14 -O1

CXXSRC = \
	main.cpp \
	src/MotifParts.cpp

OBJ = $(CXXSRC:.cpp=.o)
DEP = $(OBJ:.o=.d)

all : $(TARGET)

$(TARGET) : $(OBJ)
	$(CXX) $(CXXFLAGS) $^ -o $@
	@ echo "\n\t\tAll Done. Thank You\n"

%.d : %.cpp
	$(CPP) $< $(CXXFLAGS) -MM -MT $(@:.d=.o) >$@

-include $(DEP)

.PHONY : clean CleanDep makeDebug syntax

syntax :
	$(CXX) $(CXXFLAGS) -fsyntax-only $(CXXSRC)
	@ echo "\n\t\tSyntax Checked\n"

clean :
	rm -f $(OBJ) $(TARGET)
	@ echo "\n\t\tEverything Cleaned Up\n"

cleanDep :
	rm -f $(DEP)
	@ echo "\n\t\tDependencies Cleaned Up\n"

makeDebug :
	@ echo $(CXXSRC)
	@ echo $(OBJ)
	@ echo $(DEP)
