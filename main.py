# sgl-ops-automator
# Automates SGL's internal operations: file organisation, report generation, task scheduling. 
# You're building the company's infrastructure while learning automation.

# what the hell are we doing here?

# goal: a script that fully automates everything in SGL Developments
# the nitty gritties are in the vision

# let's start

###### Imports ######
''' what do we need to import?
path and shutil
os
what else? check documentation/ handbook...
okei, first create one. okei had one, just didn't save
cool.. imports
os, path, datetime(duh),
json read data, schedule,
logging,
shutil (taking action on files), 
time (schedule loop)
best practice use path for defining and manipulating paths
and shutil to perform actions on those paths
'''

import os # access to file system
import shutil
from pathlib import Path # file path handling

# hajime!

'''
i've never been so confused in my life, wow
let's watch a youtube video at least
my mistake, i didn't define what i'm gonna be doing for version one and how it works in favour for the final version
defined: the first version; for me, focuses in the downloads path since it holds most of the different file extensions
data structure: dict over list for file extentions (so damn cool learning this) DRY principle: Do Not Repeat Yourself
and the idea of a single source of truth: the dict is one authoritative table of "extension → folder," whereas the list
approach scatters that same fact across several variables plus the order of your if chain
now for the code
'''

# extensions = {
#     '.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx': 'Documents'
# }

# method for storing sets in dictionary is different

# if/ dict comprehension/ defaultdict(set)/ dict.setdefault() 

# most efficient method is defaultdict(set) - okei hsit, still poses the same
# problem as the lsit, we drop it and focus on writing each extension one by one

extensions = {
    # Text and Document Files -> Documents
    '.txt': 'Documents',
    '.doc': 'Documents',
    '.docx': 'Documents',
    '.pdf': 'Documents',
    '.rtf': 'Documents',
    '.odt': 'Documents',
    '.csv': 'Documents',

    # Image Files -> Pictures
    '.jpg': 'Pictures',
    '.jpeg': 'Pictures',
    '.png': 'Pictures',
    '.gif': 'Pictures',
    '.bmp': 'Pictures',
    '.svg': 'Pictures',
    '.tiff': 'Pictures',
    '.tif': 'Pictures',
    '.psd': 'Pictures',

    # Audio and Video Files -> Media
    '.mp3': 'Media',
    '.wav': 'Media',
    '.wmv': 'Media',
    '.mp4': 'Media',
    '.avi': 'Media',
    '.mov': 'Media',
    '.flv': 'Media',

    # Executable and System Files -> Programs
    '.exe': 'Programs',
    '.dll': 'Programs',
    '.sys': 'Programs',
    '.bat': 'Programs',
    '.sh': 'Programs',
    '.msi': 'Programs',
    '.com': 'Programs',

    # Programming and Web Files -> Code
    '.html': 'Code',
    '.htm': 'Code',
    '.css': 'Code',
    '.js': 'Code',
    '.py': 'Code',
    '.java': 'Code',
    '.c': 'Code',
    '.cpp': 'Code',
    '.php': 'Code',

    # Archive and Data Files -> Archives
    '.zip': 'Archives',
    '.rar': 'Archives',
    '.7z': 'Archives',
    '.tar': 'Archives',
    '.db': 'Archives',
    '.dbf': 'Archives',
    '.xml': 'Archives',
    '.json': 'Archives',
}

'''
list of extentions done called: extensions
now what do i do?
i need to check in the downloads folder
do a search in it for the specific extention i'm looking for
then put it in my desired folder
does that mean i have to retype each extension?
which one is more important? speed or easiness of code
or how easily i can code? speed makes sense in the long run 
and for editing in future
okei cool, let's do the steps


how the hell do i check? 
okei what import allows me to go through my file path on the computer?
PATH? I believe, nah it's os or is os what allows path to work?
looking at the handbook it seems so
under Path is pathlib, which a modern path handling
i actually don't understand shit here wow
there's too much happening, unix, windows, pureposixpath, pureqindospath
i actually don't understand how file handling works on the basic level
never used os, so that's the gap
'''

'''
Logic:
Pick folder
Check everything inside it: looping
for each item in download, decide if it's a folder or file (leave folders alone)
for each file read it's extention (.suffix)
ask my dictionary 'extensions' which folder does the suffix belong to
ensure the destination folder exists, but have logic if file destination does not exist
move file there
handle odd cases, file with two same names, file already exists, file with no extension, hidden dotfile etc
'''

p = Path('.')

