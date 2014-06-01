# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~ Main program wrapper ~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#
# ~~~~~ Enables program to run with outside arguments, such as project details

import sys, getopt
import start_timer, restart_timer, pause_timer, end_timer, end_statistics

# ~~~~~ FUNCTION DEFINITIONS:
def optsArgsOkay(opts, args):
	if len(opts) < 3 and len(args) < 2:
		return True
	elif '-d' in opts and len(args) is not 1:
		print 'Option -d requires argument (project name as string).'
		return False
	else:
		print 'Too many options.'
		return False 

def main(argv):
	try:
		# second is list of allowed options, third of long version options
		options, arguments = getopt.getopt(argv, "npced:", ["new", "pause", "continue", "end", "details="])
	except getopt.GetoptError as error:
		sys.exit(error)

	# exit if combination of opts and args is not okay (more than 2 opts or opt
	# '-d' with more or less than 1 arg)
	if not optsArgsOkay(options, arguments):
		sys.exit(1)

	for opt, arg in options:
		if opt in ('-n', '--new'):
			start_timer.run()
			print 'Good luck, be productive :)'
		elif opt in ('-p', '--pause'):
			pause_timer.run()
			print 'Come back soon, there is still work to do!'
		elif opt in ('-c', '--continue'):
			restart_timer.run()
			print 'I hope your batteries are full now, because there\'s some stuff you gotta finish ;)'
		elif opt in ('-e', '--end'):
			end_timer.run()
			end_statistics.run()
			print 'Well, that\'s it for now... Go get some air! :)'


# enable passing in arguments when run .argv[1:] because first element in input
# is script name
if __name__ == "__main__":
	main(sys.argv[1:])