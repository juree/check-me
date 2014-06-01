# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ CheckMeTools module ~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#
# ~~~~~ Often used functions in CheckMeProjects
import time, os
from datetime import datetime

# intialize data object that will later be converted to json
def initDataObj(project_name=None):
	# get current time and date, set id for today
	start_time, date = getTimeDate()
	work_id = createID()

	data_obj =	[{
					'date': date,
					'start_time': start_time,
					'end_time': None,
					'project': None,
					'pause': None,
					'total_workspan': None,
					'total_timespan': None,
					'id': work_id,
					'code_statistics': None
				}]

	return data_obj

def createID():
	return "check_me_" + time.strftime("%d%m%y")

def createPath():
	directory = os.path.dirname(__file__)
	data_path = directory + "/data/check_me_" + time.strftime("%d%m%y") + ".json"
	return data_path

def getTimeDate():
	# get current time and date
	c_time = time.strftime("%H:%M:%S")
	c_date = time.strftime("%d.%m.%Y")
	return c_time, c_date

##
# input t_end, t_start: string as H:M:S
# return int: difference between times in number of seconds
def timeDifference(t_end, t_start):
    t_end = datetime.strptime(t_end, "%H:%M:%S")
    t_start = datetime.strptime(t_start, "%H:%M:%S")
    return abs((t_end - t_start).seconds)

def sec2hour(seconds):
	return time.strftime("%H hours, %M minutes and %S seconds", time.gmtime(seconds))