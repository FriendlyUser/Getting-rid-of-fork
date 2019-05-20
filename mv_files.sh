#!/usr/bin/env bash 

# Make this a parameter later
mkdir -p cait_music
for f1 in *.mp3
 do
   filename2="${f1##*/}" 
   echo ${filename2}        
   mv "${f1}" cait_music/
done