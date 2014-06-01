import json, checkmetools

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
def run():
	current_time, date = checkmetools.getTimeDate()
	data_path = checkmetools.createPath()

	with open(data_path, "r+") as data_json:
		working_time = json.load(data_json)
		data_json.seek(0) # file rewrite
		working_time = addPause(working_time, current_time)
		json.dump(working_time, data_json, indent=2)
		data_json.truncate() # file rewrite