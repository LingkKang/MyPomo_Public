# MyPomo

Type in your work and planed time, stay focused on pomodoro!

A simple progress bar will show your current timing, and when time's up, a message will prompt up on Windows notification list. 

## 1. Release Note

### 1.1. Version: 1.0.2
The first mass testable version! 

### 1.2. Update Notes

1. Check whether the icon is in same directory with exe file; 
2. Clean window command added; 
3. Work names with space(s) supported; 
4. Work time input check added; 
5. Longer work name supported. 


### 1.3. Running Requirement 
* System requirement: Windows 10 only
  * Other Windows versions are not guaranteed 
  * Other systems are not supported
* Stable connection to the Internet.


## 2. Cautious!

### 2.1. Command lines

The interface commands are listed as below:

> 
> * **-h** print help text
> * **-a** print acknowledgement : ) 
> * **-w** start your work
> * **-v --all** print all of your job list records
> * **-v --Work_Name** print specific work records(Case-sensitive!)
> * **-c** clean current window
> * **-version** view the version detail
> * **-q** quit the app
>

Type them in the running window and press **Enter** to go on. (Replace the **Work_Name** with your own work name)


### 2.2. Never Do

* Do not type any illegal characters, including:
  * English quote marks, e.g. ' or " 
  * backslashes, e.g. \ 
  * emoji or other UniCode but non-ASCII characters
    
Chinese characters are okay but not suggested, since some terminal may not support UTF-8 Encoding or UniCode Character set, the output may be unreadable. 

* Do not input work names with case inconsistency
  * E.g. 'Java' and 'JAva'
  * Or it will raise an exception and your work cannot be recorded into database. 

* Do not input work names ended with space(s)
  * Database can not read those names correctly. 
  * And may fail to retrieve data. 

* Do not leave any spaces after each command
  * Or you would get a prompt asking for retype...
  
If you find other errors unlisted, please contact me and report the bug. Many thanks. :)

### 2.3. Other Notices

* If you want to pause timing, just click anywhere in the window. Pause time could be theoretically infinite. Back to MyPomo window and press Enter to continue timing. 

* Running app on Virtual Machines or Sub-systems is not suggested
  * Doing this may cause a waste of cloud database space. 


* Having spaces or not after your work name are considered as two different items by the database automatically, be cautious on this. 


* The icon image of MyPomo should be put in the same folder with exe file. 
  * Or the notification can not function well. 
  * And the app would remind you the image is missing. 
  

* If you do not have any comment on your new work, just press **Enter** once is acceptable for convenience. And your comment will be recorded as empty. 

## 3. Upcoming Features!!

* Offline running. 
* Colored Progress bar. 
* Graphic user interface. 
* Data visualization. 
* Combine with a to-do list
* And so on... 

## 4. History Update Notes

### Version: 1.0.1
First third-party completely runnable version! 
1. Every user will have a database on cloud. 
2. Add user initialization. 


## 5. The Lib Used
(Besides Python standard libs. )

### 5.1. mysql.connector
Used to connect to MySQL server. 

### 5.2. tqdm
Used to generate a progress bar. 

### 5.3. plyer

> import plyer.platforms.win.notification
> 
> from plyer import notification

Used to generate a system notification. 

### 5.4. pyinstaller

Used to export python script as an executable file. 

