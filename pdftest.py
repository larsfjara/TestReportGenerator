
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.platypus import  Image
from reportlab.lib.units import inch, cm
import matplotlib.pyplot as plt
import datetime
import pandas as pd
import csv
import sys
from io import BytesIO
import statistics

from PyPDF2 import PdfFileWriter, PdfFileReader

plt.rcParams.update({'font.size': 6})


def testplot(names, showChannels, infile, outfile, approved):
    x = []
    ch1 = []
    ch2 = []
    ch3 = []
    ch4 = []
    ch5 = []
    ch6 = []
    ch7 = []
    ch8 = []

    with open(infile,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        fig, ax = plt.subplots()

        df = pd.read_csv(infile, sep='\s*,\s*', header=None, names=['date', 'ch0', 'ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6', 'ch7'], encoding='ascii', engine='python')
        for row in plots:
            ch1.append(int(row[1]))

    if showChannels[0] == 'true':
        plt.plot(df.index.values, df['ch1'], label=names[0])
    if showChannels[1] == 'true':
        plt.plot(df.index.values, df['ch1'], label=names[1])
    if showChannels[2] == 'true':
        plt.plot(df.index.values, df['ch1'], label=names[2])
    if showChannels[3] == 'true':
        plt.plot(df.index.values, df['ch1'], label=names[3])
    if showChannels[4] == 'true':
        plt.plot(df.index.values, df['ch1'], label=names[4])
    if showChannels[5] == 'true':
        plt.plot(df.index.values, df['ch1'], label=names[5])
    if showChannels[6] == 'true':
        plt.plot(df.index.values, df['ch1'], label=names[6])
    if showChannels[7] == 'true':
        plt.plot(df.index.values, df['ch1'], label=names[7])

    ax.xaxis.set_major_locator(plt.MaxNLocator(3))
    ax.set_ylim(0, 1000);
    plt.setp(ax.get_xticklabels())
    plt.xlabel('time')
    plt.grid()
    plt.ylabel('mbar')
    plt.legend()

    imgdata = BytesIO()
    plt.savefig(imgdata, format='png', dpi=1200)
    imgdata.seek(0)

    im = ImageReader(imgdata)
    logo = ImageReader('/home/larskf/TestReportGenerator/DB_long.jpg')

    c = canvas.Canvas(outfile)
    w,h = c._pagesize
    c.drawImage(im, 0, 120, w, h, preserveAspectRatio=True)
    c.drawImage(logo, 100, h/2 - 50, w-200, h, preserveAspectRatio=True)

    start = datetime.datetime.strptime(df.index.values[0], '%d.%m.%Y %H:%M:%S')
    stop = datetime.datetime.strptime(df.index.values[-1], '%d.%m.%Y %H:%M:%S')
    dur = stop - start

    c.setFont('Helvetica-Bold', 13)
    str = "Pressure leak test"
    c.drawString(50, 725, str)
    c.setFont('Helvetica', 11)

    str = "Started logging at:"
    c.drawString(50, 300, str)
    str = "     {}".format(start)
    c.drawString(50,280, str)
    str = "Test duration: {}".format(dur)
    c.drawString(50,260,str)


    c.drawString(50, 255, "_______________________________________________________________________________")
    c.setFont('Helvetica', 9)
    if showChannels[0] == 'true':
        maxval = max(df['ch0'])
        minval = min(df['ch0'])
        avgval = statistics.mean(df['ch0'])
        str = "{}:  Max: {:.0f} mbar     Min: {:.0f} mbar     Avg: {:.0f} mbar      Drop: {:.0f} mbar".format(names[0], maxval, minval, avgval, maxval - minval)
        #str = "%s:  Max: %f.2  Min: %f.2 Avg: %f.2 " % (names[0], maxval, minval, avgval)
        c.drawString(50,240, str)

    if showChannels[1] == 'true':
        maxval = max(df['ch1'])
        minval = min(df['ch1'])
        avgval = statistics.mean(df['ch1'])
        str = "{}:  Max: {:.0f} mbar     Min: {:.0f} mbar     Avg: {:.0f} mbar      Drop: {:.0f} mbar".format(names[1], maxval, minval, avgval, maxval - minval)
        c.drawString(50, 220, str)
    if showChannels[2] == 'true':
        maxval = max(df['ch2'])
        minval = min(df['ch2'])
        avgval = statistics.mean(df['ch2'])
        str = "{}:  Max: {:.0f} mbar     Min: {:.0f} mbar     Avg: {:.0f} mbar      Drop: {:.0f} mbar".format(names[2], maxval, minval, avgval, maxval - minval)
        c.drawString(50,200, str)
    if showChannels[3] == 'true':
        maxval = max(df['ch3'])
        minval = min(df['ch4'])
        avgval = statistics.mean(df['ch3'])
        str = "{}:  Max: {:.0f} mbar     Min: {:.0f} mbar     Avg: {:.0f} mbar      Drop: {:.0f} mbar".format(names[3], maxval, minval, avgval, maxval - minval)
        c.drawString(50,180, str)
    if showChannels[4] == 'true':
        maxval = max(df['ch4'])
        minval = min(df['ch4'])
        avgval = statistics.mean(df['ch4'])
        str = "{}:  Max: {:.0f} mbar     Min: {:.0f} mbar     Avg: {:.0f} mbar      Drop: {:.0f} mbar".format(names[4],
                                                                                                              maxval,
                                                                                                              minval,
                                                                                                              avgval,
                                                                                                              maxval - minval)
        c.drawString(50,160, str)
    if showChannels[5] == 'true':
        maxval = max(df['ch5'])
        minval = min(df['ch5'])
        avgval = statistics.mean(df['ch5'])
        str = "{}:  Max: {:.0f} mbar     Min: {:.0f} mbar     Avg: {:.0f} mbar      Drop: {:.0f} mbar".format(names[5],
                                                                                                              maxval,
                                                                                                              minval,
                                                                                                              avgval,
                                                                                                              maxval - minval)
        c.drawString(50, 140, str)
    if showChannels[6] == 'true':
        maxval = max(df['ch6'])
        minval = min(df['ch6'])
        avgval = statistics.mean(df['ch6'])
        str = "{}:  Max: {:.0f} mbar     Min: {:.0f} mbar     Avg: {:.0f} mbar      Drop: {:.0f} mbar".format(names[6],
                                                                                                              maxval,
                                                                                                              minval,
                                                                                                              avgval,
                                                                                                              maxval - minval)
        c.drawString(50, 120, str)
    if showChannels[7] == 'true':
        maxval = max(df['ch7'])
        minval = min(df['ch7'])
        avgval = statistics.mean(df['ch7'])
        str = "{}:  Max: {:.0f} mbar     Min: {:.0f} mbar     Avg: {:.0f} mbar      Drop: {:.0f} mbar".format(names[7],
                                                                                                              maxval,
                                                                                                              minval,
                                                                                                              avgval,
                                                                                                              maxval - minval)
        c.drawString(50, 100, str)

    c.drawString(50, 95, "_______________________________________________________________________________")

    c.setFont('Helvetica', 11)
    str = "Approved by: %s" % approved
    c.drawString(50, 75, str)
    c.drawString(50, 30, "_____________________________________")

    c.save()


if __name__ == '__main__':
    nms = sys.argv[1].split(',')
    chs = sys.argv[2].split(',')
    for x in chs: x = bool(x)
    inf = sys.argv[3]
    outf = sys.argv[4]
    appr = sys.argv[5]
    testplot(nms, chs, inf, outf, appr)
