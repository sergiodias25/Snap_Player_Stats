from os import environ
import os
import platform
import sys

# ---- Constants ----

ARG_HELP_SHORT = '-h'
ARG_HELP_LONG = '--help'

ARG_TEST = '-t'
ARG_COLLECTION = '-c'
ARG_PROFILE = '-p'
ARG_SHOP = '-s'

PATH_WINDOWS = '~/AppData/Locallow/Second Dinner/SNAP/Standalone/States/nvprod/'
PATH_LINUX = '~/.steam/steam/steamapps/compatdata/1997040/pfx/drive_c/users/steamuser/AppData/LocalLow/Second Dinner/SNAP/Standalone/States/nvprod/'
PATH_MOBILE = '/sdcard/Android/data/com.nvsgames.snap/files/Standalone/States/nvprod/'
PATH_TEST = './test_data/'

FILE_COLLECTION = 'CollectionState.json'
FILE_PROFILE = 'ProfileState.json'
FILE_SHOP = 'ShopState.json'

USAGE = f"""
Usage: python3 generate_file.py [-OPTIONS]

Arguments:
    {ARG_HELP_SHORT}, {ARG_HELP_LONG}: Display this help message.
    {ARG_TEST}: Run the script in test mode.
        If this flag is included, the script will ignore the current
        system and search for all files in the `{PATH_TEST}` directory.
    {ARG_COLLECTION}: The `{FILE_COLLECTION}` file location
    {ARG_PROFILE}: The `{FILE_PROFILE}` file location
    {ARG_SHOP}: The `{FILE_SHOP}` file location
    
Defaults:
    If no arguments are provided, the script will search for the files
    in the following directories:
        - Windows: {PATH_WINDOWS}
        - Linux: {PATH_LINUX}
        - Mobile: {PATH_MOBILE}
        - Mac (AKA Darwin) or unknown: {PATH_TEST}
"""

# ---- CLI Argument Parsing ----

args = sys.argv[1:]

def getArgs():
    return args

def isTest():
    return ARG_TEST in args

def isHelp():
    return ARG_HELP_SHORT in args or ARG_HELP_LONG in args

def getArgFilePath(arg):
    if arg not in args:
        return None

    index = args.index(arg)
    filePath = args[index + 1]
    if not filePath or not filePath.endswith('.json'):
        print(USAGE)
        raise FileNotFoundError(f"File path not found: {filePath}")
    else:
        return filePath

# ---- System Detection ----

is_android = 'ANDROID_STORAGE' in environ

def isSystemWindows():
    return platform.system() == 'Windows'

def isSystemLinux():
    return platform.system() == 'Linux'

def isSystemMac():
    return platform.system() == 'Darwin'

def isSystemMobile():
    if platform.system() == 'Linux' and is_android:
        return True
    return False

# file resolution

def getFilePath(arg, fileName):
    path = ""
    argPath = getArgFilePath(arg)
    if argPath is not None:
        path = argPath
    elif isSystemWindows():
        path = PATH_WINDOWS + fileName
    elif isSystemLinux():
        path = PATH_LINUX + fileName
    elif isSystemMobile():
        path = PATH_MOBILE + fileName
    elif isTest() or isSystemMac():
        path = PATH_TEST + fileName
    else:
        print(f"Unknown system, and no path path defined for {fileName}")
        path = None
    
    return os.path.expanduser(path)

def getProfilePath():
    return getFilePath(ARG_PROFILE, FILE_PROFILE)

def getShopPath():
    return getFilePath(ARG_SHOP, FILE_SHOP)

def getCollectionPath():
    return getFilePath(ARG_COLLECTION, FILE_COLLECTION)
