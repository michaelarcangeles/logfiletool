from datetime import datetime, timedelta

log_path = 'log_entries.txt'
out_path = 'scenario4_r3_out.txt'

# Make sure log entries are in the right order as they are below

s1 = 'addPageToDocList(0'
s2 = 'addPageToDocList(9'

def get_timediff(line1, line2):
	words1 = line1.split()
	words2 = line2.split()
	
	d1 = datetime.strptime(words1[1], '%H:%M:%S,%f')
	d2 = datetime.strptime(words2[1], '%H:%M:%S,%f')
	diff = d2 - d1
	return diff

with open(log_path, 'r') as l:
	lines = l.readlines()
	
	filtered_lines = [li for li in lines if (s1 in li or s2 in li)]
	
	if len(filtered_lines) % 2 > 0:
		print('ERROR: The total number of log entries needed for calculation should be even. This script can only compute time differences using two log entries for now.')
	
	with open(out_path, 'a+') as o:
		count = 0
		run = 1
		diffs = []
		
		while count < len(filtered_lines):
			res = get_timediff(filtered_lines[count], filtered_lines[count + 1])
			diffs.append(res)
			o.write(str(run) + '\n')
			o.write(filtered_lines[count])
			o.write(filtered_lines[count + 1])
			o.write(str(res) + '\n')
			count += 2
			run += 1
		
		average_timedelta = sum(diffs, timedelta(0)) / len(diffs)
		o.write('\nAverage: ' + str(average_timedelta))
	
	# get aver ...