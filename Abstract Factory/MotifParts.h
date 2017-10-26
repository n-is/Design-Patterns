#ifndef MOTIF_PARTS_H_
#define MOTIF_PARTS_H_

#include <iostream>

#include "WidgetParts.h"

class MotifWindow : public Window
{
public:
        ostream & print(ostream & os);
        void appears();
};

class MotifScrollBar : public ScrollBar
{
public:
        ostream & print(ostream & os);
        void moves();
};

#endif