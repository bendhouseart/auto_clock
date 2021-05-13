# auto_clock
A script to clock in and out using crontab

Script requires one command line argument and it is either `in` or `out` this changes the subject line and content to Signing In/Signing out.

First copy the sample.env to a .env file:

```bash
cp sample.env .env
```

Then fill out the values in your `.env` file to suite:
```bash
sender_email=senderemail@domain
receiver_email=receiveremail@domain
email_password=1234justlikemyluggage
port_number=9999
mail_server=mail.yourmailserver.domain
```


If you're working 9 to 5 you would create the following two crontabs:
```bash
# m h  dom mon dow   command
0 9 * * 1-5 /path/to/auto_clock.py in
0 17 * * 1-5 /path/to/auto_clock.py out
```

