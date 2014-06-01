import time, json, os

#### FUNCTION DEFINITIONS
def addPause(input_data, current_time):
	data = input_data[0]['pause']
	if data is None:
		data = [{
			'start': current_time,
			'end': None,
			'duration': None
		}]
	else:
		new_pause = {
			'start': current_time,
			'end': None,
			'duration': None
		}
		data.append(new_pause)

	input_data[0]['pause'] = data
	return input_data

#### MAIN
# get files current directory
directory = os.path.dirname(__file__)

date = time.strftime("%d.%m.%Y");
current_time = time.strftime("%H:%M:%S");
data_path = directory + "/data/check_me_" + time.strftime("%d%m%y") + ".json"

with open(data_path, "r+") as data_json:
	working_time = json.load(data_json)
	data_json.seek(0)
	working_time = addPause(working_time, current_time)
	json.dump(working_time, data_json, sort_keys=True, indent=2)
	data_json.truncate()