import json
from datetime import datetime
fn = "workOutData.json"


def SelectFromMealList(FoodList):
    pass


def addFoodnDrinkData():
    # or you can design the meal wrt to time.
    FoodList = ["brocolli", "banana", "Japple", "mushroom", "chicken", "fish",
                "redMeat", "vegSalad", "fruitSalad", "greens", "beans", "nuts",
                "Jorange", "JbutterFruit", "Egg", "sweetPotato", "butter",
                "cheese", "rice", "wheatRoti", "maizeRoti", "RagiBall/Roti",
                "junks", "sweets", "liquids"]
    drinks = ["beer", "whisky", "zin", "rum", "brandy"]
    mL = [30*(i+1) for i in range(36)]
    mealTimesN = int(input("[*] How many times did you have meal today,"))
    if mealTimesN < 1:
        return -1, "today's meal data not found."
    mealData = {}
    for i in mealTimesN:
        selectMeal = SelectFromMealList(FoodList)
        # mealData[i+1] = None


class Kill(object):
    def __init__(self):
        pass

    def getDMY(self, today):
        day = str(today.day).zfill(2)
        month = str(today.month).zfill(2)
        year = today.year
        return day, month, year

    def getKeyFormat(self, d, m, y):
        return f"{d}/{m}/{y}"

    def yesterdayData(self, data):
        pass

    def particularDayData(self, data):
        pass

    # def intervalDatabwTwoDates(self, data):
        # pass

    def todayData(self, data):
        today = datetime.now()
        d, m, y = self.getDMY(today)
        keyFormat = self.getKeyFormat(d, m, y)
        if keyFormat in data.keys():
            for i in data[keyFormat]['data']:
                for j in data[keyFormat]['data'][i]:
                    print(f"{i} {j} {data[keyFormat]['data'][i][j]}")

    def weekData(self, data):
        pass

    def monthData(self, data):
        pass

    def completeData(self, data):
        pass

    def visualizeData(self, fn=fn, count=0):
        if count == 3:
            print("[*] You are attempting runtime consumption, returning Execution.\n")
            return
        data = readData(fn)
        print("[1] Today's data.\n[2] Weeks' data.\n[3] Month's data.\n[4] complete data.[default] Exit.")
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


def writeData(tData, fn):
    date = datetime.now()
    _date = f"{str(date.day).zfill(2)}/{str(date.month).zfill(2)}/{date.year}"
    time = f"{str(date.hour).zfill(2)}:{str(date.minute).zfill(2)}:{str(date.second).zfill(2)}"
    tData['updateTime'] = time
    data = readData(fn)
    if data:
        data[_date] = tData
    else:
        data = {_date: tData}
    with open(fn, "w") as f:
        json.dump(data, f)


def readData(fn):
    try:
        with open(fn, "r") as f:
            data = json.load(f)
        return data if data else False
    except Exception:
        return False


def main(tData, fn):
    date = datetime.now()
    time = f"{date.day}/{date.month}/{date.year}:{date.hour}:{date.minute}:{date.second}"
    print(f"[*] Execution startTime: {time}")
    for i in tData['data']:
        ch = input(f"[*]Are you done with {i} (y/n): ")
        if ch.lower() != 'n':
            if type(tData['data'][i]) is not dict:
                tData['data'][i] = True
            else:
                for j in tData['data'][i]:
                    try:
                        c = int(
                            input(f"[*] {j} count (default: {tData['data'][i][j][0]}): "))
                        c = tData['data'][i][j][0] if c == 1 else c
                    except:
                        c = 0
                    tData['data'][i][j][0] = c
        else:
            tData['data'][i] = False if type(
                tData['data'][i]) is not dict else None
    wCh = input("[*] WarmUp done.? (y/n)")
    w = False
    if wCh != 'n':
        w = True
    tData['data']['warmUp'] = w
    tData['CodeExecutionStartTime'] = time
    writeData(tData, fn)


if __name__ == '__main__':
    tData = {
        "data": {
            "warmUp": False,
            "chest": {
                "pushUp": [40, 1],
                "wLift": [20, 1],
                "pullUp": [12, 1]
            },
            "ArmMuscle": {
                "180degLift": [20, 1],
                "ArmV": [12, 2],
                "gravityPull": [20, 1]
                },
            "ab": {
                "militaryCrunch": [30, 1],
                "pushUpCycle": [20, 2],
                "lowerAbCrunch": [10, 1],
                "legRaiseV": [24, 2],
                "jumpRun": [3, 0],
                "skipping": [250, 2],
                "plank": [1, 0]
            },
            "leg": {
                "thighSquat": [25, 1],
                "90Kneel": [12, 2]
            }
            },
        "CodeExecutionStartTime": None,
        "updateTime": None
    }
    main(tData, fn)
