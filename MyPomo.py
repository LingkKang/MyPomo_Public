#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A simple countdown timer (Pomodoro) on Windows"""

__author__ = 'Lingkang'
__author_email__ = 'karlzhu12@gmail.com'
__date__ = '2022-04-21'
__version__ = '1.0.2'
__note__ = (
    '\n \n'
    '    1. Check whether the icon is in same directory with exe file; \n'
    '    2. Clean window command added; \n'
    '    3. Work names with space(s) supported; \n'
    '    4. Work time input check added; \n'
    '    5. Longer work name supported. \n'
    )


# Import standard libs
import getpass
import sys
import time
import os

# Import third-party libs
import plyer.platforms.win.notification
from plyer import notification
import tqdm

# Import local codes
import Record
import check_user

version_detail = (
    "\n"
    "version:       {0}\n"
    "author:        {1}\n"
    "release date:  {2}\n"
    "release note:  {3}\n"
    "for more details, please refer to README document. "
    "\n".format(__version__, __author__, __date__, __note__)
)

help_text = (
    "\n"
    "-h              print help text \n"
    "-a              print acknowledgement :) \n"
    "-w              start your work \n"
    "-v --all        view all of your job list records \n"
    "-v --Work_Name  view specific work records (Case-sensitive!) \n"
    "                replace \'Work_Name\' with your own work name \n"
    "-c              clean current window \n"
    "-version        view the version detail \n"
    "-q              quit the app \n"
)

acknowledgement = (
    "\nThe icon of MyPomo comes from Cosette. "
    "Many thanks to her! "
    "Hurray!! \n"
    "\n"
    "Additionally, many thanks to ykpcx, "
    "who gives me tremendous encouragement and helps me a lot. \n"
    "\n"
    "Also, many thanks to Tember, my nice dormitory mate, "
    "who first tried my demo and gave me some great suggestions. \n"
)


print("\nHi there!")

username = getpass.getuser()
user_existence = check_user.check_user(username)
if not user_existence:
    check_user.user_initialization(username)
    print("Welcome, here is the command list to help you get familiar with MyPomo:\n")
    print(help_text)
else:
    print("Welcome back!")

userid = Record.get_user_id(username)
user_db_name = "user_{0}_{1}".format(userid, username)


def check_icon(icon_name):
    t = os.path.exists(icon_name)
    return t


def my_work():
    """Every time do a work, call the function. """
    # input
    work_name = input("\nWhat job do you want to do?\n")
    # Check work existed or not, if not, add it into database
    space = Record.check_space(work_name)
    work_name_backtick = work_name
    if space:
        work_name_backtick = Record.backtick_work_name(work_name)
    t = Record.check_existence(user_db_name, work_name)
    if not t:
        note = input("Any remarks on your new work?\n")
        Record.creat_record(user_db_name, work_name, note)
        Record.create_record_table(user_db_name, work_name_backtick)
        print("\nYour new work has been added to database!")

    # Make sure the input time is integer
    input_test = False
    while not input_test:
        try:
            work_time = int(input("\nHow long do you plan to do it (in minutes)?\n")) * 60
            input_test = True
        except ValueError:
            print("Only input an integer plz. ")

    # Starting preamble
    seconds = time.time()
    current_time = time.ctime(seconds)
    print()
    print('Start time: ', current_time)
    print('\nWorking: ', work_name)
    planed_time = time.ctime(seconds + work_time)
    print('\nPlaned finish time: ', planed_time)
    print()

    # Timing
    for i in tqdm.trange(work_time, desc=work_name):
        time.sleep(0.99)

    # Raise a notification
    if __name__ == "__main__":
        if check_icon("Tomato.ico"):
            notification.notify(
                title='Well done!',
                message='Drink some water!',
                app_name='MyPomo',
                app_icon='Tomato.ico',
                timeout=10,
            )
        else:
            notification.notify(
                title='Well done!',
                message='Drink some water!',
                app_name='MyPomo',
                timeout=10,
            )
            print(
                "It seems that the icon image was missing... \n"
                "Put it in the same folder with the exe file plz. \n"
            )

    Record.update_line(user_db_name, work_name_backtick, work_time)
    Record.update_in_all_user_list(work_time, username)
    print("\nYour current work has been registered onto database! ")


# Start
while True:
    init = input(
        "\nWhat would you like to do? \n"
        "(for more information, type '-h') \n"
    )

    try:
        if init == "-v --all":
            print("\nThis is all of your job list records. \n")
            print("Format: \nJob_ID, Job_Name, Created_Time, Total_Time, Last_Done_Time, Comment\n")
            all_data = Record.read_all_data(user_db_name)
            for j in range(len(all_data)):
                print(all_data[j])

        elif init == "-version":
            print(version_detail)

        elif init[:2] == "-v":
            job_name = init[5:]
            job_name_backtick = job_name
            if Record.check_space(job_name):
                job_name_backtick = Record.backtick_work_name(job_name)
            existence = Record.check_existence(user_db_name, job_name)
            if existence:
                print("\nHere is all of your records on work {0}. \n".format(job_name))
                print("Format: \nRecord_ID, Done_Time, Duration\n")
                one_data = Record.read_one_data(user_db_name, job_name_backtick)
                for j in range(len(one_data)):
                    print(one_data[j])
            else:
                print("There is no job called \'{0}\'... \n"
                      "Start working and it would be created automatically!".format(job_name))

        elif init == "-w":
            print("\nGreat, let\'s start working! ")
            my_work()

        elif init == "-q":
            print("\nWell, see ya! :) ")
            time.sleep(1.5)
            sys.exit()

        elif init == "-h":
            print(help_text)

        elif init == "-a":
            # print the acknowledgement
            print(acknowledgement)

        elif init == "-c":
            # Clean curren window
            os.system("cls")

        else:
            raise NameError()

    except NameError:
        print('\nNo such command {0}! \nType \'-h\' for help... '.format(init))

    except (Record.mysql.connector.errors.ProgrammingError, Record.mysql.connector.errors.DatabaseError) as err:
        print(err)
        print()
        print("Maybe you have input some illegal characters and/or case inconsistency... \n"
              "Otherwise, please report the bug to author. \n"
              "Check README for more detail. "
              )

# 4. When exported as exe...
# pyinstaller --onefile  MyPomo.py --hidden-import plyer.platforms.win.notification --icon Tomato.ico
