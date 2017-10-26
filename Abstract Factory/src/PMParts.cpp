using namespace std;

#include "../PMParts.h"

ostream & PMWindow::print(ostream & os)
{
        os << "PM Window";
        return os;
}

void PMWindow::appears()
{
        cout << "A 1366 x 720 black screen appears." << endl;
}


ostream & PMScrollBar::print(ostream & os)
{
        os << "PM ScrollBar";
        return os;
}

void PMScrollBar::moves()
{
        cout << "Where is the scroll bar?" << endl;
}