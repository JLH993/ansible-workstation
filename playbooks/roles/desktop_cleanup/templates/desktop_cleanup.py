#!/usr/bin/env python
# Written by: Robert J.
# Email:      robert@scriptmyjob.com

import sys
import os
import re
import logging
from time import sleep

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG
)

logger = logging.getLogger()

#######################################
### Main Function #####################
#######################################

def main():
    home_dir    = os.environ['HOME']
    desktop     = os.path.join(home_dir, 'Desktop')
    temp_dir    = os.path.join(home_dir, 'Pictures/Temp')
    pattern     = 'Screen.*\.png'
    pictures    = get_pictures(desktop, pattern)

    if pictures:
        move_items(pictures, desktop, temp_dir)
        archive_old_pictures(temp_dir, pattern)


#######################################
### Generic Functions #################
#######################################

def move_items(items, source, destination):
    if not os.path.isdir(destination):
        logger.info('Creating directory: "{0}"'.format(destination))
        os.makedirs(destination)

    for i in items:
        source_file = os.path.join(source, i)
        dest_file   = os.path.join(destination, i)

        logger.info('Moving "{0}" to "{1}"'.format(source_file, dest_file))
        os.rename(source_file, dest_file)


#######################################
### Program Specific Functions ########
#######################################

def get_pictures(directory, pattern):
    pictures = [
        p for p in os.listdir(directory) if re.match(pattern, p)
    ]

    if pictures:
        logger.info('Found items to move: ' + str(pictures))

    return pictures


def archive_old_pictures(temp_dir, pattern):
    pictures = get_pictures(temp_dir, pattern)

    old_pictures = [
        os.path.split(o)[1] for o in sorted(
            [
                os.path.join(temp_dir, p) for p in pictures
            ],
            key=os.path.getmtime
        )
    ][:-5]

    for op in old_pictures:
        dest = temp_dir.strip('Temp') + op.split(' ')[2]
        src  = temp_dir

        move_items([op], src, dest)


#######################################
### Execution #########################
#######################################

if __name__ == "__main__":
    logger.info('Starting Desktop Cleanup Daemon.')

    while True:
        try:
            main()
            sleep(1)
        except KeyboardInterrupt, e:
            print('\n')
            logging.info("Stopping Desktop Cleanup Deamon per user input.")
            break
