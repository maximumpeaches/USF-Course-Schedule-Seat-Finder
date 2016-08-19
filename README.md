# Purpose
This project is intended to periodically check USF's course schedule search for open seats in a course the user would like to enroll in, and email him/her notifications of openings.

# Usage instructions
This project depends on selenium and python. You can install selenium using [these directions](http://selenium-python.readthedocs.io/installation.html).

You can edit the courses you want to receive notifications for when seats open up by editing courses_of_interest in [seats.py](seats.py). You should also edit sender and receiver in the same file with the email addresses you'd like to send the from and receive the email at, respectively. This can be the same email, but I found it helpful to make it two separate emails so that the message would be marked as unread upon arrival in my inbox, and I would recieve a notification when receiving it. The sender I made is just a dummy email account set up for this project, and the receiver is the actual email I use.

To set up my Gmail account to work with this script I had to turn on 2-step verification for the sender using [these directions](https://support.google.com/accounts/answer/185839 "Google's instructions to set up 2-step verification").
and then create an App Password for the sender email using [these directions](https://support.google.com/accounts/answer/185834#ASPs "Google's instructions to set up an App Password").
then replace the app_password variable in [seats.py](seats.py) with the App Password.
