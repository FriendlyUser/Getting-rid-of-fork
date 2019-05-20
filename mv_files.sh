#!/usr/bin/env bash 

# Make this a parameter later
mkdir cait_music
echo "Starting to grab files"
for fullname in $(find -type f -name "*.mp4")
 do
   filename=$(basename -- "$fullfile")
   extension="${filename##*.}"
   filename="${filename%.*}"
   mp3_file="${fullname%.mp4}.mp3"
   # "ffmpeg, "-y", "-loglevel", "quiet", "-i", fname, "-vn"  mp3"
   # ffmpeg -y -loglevel quiet -i fullfile -vn mp3_file
   filename2="${f1##*/}" 
   echo ${filename2}        
   mv "${mp3_file}" cait_music || true
   mv $fullname cait_music
done