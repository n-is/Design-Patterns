#include <iostream>

using namespace std;

#include "Motif.h"

int main()
{
        WidgetFactory * theWidget = new Motif;

        Window * theJhyal = theWidget->createWindow();
        cout << *theJhyal << endl;
        theJhyal->appears();

        ScrollBar * scroll = theWidget->createScrollBar();
        cout << *scroll << endl;
        scroll->moves();

        return 0;
}