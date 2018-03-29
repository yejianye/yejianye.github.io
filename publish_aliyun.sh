#!/bin/bash
echo "Build site..."
jekyll build
echo "Sync to aliyun..."
rsync --verbose  --progress --stats --compress --rsh=ssh \
     --recursive --times --perms --delete \
     _site/* ryan-aliyun:/home/ryan/blog
