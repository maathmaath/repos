from datetime import datetime
import json
fn = "workOutData.json"


class Visual(object):
    def __init__(self, fn):
        self.fn = fn

    def getDMY(self, date):
        day = str(date.day).zfill(2)
        month = str(date.month).zfill(2)
        year = date.year
        return day, month, year

    def getKeyFormat(self, d, m, y):
        return f"{d}/{m}/{y}"

    def getTime(self, _dateTime=None, key=None):
        d, m, y = self.getDMY(date=_dateTime)
        return d if key == "day" else (m if key == "month" else y)

    def yesterdayData(self, data):
        pass

    def particularDayData(self, data):
        pass

    # def intervalDatabwTwoDates(self, data):
        # pass

    def processData(self, _list, data):
        for i in _list:
            dData = data[i]
            for j in dData['data']:
                if dData['data'][j] is not None:
                    if type(dData['data'][j]) is not dict:
                        print("[*] {0}: {1}".format(i,
                              "DONE" if True else False))
                    else:
                        for j in dData['data'][i]:
                            n = dData['data'][i][j][0]
                            rep = dData['data'][i][j][1]

    def todayData(self, data):
        today = datetime.now()
        d, m, y = self.getDMY(today)
        keyFormat = self.getKeyFormat(d, m, y)
        if keyFormat in data.keys():
            for i in data[keyFormat]['data']:
                if data[keyFormat]['data'][i] is not None:
                    if type(data[keyFormat]['data'][i]) is not dict:
                        print("[*] {0}: {1}".format(i,
                              "DONE" if True else False))
                    else:
                        for j in data[keyFormat]['data'][i]:
                            n = data[keyFormat]['data'][i][j][0]
                            rep = data[keyFormat]['data'][i][j][1]
                            if rep == 2:
                                n = str(n*2) + " times"
                            elif rep == 0:
                                n = str(n*1) + " min"
                            elif rep == 1:
                                n = str(n) + " times"
                            print(
                                f"[*] {i} {j} {n}")
                else:
                    print(f"[*] {i} NOT DONE.")
        else:
            print("[*] Data for today not, maybe you have to exersice now.")

    def weekData(self, data):
        _dateTime = datetime.now()
        d, m, y = self.getDMY(date=_dateTime)
        if self.getKeyFormat(d=d, m=m, y=y) in data.keys():
            index = list(data.keys()).index(self.getKeyFormat(d=d, m=m, y=y))
            list_ = list(data.keys())[:index]
            if len(list_) >= 7:
                weekList = (list[:7:-1])[::-1]
                self.processData(weekList)
            else:
                print("[*] Good expectation, but I feel you haven't made it to the week.\nContinue your hardWork, It yields the best fruit for you Oneday.")
                print(f"[*] You hold {len(list_)} days of record in my data.")
                self.processData(list_)

    def weekData(self, data):
        _dateTime = datetime.now()
        d, m, y = self.getDMY(date=_dateTime)
        try:
            data[self.getKeyFormat(d=d, m=m, y=y)]
            try:
                D = d-7
                data[self.getKeyFormat(d=D, m=m, y=y)]
                self.processData(list(data.keys())[list(
                    data.keys()).index(self.getKeyFormat(d=D, m=m, y=y)):list(
                    data.keys()).index(self.getKeyFormat(d=d, m=m, y=y))])
            except:
                self.processData(list(data.keys())[:list(
                    data.keys()).index(self.getKeyFormat(d=d, m=m, y=y))])
                # fetch the first workOutDay till d day.
        except:
            pass
            # fetchLastWorkoutDay and -7 days
        # if self.getKeyFormat(d=d, m=m, y=y) in data.keys():

    def thisWeekData():
        pass
        # from Monday : present day

    def monthData(self, data):
        pass

    def completeData(self, data):
        pass

    def visualizeData(self, fn=fn, count=0):
        if count == 3:
            print("[*] You are attempting runtime consumption, returning Execution.\n")
            return
        data = self.readData(fn)
        print("[1] Today's data.\n[2] Weeks' data.\n[3] Month's data.\n[4] complete data.\n[default] Exit.")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            self.todayData(data=data)
        elif ch == 2:
            self.weekData(data)
        elif ch == 3:
            self.monthData(data)
        elif ch == 4:
            self.completeData(data)
        else:
            print("[*] Invalid selection, reconsider your option wrt the details.")
            self.visualizeData(fn, count+1)

    def readData(self, fn=fn):
        try:
            with open(fn, "r") as f:
                data = json.load(f)
            return data if data else False
        except Exception:
            return False


x = Visual(fn)
x.visualizeData()
