import json, checkmetools

#### MAIN
def run():
	current_time, date = checkmetools.getTimeDate()
	data_path = checkmetools.createPath()

	with open(data_path, "r") as data_json:
		working_time = json.load(data_json)
		working_time = working_time[0]
		print 'You worked from ' + working_time['start_time'] + ' to ' + working_time['end_time']
		print 'That means ' + checkmetools.sec2hour(working_time['total_workspan'])
		print 'Not counting pauses: ' + checkmetools.sec2hour(working_time['total_timespan'])