#!/bin/bash
# wget -i urls.txt下载没有时间间隔，以下代码加入时间间隔
# --content-disposition 表示用服务器返回的文件名保存
# --cookies=on --load-cookies=cookie.txt --keep-session-cookies --save-cookies=cookie.txt 带cookie,需要提前填入cookie到cookie.txt
while read file_url
do
    wget --content-disposition -c ${file_url}
    sleep 5
done < urls.txt




