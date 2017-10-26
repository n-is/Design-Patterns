#ifndef WIDGET_PARTS_H_
#define WIDGET_PARTS_H_

#include <iostream>

class WidgetParts
{
protected:
        virtual ostream & print(ostream & os) = 0;
public:
        friend ostream & operator<<(ostream &os, WidgetParts & wp) {
                return wp.print(os);
        }
};

class Window : public WidgetParts
{
public:
        virtual ostream & print(ostream & os) = 0;
        virtual void appears() = 0;
};

class ScrollBar : public WidgetParts
{
public:
        virtual ostream & print(ostream & os) = 0;
        virtual void moves() = 0;
};

#endif