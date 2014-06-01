import time, json, os
from datetime import datetime

#### FUNCTION DEFINITIONS
def stopPause(data, current_time):
	last_pause = data[0]['pause'][-1]
	last_pause = setDuration(last_pause, current_time)
	data[0]['pause'][-1] = last_pause
	return data

def setDuration(pause, current_time):
	# end = time.strptime(current_time, "%H:%M:%S")
	# print end
	# start = time.strptime(pause['start'], "%H:%M:%S")
	# print start
	pause['duration'] = timeDifference(current_time, pause['start'])
	pause['end'] = current_time
	return pause

def timeDifference(t_end, t_start):
    t_end = datetime.strptime(t_end, "%H:%M:%S")
    t_start = datetime.strptime(t_start, "%H:%M:%S")
    return abs((t_end - t_start).seconds)

#### MAIN
# get files current directory
directory = os.path.dirname(__file__)

date = time.strftime("%d.%m.%Y");
current_time = time.strftime("%H:%M:%S");
data_path = directory + "/data/check_me_" + time.strftime("%d%m%y") + ".json"

with open(data_path, "r+") as data_json:
	working_time = json.load(data_json)
	data_json.seek(0)
	working_time = stopPause(working_time, current_time)
	json.dump(working_time, data_json, sort_keys=True, indent=2)
	data_json.truncate()