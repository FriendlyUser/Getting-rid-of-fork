#!/usr/bin/env bash 

# Make this a parameter later
mkdir cait_music
ls
echo "Starting to grab files"
find . -type f -name "*.mp4" -print0 | while IFS= read -r -d '' fullfile;
 do
   echo $fullfile
   # filename=$(basename -- "$fullfile")
   extension="${fullfile##*.}"
   filename="${fullfile%.*}"
   echo $filename
   mp3_file="${fullfile%.*}.mp3" 
   echo "$mp3_file"
   # "ffmpeg, "-y", "-loglevel", "quiet", "-i", fname, "-vn"  mp3"
   ffmpeg -y -loglevel quiet -i -nostdin "$fullfile" -vn "$mp3_file" 
   filename2="${f1##*/}" 
   echo ${filename2}        
   # mv "$mp3_file" cait_music || true
   # mv "$fullname" cait_music || true
done
cd cait_music
echo "Files in Cait music are"
ls 
cd ../
echo "Files in main directory are"
ls
