#include "testreportgenerator.h"
#include "ui_testreportgenerator.h"
#include <QFileDialog>
#include <QDebug>
#include <QProcess>
TestReportGenerator::TestReportGenerator(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::TestReportGenerator)
{
    ui->setupUi(this);
    ui->checkBox1->setChecked(channels[0]);
    ui->checkBox2->setChecked(channels[1]);
    ui->checkBox3->setChecked(channels[2]);
    ui->checkBox4->setChecked(channels[3]);
    ui->checkBox5->setChecked(channels[4]);
    ui->checkBox6->setChecked(channels[5]);
    ui->checkBox7->setChecked(channels[6]);
    ui->checkBox8->setChecked(channels[7]);
}

TestReportGenerator::~TestReportGenerator()
{
    delete ui;
}

void TestReportGenerator::on_BrowseCSV_clicked()
{
    QString filename = QFileDialog::getOpenFileName(
                this,
                "Open CSV File",
                "/home/larskf/TestReportGenerator",
                "CSV files (*.csv);; All files (*)");

    if(!filename.isNull() ){
        inputFile = filename;
        ui->inputFileFIeld->setText(filename);
    }
}


void TestReportGenerator::on_BrowseOutput_clicked()
{
    QString filename = QFileDialog::getSaveFileName(
                this,
                "Select output path",
                "/home/larskf/TestReportGenerator",
                "*.pdf;; All files (*)");

    if(!filename.isNull() ){
        outputFile = filename;
        ui->OutputFileField->setText(filename);
    }
}

void TestReportGenerator::on_checkBox1_stateChanged(int arg1)
{
    channels[0] = arg1 ? true : false;
}

void TestReportGenerator::on_checkBox2_stateChanged(int arg1)
{
    channels[1] = arg1 ? true : false;
}

void TestReportGenerator::on_checkBox3_stateChanged(int arg1)
{
    channels[2] = arg1 ? true : false;
}

void TestReportGenerator::on_checkBox4_stateChanged(int arg1)
{
    channels[3] = arg1 ? true : false;
}

void TestReportGenerator::on_checkBox5_stateChanged(int arg1)
{
    channels[4] = arg1 ? true : false;
}

void TestReportGenerator::on_checkBox6_stateChanged(int arg1)
{
    channels[5] = arg1 ? true : false;
}

void TestReportGenerator::on_checkBox7_stateChanged(int arg1)
{
    channels[6] = arg1 ? true : false;
}

void TestReportGenerator::on_checkBox8_stateChanged(int arg1)
{
    channels[7] = arg1 ? true : false;
}

void TestReportGenerator::on_Generate_clicked()
{
    const QFileInfo out(outputFile);
    QString outPath = out.path();
    const QFileInfo outputDir(outPath);
    if ((!outputDir.exists()) || (!outputDir.isDir()) || (!outputDir.isWritable())) {
        qWarning() << "output directory does not exist, is not a directory, or is not writeable"
                   << outputDir.absoluteFilePath();
        return;
    }

    QString ch = "";
    for(int i = 0; i < 8; i++){
        ch.append(channels[i] ? "true" : "false");
        if (i < 7)
            ch.append(",");
    }

    QString nms = "Channel1,Channel2,Channel3,Channel4,Channel5,Channel6,Channel7,Channel8";
    QString appr = "\"";
    appr.append(ui->approveBy->text());
    appr.append("\"");
    QStringList arguments { "/home/larskf/TestReportGenerator/pdftest.py", nms, ch, inputFile, outputFile, appr};
    QProcess p;
    p.start("python3", arguments);
    p.waitForFinished();


}
