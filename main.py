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

p = Path('.') # calls an unknown directory but i'm looking for downloads

p = Path('/home/lesego-blessing-segole/Downloads')

exist = p.exists() # checking if i did the right thing and if my path exists which is true, so good stuff
# logic 1, done. picked a folder

# print(f'{exist}')

# for x in p.exists(): #boolean, not iterable
#     results =  x
# print(f'{results}')

# for x in p: # poxipath, not iterable
    # print(x)

# logic 2, how do i check everything inside the downloads? looping
# but how when i cant iterate a poxipath? let's try again

# for dfiles in p:
#     if p.suffix ...

'''
wait let me think about it:
loop through the downloads path
e.g. code without full understanding of syntax: pseudo code:
for dfiles in p:
    if p is folder
    skip
    elif p is file
    read.suffix (read file extention) against extentions
    return dfiles
    
then the asking the dictionary which folder it belongs to
it looks like i'm gonna have to store the return of the suffix in a variable so we can do something like...
for ext in suffix:
    if ext == extentions
    shuti.move('/Download.suffix', 'extentions')???
    if shutil.move() === error
    path.mkdir(parents = True, exist_ok = True)

i'm still confused on the syntax and understanding but i get the gist of it
'''

# okei cool, so for the loop of the path, i have to use the right method:

for dfiles in p.iterdir():
        # if p.is_file() == True: # mistake, i'm looping through function not results
        # if dfiles.is_file() == False: # discouraged by the PEP 18 guide options: if variable: for True and if not variable: for false
        # if not dfiles.is_file: # here i'm saying if it's a folder,but i want a file
        if dfiles.is_file():
            suffix = dfiles.suffix # why is it not returning anything?
            print(f'{suffix}')
            '''
            Get the suffix
            Look up the destination
            Create the destination folder if needed
            Move the file
            '''
            # continue # here i skipped it

        # print(f'{suffix}')
            

            # pass # temporary to close the if block
        # else: # i don't know how to do the exception here
        #     pass

        '''
        for item in download folder
        first check if an item is a p.is_file()
        ignore it if p.is_dir()
        if item p.is_file == True
        return its suffix
        and check the suffix against the dictionary
        then shutil.move(p.is_file, extension)
        and then logging of what was moved to where

        i think that's how the above should go
        '''

    # except Exception:
    #     pass # i don't fully understand this exception
    # do error handling manually, the above ignores errors

    # print (f'{dfiles}') # perfect, lists every file in the download
    # now to check if it's a file or folder
    # what's the syntax to differentiate subdirs and files? subdir = p.is_dir  files = path.is_file
    # what is the syntax to ignore?


# oh yea, i meant to loop through the extentions

# for x in extensions:
#     # result = x
#     print(f'{x}') # prints every extention
#     #useless loop since i'm looking up the extention returned from the download folder, not
#     # not looping thorugh the dict to check each value, there's nothing it's doing, i have to loop around the folder

    

# print(f'{result}') # printed only the last item on the list, why?
# but that's not the point, i stored and looped through the extentions and sorted the result
# this is logic 4, too early for it but let's keep it for now



'''iterable meaning: anything i can loop over with a for loop like a list
or a string, or a dictionary'''