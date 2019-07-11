#ifndef TESTREPORTGENERATOR_H
#define TESTREPORTGENERATOR_H

#include <QMainWindow>

namespace Ui {
class TestReportGenerator;
}

class TestReportGenerator : public QMainWindow
{
    Q_OBJECT

public:
    explicit TestReportGenerator(QWidget *parent = nullptr);
    ~TestReportGenerator();

private slots:

    void on_BrowseCSV_clicked();

    void on_BrowseOutput_clicked();

    void on_checkBox1_stateChanged(int arg1);

    void on_checkBox2_stateChanged(int arg1);

    void on_checkBox4_stateChanged(int arg1);

    void on_checkBox3_stateChanged(int arg1);

    void on_checkBox5_stateChanged(int arg1);

    void on_checkBox6_stateChanged(int arg1);

    void on_checkBox7_stateChanged(int arg1);

    void on_checkBox8_stateChanged(int arg1);

    void on_Generate_clicked();

private:
    Ui::TestReportGenerator *ui;
    bool channels[8] = {true, true, true, true, true, false, false, false};
    QString outputFile = "";
    QString inputFile = "";
};

#endif // TESTREPORTGENERATOR_H
