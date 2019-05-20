#!/usr/bin/env bash 

# Make this a parameter later
mkdir cait_music
echo "Starting to grab files"
for fullfile in *.mp3
 do
   filename=$(basename -- "$fullfile")
   extension="${filename##*.}"
   filename="${filename%.*}"
   mp3_file="${filename}.mp3"
   # "ffmpeg, "-y", "-loglevel", "quiet", "-i", fname, "-vn"  mp3"
   ffmpeg -y -loglevel quiet -i fullfile -vn mp3_file
   filename2="${f1##*/}" 
   echo ${filename2}        
   mv "${mp3_file}" cait_music/
done