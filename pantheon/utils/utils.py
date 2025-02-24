
import time, datetime

def getLimits(headers):
    if 'X-Method-Rate-Limit' in headers and 'X-App-Rate-Limit' in headers:
        appLimits = {}
        for appLimit in headers['X-App-Rate-Limit'].split(","):
            appLimits[int(appLimit.split(":")[1])] = int(appLimit.split(":")[0])

        methodLimits = {}
        for methodLimit in headers['X-Method-Rate-Limit'].split(","):
            methodLimits[int(methodLimit.split(":")[1])] = int(methodLimit.split(":")[0])

        return (appLimits,methodLimits)
    return None

def serverToRegion(server):
    americas = ["br1", "la1", "la2", "na1", "oc1"]
    europe = ["eun1", "euw1", "tr1", "ru"]
    asia = ["kr", "jp1"]
    if server in americas:
        return "americas"
    elif server in europe:
        return "europe"
    elif server in asia:
        return "asia"
    return None

def dateToTimestamp(date):
    return int(time.mktime(datetime.datetime.strptime(date, '%a, %d %b %Y %H:%M:%S GMT').timetuple()))

def getTimestamp(headers):
    try:
        timestamp = dateToTimestamp(headers['Date'])
    except Exception as e:
        timestamp = int(time.time())
    return timestamp

def urlParams(params):
    if params is None:
        return ""
    else:
        strParams = "?"
        for i in params:
            if type(params[i]) == list:
                for p in params[i]:
                    strParams+= i+"="+str(p)+"&"
            else:
                strParams+= i+"="+str(params[i])+"&"
        return strParams[:-1]