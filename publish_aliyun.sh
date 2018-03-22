#!/bin/bash
rsync --verbose  --progress --stats --compress --rsh=ssh \
     --recursive --times --perms --delete \
     _site/* ryan-aliyun:/home/ryan/blog
