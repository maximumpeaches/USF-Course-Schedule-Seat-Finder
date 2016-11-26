# Purpose
This project is intended to periodically check USF's course schedule search for open seats in a course the user would like to enroll in, and email him/her notifications of openings.

# Usage instructions
UPDATE: Things are a bit different for Selenium 3. Run `pip install -U selenium`. I (temporarily?) changed seats.py to use Chrome instead of Firefox so to get things running you have to download chromedriver from [this page](https://sites.google.com/a/chromium.org/chromedriver/downloads) and add it to the path. Firefox should also work, if you download geckodriver and it it to the path as per [these instructions](https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette/WebDriver), *but* the certificate at https://www.registrar.usf.edu/ssearch/search.php is insecure (in Firefox, but not in Chrome, for some reason) and although this shouldn't be a problem, there is [a bug](https://github.com/mozilla/geckodriver/issues/93) in selenium as of November 26, 2016 such that it does not support insecure certificates]. I was also getting some issues using Chrome where it didn't seem to load quickly enough. I haven't looked in to this problem yet so expect this script to not work like 30% of the time. The workaround until they fix the bug and we can use Firefox again is if you run the script every couple minutes then you can afford for it to not work some of the time.

This project depends on Selenium and Firefox. You can install selenium using [these directions](http://selenium-python.readthedocs.io/installation.html). I've tested this using Python 2.7 and Ubuntu 16.

To change which courses you get notifications for, enter the name of the courses one line at a time in [courses_of_interest.txt](courses_of_interest.txt) followed by the section number. So for instance courses_of_interest.txt will look something like,
```
Web Apps Design
001
Software Testing
002
```
You'll need to edit sender and receiver in [seats.py](seats.py) with the email addresses you'd like to send the from and receive the email at, respectively. Sender and receiver can be the same email, but I found it helpful to make them two separate emails so that the message would be marked as unread upon arrival in my inbox, and I would recieve a notification when receiving it. The sender I made is just a dummy email account set up for this project, and the receiver is the actual email I use.

To set up my Gmail account to work with this script I had to turn on 2-step verification for the sender using [these directions](https://support.google.com/accounts/answer/185839 "Google's instructions to set up 2-step verification").
and then create an App Password for the sender email using [these directions](https://support.google.com/accounts/answer/185834#ASPs "Google's instructions to set up an App Password").
then run `python read_app_password.py` and enter the App Password.

To run the script periodically, run [periodically.sh](periodically.sh) with the command `bash periodically.sh`. By default it runs every 70 seconds.

# Support
Please email me at maxwell.pietsch@gmail.com with any issues you're having, or send me a message through GitHub.
