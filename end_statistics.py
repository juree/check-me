import json, time, os

#### FUNCTION DEFINITIONS
def sec2hour(seconds):
	return time.strftime("%H ur, %M minut in %S sekund", time.gmtime(seconds))

#### MAIN
# get files current directory
directory = os.path.dirname(__file__)

date = time.strftime("%d.%m.%Y");
current_time = time.strftime("%H:%M:%S");
data_path = directory + "/data/check_me_" + time.strftime("%d%m%y") + ".json"

with open(data_path, "r") as data_json:
	working_time = json.load(data_json)
	print 'Delal si od ' + working_time[0]['start_time'] + ' do ' + working_time[0]['end_time']
	print 'To skupaj znese ' + sec2hour(working_time[0]['total_workspan'])
	print 'Brez pavz je to ' + sec2hour(working_time[0]['total_timespan'])