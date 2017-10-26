#ifndef PM_H_
#define PM_H_

#include "WidgetFactory.h"
#include "PMParts.h"

class PM : public WidgetFactory
{
public:
        PMWindow * createWindow() { return new PMWindow; }
        PMScrollBar * createScrollBar() { return new PMScrollBar; }
};

#endif