import time, json, os

# FUNCTION DEFINITIONS
#currently under development:
def createDataFile():
	# create file for json data
	pass

def findLastProject():
	# determine if there was already work done today, e.g if checkMeOut was called,
	# so we know we have to create new file
	pass

# MAIN
# get files current directory
directory = os.path.dirname(__file__)

# get current time and date, set id for today
date = time.strftime("%d.%m.%Y");
start_time = time.strftime("%H:%M:%S");
work_id = "check_me_" + time.strftime("%d%m%y")

working_time = [{
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

# filenames will be the same as data/id, so its open("data/check_me_121214.txt", "w")
save_path = directory + "/data/" + working_time[0]['id'] + ".json"
with open(save_path, "w") as save_to_file:
	json.dump(working_time, save_to_file, sort_keys=True, indent=2)