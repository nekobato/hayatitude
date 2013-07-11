# 1. install modules
#
# this program use google API modules
#
#   apiclient
#   oauth2client
#
# set modules to current directory
#   or use install command.
#
#
# 2. set cron
#

import httplib2
import sqlite3
import os.path
import pprint

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run


URL = 'https://www.googleapis.com/auth/latitude'


def minTime():
    cn = sqlite3.connect('../sqlite3')
    query = u"SELECT * FROM latitude ORDER BY time DESC"
    cc = cn.execute(query)
    row = cc.fetchone()
    if row is None:
        res = None
    else:
        #return timestampMs
        res = row[2]
    return res


def insertData(data):
    cn = sqlite3.connect('../sqlite3', isolation_level=None)
    for d in data:
        query = u"insert into latitude values (?, ?, ?)"
        cn.execute(query, (d[u"latitude"], d[u"longitude"], d[u"timestampMs"]))
    cn.close()


def main():
    if os.path.isfile('../sqlite3') is False:
        cn = sqlite3.connect('../sqlite3', isolation_level=None)
        query = u"CREATE TABLE latitude (latitude real, longitude real, time integer)"
        cn.execute(query)
        cn.close()

    mintime = minTime()

    flow = OAuth2WebServerFlow('', '', URL)

    storage = Storage('credentials.dat')
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        credentials = run(flow, storage)

    http = httplib2.Http()

    service = build('latitude', 'v1', http=credentials.authorize(http))

    res = service.location().list(min_time=mintime).execute()
    insertData(res.get('items', []))
    pprint.pprint(res.get('items', []))


if __name__ == '__main__':
    main()
