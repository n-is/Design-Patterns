#ifndef PM_PARTS_H_
#define PM_PARTS_H_

#include <iostream>

#include "WidgetParts.h"

class PMWindow : public Window
{
public:
        ostream & print(ostream & os);
        void appears();
};

class PMScrollBar : public ScrollBar
{        
public:
        ostream & print(ostream & os);
        void moves();
};

#endif