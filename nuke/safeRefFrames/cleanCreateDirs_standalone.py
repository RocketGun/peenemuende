#!/usr/bin/python
# 
# create missing folders / clean-up render folders
#
# Last Edit: 29/10/10 SME

import os, sys

def create_missing_dirs(d, do_clean=True):
    # extract last path elements for cleanup-check
    d_base = os.path.basename(d)  
                                       
    if ((not os.path.exists(d)) and (d != "")):
        print "Creating directory: " + d
        os.makedirs(d) 

    elif ((os.path.exists(d)) and (d != "")):
        if (not do_clean):
            return

        # - path must exist
        # - path cannot be empty

        # delete files recursively
        print "started cleaning routine for basename " + d_base

        try:
          for f in os.listdir(d):
            print ("Now unlinking %s/%s...") % (d, f) 
            os.unlink(("%s/%s") % (d, f)) 
            
        except:
            print ("Error cleaning folder %s") % (d)
            
# END: def
    
if (len(sys.argv) < 3):
    print "Not enough arguments!"
    print ""
    print "USAGE:"
    print "[python] cleanCreateDirs_standalone.py ShotName ProjectBasePath [DoClean = on/off]"
    
    sys.exit(1)

shot = sys.argv[1]
project_path = sys.argv[2]

try:
    t = sys.argv[3]
except:
    t = ""

if (t == "on"):
    doclean = True
else:
    doclean = False

# let's at least check the project_path for len > 19
# since: filmserver + / + DATE[6] + _ + x    =    19

if (len(project_path) < 19):
    print "Invalid project path detected! Terminating."
    sys.exit(1)
    
# build paths needed
# creating missing folders on user creation

shotout = ("%s/output/shot_out/%s") % (project_path, shot)
latestout = ("%s/output/versions/%s/_latest") % (project_path, shot)

# commit
create_missing_dirs(shotout, doclean)
create_missing_dirs(latestout, doclean)            
