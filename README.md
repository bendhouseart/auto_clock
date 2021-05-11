# auto_clock
A script to clock in and out using crontab

Script requires one command line argument and it is either `in` or `out` this changes the subject line and content to Signing In/Signing out.

If you're working 9 to 5 you would create the following two crotabs:
# m h  dom mon dow   command
0 9 * * 1-5 /path/to/auto_clock.py in
0 17 * * 1-5 /path/to/auto_clock.py out
