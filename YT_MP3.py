#!/usr/bin/env python
# coding: utf-8

# In[5]:


# importing packages
from pytube import YouTube
import os
  
# url input from user
yt = YouTube(input("請輸入影片地址"))
  
# extract only audio
video = yt.streams.filter(only_audio=True).first()
  
# check for destination to save file
print("請輸入存檔地址")
destination = str(input(">> ")) or '.'
  
# download the file
out_file = video.download(output_path=destination)
  
# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
  
# result of success
print(yt.title + " has been successfully downloaded.")

