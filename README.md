# Purpose
This project is intended to periodically check USF's course schedule search for open seats in a course the user would like to enroll in, and email him/her notifications of openings.

# Usage instructions
This project depends on selenium and python. You can install selenium using [these directions](http://selenium-python.readthedocs.io/installation.html).

You can edit the courses you want to receive notifications for when seats open up by editing courses_of_interest in [seats.py](seats.py). You'll see some course names appended to courses_of_interest. You can delete lines which append courses you are not interested in, and add new lines to append courses you are interested in. You should also edit sender and receiver in the same file with the email addresses you'd like to send the from and receive the email at, respectively. Sender and receiver can be the same email, but I found it helpful to make them two separate emails so that the message would be marked as unread upon arrival in my inbox, and I would recieve a notification when receiving it. The sender I made is just a dummy email account set up for this project, and the receiver is the actual email I use.

To set up my Gmail account to work with this script I had to turn on 2-step verification for the sender using [these directions](https://support.google.com/accounts/answer/185839 "Google's instructions to set up 2-step verification").
and then create an App Password for the sender email using [these directions](https://support.google.com/accounts/answer/185834#ASPs "Google's instructions to set up an App Password").
then run `python read_app_password.py` and enter the App Password.

To run the script periodically, run [periodically.sh](periodically.sh) with the command `bash periodically.sh`. You can modify the period of time the script waits to run again by editing periodically.sh. By default it runs every 70 seconds.

# Support
Please email me at maxwell.pietsch@gmail.com with any issues you're having, or send me a message through GitHub.
