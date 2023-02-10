#!/bin/bash
# wget -i download.txt下载没有时间间隔，以下代码加入时间间隔
# --content-disposition 表示用服务器返回的文件名保存
while read file_url
do
    wget --content-disposition -c ${file_url}
    sleep 5
done < urls.txt

