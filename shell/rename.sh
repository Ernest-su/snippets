#!/bin/bash
# 把当前文件名包含download的加后缀.torrent
for file in `ls | grep download`
do
 mv $file "${file}.torrent"
done