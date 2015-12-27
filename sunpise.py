#!/usr/bin/python

# SunpPise
# Caleb Gross
#
# A Raspberry Pi (Model B) grabs the sunrise time from the web, and
# records a timelapse of the sunrise each morning. It then posts the
# timelapse to a YouTube channel where others can view it.
#
# Uses:
# - Raspberry Pi Model B
# - Raspberry Pi Camera Module
# - crontab
# - Wi-Fi module
#
# Dependencies:
# - raspistill
# - mencoder
# - youtube-upload

from functions import *

def main():
	print('=================================')
	print('==========',datetime.now().strftime('%d %b %Y'),'==========')
	print('=================================')
	capture_interval = 1000	                 # still interval in ms
	event_times = get_event_times()          # 1) get sunrise times
	for key in event_times:
		print(key + ':',event_times[key])
	print("now:",datetime.now())
	wait_until_dawn(event_times['dawn'])     # 2) wait until sunrise
	# capture(event_times, capture_interval) # 3) get pics
	# stitch()                               # 4) create timelapse
	# upload()                               # 5) upload to YouTube
	# cleanup()                              # 6) delete files
	# print('Done at',datetime.strftime('%H:%M', localtime()),'\n')

	# testing
	# test_times = {'dawn': u'18:23', 'sunshine': u'19:23'}
	# print(test_times)
	# wait_start(test_times, capture_interval)

if __name__ == "__main__":
    main()
