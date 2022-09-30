import subprocess
import shlex

queryString = 'python /smdl.py -u usernameHERE --folders "Folder-1-URL$Folder-2-URL" -o output/path/here'

subprocess.call(shlex.split(queryString))
