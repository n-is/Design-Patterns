#ifndef MOTIF_H_
#define MOTIF_H_

#include "WidgetFactory.h"
#include "MotifParts.h"

class Motif : public WidgetFactory
{
public:
        MotifWindow * createWindow() { return new MotifWindow; }
        MotifScrollBar * createScrollBar() { return new MotifScrollBar; }
};

#endif