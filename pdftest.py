
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

        df = pd.read_csv(infile, sep='\s*,\s*',  encoding='ascii', engine='python')
        #df.set_index("Time", inplace=True)
        #print(df.head())
        headers = df.columns.tolist()
        #print(headers)
        #for row in plots:
         #   ch1.append(int(row[1]))
        test = df[headers[0]]
        print(df[headers[0]].head())

    if showChannels[0] == 'true':
        plt.plot(df[headers[0]], df[headers[1]], label = headers[1])
    if showChannels[1] == 'true':
        plt.plot(df[headers[0]], df[headers[2]], label = headers[2])
    if showChannels[2] == 'true':
        plt.plot(df[headers[0]], df[headers[3]], label = headers[3])
    if showChannels[3] == 'true':
        plt.plot(df[headers[0]], df[headers[4]], label = headers[4])
    if showChannels[4] == 'true':
        plt.plot(df[headers[0]], df[headers[5]], label = headers[5])
    if showChannels[5] == 'true':
        plt.plot(df[headers[0]], df[headers[6]], label = headers[6])
    if showChannels[6] == 'true' :
        plt.plot(df[headers[0]], df[headers[7]], label = headers[7])
    if showChannels[7] == 'true':
        plt.plot(df[headers[0]], df[headers[8]], label = headers[8])

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

    start = datetime.datetime.strptime(df[headers[0]].values[0], '%d.%m.%Y %H:%M:%S')
    stop = datetime.datetime.strptime(df[headers[0]].values[-1], '%d.%m.%Y %H:%M:%S')
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
        maxval = max(df[headers[1]])
        minval = min(df[headers[1]])
        avgval = statistics.mean(df[headers[1]])
        str = "{}:  Max: {:.0f} mbar     Min: {:.0f} mbar     Avg: {:.0f} mbar      Drop: {:.0f} mbar".format(headers[1], maxval, minval, avgval, maxval - minval)
        #str = "%s:  Max: %f.2  Min: %f.2 Avg: %f.2 " % (names[0], maxval, minval, avgval)
        c.drawString(50,240, str)

    if showChannels[1] == 'true':
        maxval = max(df[headers[2]])
        minval = min(df[headers[2]])
        avgval = statistics.mean(df[headers[2]])
        str = "{}:  Max: {:.0f} mbar     Min: {:.0f} mbar     Avg: {:.0f} mbar      Drop: {:.0f} mbar".format(headers[2], maxval, minval, avgval, maxval - minval)
        c.drawString(50, 220, str)
    if showChannels[2] == 'true':
        maxval = max(df[headers[3]])
        minval = min(df[headers[3]])
        avgval = statistics.mean(df[headers[3]])
        str = "{}:  Max: {:.0f} mbar     Min: {:.0f} mbar     Avg: {:.0f} mbar      Drop: {:.0f} mbar".format(headers[3], maxval, minval, avgval, maxval - minval)
        c.drawString(50,200, str)
    if showChannels[3] == 'true':
        maxval = max(df[headers[4]])
        minval = min(df[headers[4]])
        avgval = statistics.mean(df[headers[4]])
        str = "{}:  Max: {:.0f} mbar     Min: {:.0f} mbar     Avg: {:.0f} mbar      Drop: {:.0f} mbar".format(headers[4], maxval, minval, avgval, maxval - minval)
        c.drawString(50,180, str)
    if showChannels[4] == 'true':
        maxval = max(df[headers[5]])
        minval = min(df[headers[5]])
        avgval = statistics.mean(df[headers[5]])
        str = "{}:  Max: {:.0f} mbar     Min: {:.0f} mbar     Avg: {:.0f} mbar      Drop: {:.0f} mbar".format(headers[5],
                                                                                                              maxval,
                                                                                                              minval,
                                                                                                              avgval,
                                                                                                              maxval - minval)
        c.drawString(50,160, str)
    if showChannels[5] == 'true':
        maxval = max(df[headers[6]])
        minval = min(df[headers[6]])
        avgval = statistics.mean(df[headers[6]])
        str = "{}:  Max: {:.0f} mbar     Min: {:.0f} mbar     Avg: {:.0f} mbar      Drop: {:.0f} mbar".format(headers[6],
                                                                                                              maxval,
                                                                                                              minval,
                                                                                                              avgval,
                                                                                                              maxval - minval)
        c.drawString(50, 140, str)
    if showChannels[6] == 'true':
        maxval = max(df[headers[7]])
        minval = min(df[headers[7]])
        avgval = statistics.mean(df[headers[7]])
        str = "{}:  Max: {:.0f} mbar     Min: {:.0f} mbar     Avg: {:.0f} mbar      Drop: {:.0f} mbar".format(headers[7],
                                                                                                              maxval,
                                                                                                              minval,
                                                                                                              avgval,
                                                                                                              maxval - minval)
        c.drawString(50, 120, str)
    if showChannels[7] == 'true':
        maxval = max(df[headers[8]])
        minval = min(df[headers[8]])
        avgval = statistics.mean(df[headers[8]])
        str = "{}:  Max: {:.0f} mbar     Min: {:.0f} mbar     Avg: {:.0f} mbar      Drop: {:.0f} mbar".format(headers[8],
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
    for x in chs: x = x == 'true'
    inf = sys.argv[3]
    outf = sys.argv[4]
    appr = sys.argv[5]
    testplot(nms, chs, inf, outf, appr)
