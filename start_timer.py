import json, checkmetools

# FUNCTION DEFINITIONS
#currently under development:
def findDataFile():
	# determine if there was already work done today, e.g if checkMeOut was called,
	# so we know we have to create new file
	pass

# MAIN
def run():
	working_time = checkmetools.initDataObj()
	save_path = checkmetools.createPath()
	
	with open(save_path, "w") as save_to_file:
		json.dump(working_time, save_to_file, indent=2)