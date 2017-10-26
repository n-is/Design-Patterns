#include <iostream>

using namespace std;

#include "Motif.h"
#include "PM.h"

void test_MotifWidget();
void test_PMWidget();

int main()
{
        cout << "-----------------------------------" << endl;
        test_MotifWidget();
        cout << "-----------------------------------" << endl;
        test_PMWidget();
        cout << "-----------------------------------" << endl;
        return 0;
}

void test_MotifWidget()
{
        WidgetFactory * theWidget = new Motif;
        
        Window * theJhyal = theWidget->createWindow();
        cout << *theJhyal << endl;
        theJhyal->appears();

        ScrollBar * scroll = theWidget->createScrollBar();
        cout << *scroll << endl;
        scroll->moves();
}

void test_PMWidget()
{
        WidgetFactory * theWidget = new PM;
        
        Window * presentationManager = theWidget->createWindow();
        cout << *presentationManager << endl;
        presentationManager->appears();

        ScrollBar * PMscroll = theWidget->createScrollBar();
        cout << *PMscroll << endl;
        PMscroll->moves();
}
