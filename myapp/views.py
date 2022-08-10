from django.shortcuts import render
from django.http import HttpResponse
from django.core.files import File
import csv
import myapp.converter as converter
from tabulate import tabulate
# reading the input csv file
def read_file():
    f = open('/Users/sukanya/Downloads/two.csv', 'r')
    file_content = f.readlines()
    f.close()
    return file_content
''''
# To display transaction details
def trans_view(request):
    # create a dictionary
    output = converter.convert()
    context = {
        "transaction" : output
    }
    # return response
    return render(request, "display.html", context)
'''
def trans_view(request):
    results = converter.convert()
    tran = "Transaction id's    : "
    src = "Source Currency     : "
    dec = "Destination Currency: "
    sra = "Source Amount       : "
    dea = "destination Amount  : "
    for i in results:
        tran += " " +i[0] +","
        src += " " + str(i[1]) +","
        dec += " " + str(i[2]) +","
        sra += " " + str(i[3]) +","
        dea += " " + str(i[4]) +","
    context = {
        "trid": tran,
        "src" : src,
        "dec":dec,
        "sra":sra,
        "dea":dea
    }
    return render(request, "display.html", context )