#!/usr/bin/python
from sys import argv
import zbar
import httplib2
import json
import time
import datetime


def sendHTTPRq(barcode):
    httplib2.debuglevel     = 0
    http                    = httplib2.Http()
    content_type_header     = "application/json"

    url = "http://10.0.8.238/apis/addBook?isbn=" +str(barcode)

    data = {    'Id':         barcode,
                'CreatedDateTime':    str(datetime.datetime.now()),
                'CreatedUser':    'saurabh',
                'UpdatedDateTime':    str(datetime.datetime.now())
           }

    headers = {'Content-Type': content_type_header}
    print ("Posting %s" % data)

    #while True:
    response, content = http.request( url,
                                      'GET',
                                      json.dumps(data),
                                      headers=headers)
    print (response);
    print (content);
    #time.sleep(3)
    return;




# create a Processor
proc = zbar.Processor()

# configure the Processor
proc.parse_config('enable')

# initialize the Processor
device = '/dev/video0'
if len(argv) > 1:
    device = argv[1]

#proc.request_size(1,1)

proc.init(device)

# enable the preview window
proc.visible = True

# read at least one barcode (or until window closed)
proc.process_one()

# hide the preview window
proc.visible = True

# extract results

for symbol in proc.results:
    # do something useful with results
    print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data

   #sendHTTPRq(symbol.data)

