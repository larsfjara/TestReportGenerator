#include "testreportgenerator.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    TestReportGenerator w;
    w.show();

    return a.exec();
}
