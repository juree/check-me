import json, checkmetools

#### FUNCTION DEFINITIONS
def stopPause(data, current_time):
	last_pause = data[0]['pause'][-1]
	last_pause = setDuration(last_pause, current_time)
	data[0]['pause'][-1] = last_pause
	return data

def setDuration(pause, current_time):
	pause['duration'] = checkmetools.timeDifference(current_time, pause['start'])
	pause['end'] = current_time
	return pause

#### MAIN
def run():
	current_time, date = checkmetools.getTimeDate()
	data_path = checkmetools.createPath()

	with open(data_path, "r+") as data_json:
		working_time = json.load(data_json)
		data_json.seek(0) # used to rewrite file
		working_time = stopPause(working_time, current_time)
		json.dump(working_time, data_json, indent=2)
		data_json.truncate() # used to rewrite file