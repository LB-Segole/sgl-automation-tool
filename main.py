# sgl-ops-automator
# Automates SGL's internal operations — file organisation, report generation, task scheduling. 
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