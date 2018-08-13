import os
import os.path
import sys
import time

if len(sys.argv) == 1:
    dir = os.getcwd()
elif len(sys.argv) == 2:
    dir = sys.argv[1]
    if not os.path.isdir(dir):
        print("{} is not a valid directory".format(dir), file=sys.stderr)
        sys.exit(1)
else:
    print("Usage: python listfiles.py [ <dirname> ]", file=sys.stderr)
    sys.exit(1)

files = os.listdir(dir)

for file in files:
    filepath = os.path.join(dir, file)
    mtime = os.path.getmtime(filepath)
    mtimeStr = time.strftime("%m-%d-%Y", time.gmtime(mtime))
    if os.path.isfile(filepath):
        info = str(os.path.getsize(filepath))
    else:
        info = "<dir>"

    print("{0} {1:10} {2}".format(mtimeStr, info, file))
