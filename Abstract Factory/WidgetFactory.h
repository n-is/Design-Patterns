#ifndef WIDGET_FACTORY_H_
#define WIDGET_FACTORY_H_

#include "WidgetParts.h"

class WidgetFactory
{
public:
        virtual Window * createWindow() = 0;
        virtual ScrollBar * createScrollBar() = 0;
};

#endif