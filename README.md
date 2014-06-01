### README file for CheckMe

# CheckMe coding statistics project

## Description:
CheckMe is a hobby project that let's you follow your coding statistics, such as time spent working on a certain project or code changes (if using git). In it's current state it is useful on Linux Ubuntu. I just started developing it so it's far from perfect. If you want to use it please take a look of README.

## Project status:
It works on Ubuntu. Currently it can track time spent working, including pauses. I'm currently working on coding statistics, so it will be able to track your codebase - how much code did you create/edit during given time period.

#### Current functionality:
- track time spent working in a day (but you have to start and end just once in a day, if you are having pauses you need to use options -p and -c, otherwise your previous data for this day will be overwritten)
- subtract pauses from from full timespan
- when you stop working displays time statistics (in Terminal)
- saves data in json format, so you can use it in other applications (view exact data structure at the bottom of this document)

#### Work in progress:

Feature | Coming sometime until
------- | ---------------------
Track code statistics (if using git) | 8th June
Multiple starts and stops in a day (which means multiple projects) | 8th June

- *Please note that this is my current projection and can change at any given time*

## Setup:
Move all the files in this repo to you prefered directory such as ~/path/to/CheckMe. In this directory create new directory named 'data' (~/path/to/CheckMe/data). There are currently two ways to use it.

#### Basic usage:
In terminal run following command (where opt is one of several options, see them in table bellow):

```bash
python ~/path/to/CheckMe/checkMe.py -opt
```

Option | Long option | Argument
-------|-------------|---------
-n | --new | none
-d | --details | string with project name
-p | --pause | none
-c | --continue | none
-e | --end | none

- *Please note that -d option should only be used together with -n, like this:*
```bash
python ~/path/to/CheckMe/checkMe.py -nd 'project name string'
```

#### Usage with bash aliases:
Add following lines to .bash_aliases (**Be careful: change ~/path/to/CheckMe to the right directory!** Also feel free to change alias names):
```bash
#~~~~~~~~~~ CheckMe project aliases: ~~~~~~~~~~

#~~~~~ checkMeIn: start work on a project
alias checkMeIn='python ~/path/to/CheckMe/checkMe.py -n &' # full option: --new

#~~~~~ checkMePause: make pause on a project, such as for lunch or coffe break
alias checkMePause='python ~/path/to/CheckMe/checkMe.py -p &' # full option: --pause

#~~~~~ checkMeContinue: end pause
alias checkMeContinue='python ~/path/to/CheckMe/checkMe.py -c &' # full option: --continue

#~~~~~ checkMeOut: finish work on a project and display statistics
alias checkMeOut='python ~/path/to/CheckMe/checkMe.py -e &' # full option: --end
```

## Data format:
Script saves data as *check_me_ddmmyy.json* in data directory. **Dates** are saved as strings in format *dd.mm.yyyy*, **time** as strings in format *hh:mm:ss*. Exceptions are **duration** fields which are saved as integers which mean number of seconds spent working.

Data structure will certainly be subject to change. Currently it looks like this:
```json
[
  {
    "project": "some_project",  
    "id": "check_me_310514",
    "date": "31.05.2014",
    "start_time": "22:20:57", 
    "end_time": "22:51:11",
    "total_timespan": 1772, 
    "total_workspan": 1814, 
    "pause": [
      {
        "duration": 17, 
        "end": "22:21:25", 
        "start": "22:21:08"
      }, 
      {
        "duration": 5, 
        "end": "22:21:40", 
        "start": "22:21:35"
      }, 
      {
        "duration": 20, 
        "end": "22:50:17", 
        "start": "22:49:57"
      }
    ]
  }
]
```

## Contribute:
If you would like to contribute to project or just have comments/suggestions please feel free to contact me at dvlp.chan@gmail.com