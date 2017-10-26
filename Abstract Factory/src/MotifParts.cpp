using namespace std;

#include "../MotifParts.h"

ostream & MotifWindow::print(ostream & os)
{
        os << "Motif Window";
        return os;
}

void MotifWindow::appears()
{
        cout << "A 1920 x 1080 blue screen appears." << endl;
}


ostream & MotifScrollBar::print(ostream & os)
{
        os << "Motif ScrollBar";
        return os;
}

void MotifScrollBar::moves()
{
        cout << "The scroll bar takes us to the end." << endl;
}