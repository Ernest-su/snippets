# coding:utf-8
# author--sakala--
# 1. 适用于create_link大包内文件夹无排名序号 python3 create_link.py -p 大包路径
#    大包内文件夹有排名序号。如001.dir python3 create_link.py -p 大包路径 -l 4
# 2. 在跟大包同目录下新建一个文件夹reseed，把这个脚本放进去，执行脚本，在脚本所在的这个新目录(reseed)下生成递归生成大包内的文件夹，创建文件硬链接
# 3. 在reseed文件夹下执行杯具大佬的reseed.py脚本，得到json文件，拿去网站上传json文件解析得到下载链接列表，保存成urls.txt
# 4.（可选操作）为了方便，可以把这个新文件夹里的文件移动（剪切）到跟大包同目录的父文件夹
# 5. qbittorrent使用urls.txt下载种子文件。如果已经执行第4步操作，保存路径就是大包所在的父目录。

# 例如：dir = "/data/imdb250-FRDS"
# 此时文件夹结构如下
# /data
# ----imdb250-FRDS
# --------sub1.MNHD-FRDS 
# ----------- sub1.mkv
# --------sub2.MNHD-FRDS 
# ----------- sub2.mkv
# ----其他文件或文件夹

# 在/data内创建一个文件夹reseed,把这个脚本复制进新建的文件夹reseed.执行后，此时文件夹结构如下
# /data
# ----imdb250-FRDS
# --------sub1.MNHD-FRDS 
# ----------- sub1.mkv
# --------sub2.MNHD-FRDS 
# ----------- sub2.mkv
# ----reseed
# --------create_link.py
# --------sub1.MNHD-FRDS 
# ----------- sub1.mkv   -----这个文件是硬链接，不多占空间
# --------sub2.MNHD-FRDS 
# ----------- sub2.mkv   -----这个文件是硬链接，不多占空间
# ----其他文件或文件夹

#（可选操作）把reseed文件夹的内容移动到/data
# 移动后，此时文件夹结构如下
# /data
# ----imdb250-FRDS
# --------sub1.MNHD-FRDS 
# ----------- sub1.mkv
# --------sub2.MNHD-FRDS 
# ----------- sub2.mkv
# ----reseed
# --------create_link.py
# ----sub1.MNHD-FRDS 
# --------sub1.mkv   -----这个文件是硬链接，不多占空间
# ----sub2.MNHD-FRDS 
# ------- sub2.mkv   -----这个文件是硬链接，不多占空间
# ----其他文件或文件夹


import argparse
import os
import platform


def create_dir(dir):
   finddir = []
   l = len(dir)
   for maindir, subdir, file_name_list in os.walk(dir):
       finddir.append(maindir[l+1:][split_length:])
   for i in finddir:
       if i:
           if not os.path.exists(i):
               os.mkdir(i)
               print("*********mkdir:%s" % i)


def shell_quote(s):
   return "'" + s.replace("'", "'\\''") + "'"


def create_link(dir):
   newfile = []
   for maindir, subdir, file_name_list in os.walk(dir):
       for filename in file_name_list:
           source_path = os.path.join(maindir, filename)  # 合并成一个完整路径
           target_path = os.path.join(path, work_dir, maindir[l+1:][split_length:], filename)
           if linux_mode:
               source_path = shell_quote(source_path)
               target_path = shell_quote(target_path)
           newfile.append([source_path, target_path])
   for i in newfile:
       if linux_mode:
           print("ln {source} {target}".format(source=i[0], target=i[1]))
           os.system("ln {source} {target}".format(source=i[0], target=i[1]))
       else:
           os.system("mklink /H \"{target}\" \"{source}\"".format(source=i[0], target=i[1]))


if __name__ == "__main__":
   parser = argparse.ArgumentParser()
   parser.add_argument('-l', '--length', help="要去掉的前置字符的长度，默认0", default=0, type=int)
   parser.add_argument('-p', '--path', help="创建硬链接的源路径", required=True)
   args = parser.parse_args()
   print("*********\n不支持跨盘创建硬链接，硬链接不占空间大小，请直接保证同盘不同路径下运行次脚本\n请不要在win下通过"
         "smb挂载unix的盘执行脚本，虽然不会损坏数据\n*********输入任意字符继续")
   try:
       a = input()
   except SyntaxError:
       pass
   linux_mode = True
   path = os.getcwd()
   if (platform.system() == 'Windows'):
       linux_mode = False
       print('*********当前系统为Windows')
   elif (platform.system() == 'Linux'):
       print('*********当前系统为Linux')
   dir = args.path
   split_length = args.length
   print(dir)
   if dir[-1] == "/":
       dir = dir[:-1]
   if dir in path:
       raise Exception("*********请勿在子路径下运行脚本")
   if not dir:
       raise Exception("*********请指定要创建的源文件夹路径")
   work_dir = os.path.split(dir)[-1]
   l = len(dir)
   if not os.path.exists(work_dir):
       os.mkdir(work_dir)
       print("*********在当前路径创建同名目录:%s" % work_dir)
   os.chdir(os.path.join(path, work_dir))
   create_dir(dir)
   create_link(dir)
   print("*********运行完毕*********")

