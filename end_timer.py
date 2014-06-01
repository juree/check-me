import time, json, OS
from datetime import datetime

#### FUNCTION DEFINITIONS
def endTimer(data, current_time):
	start = data[0]['start_time']
	pause = data[0]['pause']

	total_workspan = timeDifference(current_time, start)
	total_timespan = total_workspan - computeTotalPause(pause)
	
	data[0]['total_workspan'] = total_workspan
	data[0]['total_timespan'] = total_timespan
	data[0]['end_time'] = current_time

	return data

def timeDifference(t_end, t_start):
    t_end = datetime.strptime(t_end, "%H:%M:%S")
    t_start = datetime.strptime(t_start, "%H:%M:%S")
    return abs((t_end - t_start).seconds)

def computeTotalPause(pause_obj):
	if pause_obj is None:
		return 0
	else:
		total = 0
		for pause in pause_obj:
			total += pause['duration']
		return total

#### MAIN
# get files current directory
directory = os.path.dirname(__file__)

date = time.strftime("%d.%m.%Y");
current_time = time.strftime("%H:%M:%S");
data_path = directory + "/data/check_me_" + time.strftime("%d%m%y") + ".json"

with open(data_path, "r+") as data_json:
	working_time = json.load(data_json)
	data_json.seek(0)
	working_time = endTimer(working_time, current_time)
	json.dump(working_time, data_json, sort_keys=True, indent=2)
	data_json.truncate()