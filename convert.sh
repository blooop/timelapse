#!/bin/bash
STEP_SECONDS=60
# ffmpeg -framerate ${1/STEP_SECONDS} -pattern_type glob -i "*.jpg" -vf -r 60 output.mp4



# ffmpeg -framerate ${1/STEP_SECONDS} -pattern_type glob -i "*.jpg" -vf "tblend=all_mode=average,drawtext=text='%{pts\:hms}':x=w-tw-10:y=h-th-10:fontsize=24:fontcolor=white" -r 60 output.mp4


# STEP_SECONDS=60; ffmpeg -framerate 1/$STEP_SECONDS -pattern_type glob -i 'tmp/*.jpg' -vf "tblend=all_mode=average,drawtext=text='%{pts\:hms}':x=w-tw-10:y=h-th-10:fontsize=24:fontcolor=white" -r 60 output.mp4



# STEP_SECONDS=60; ffmpeg -framerate 1/$STEP_SECONDS -pattern_type glob -i 'tmp/*.jpg' -vf "tblend=all_mode=average,drawtext=text='%{pts\:hms}':x=w-tw-10:y=h-th-10:fontsize=24:fontcolor=white" -r 60 output.mp4


ffmpeg -framerate 60 -pattern_type glob -i 'run3/*.jpg' -vf "tblend=all_mode=average,framestep=2,drawtext=text='%{pts\:hms}':x=w-tw-10:y=h-th-10:fontsize=24:fontcolor=white,setpts=0.35*PTS" -r 60 run3.mp4



ffmpeg -framerate 60 -pattern_type glob -i 'run3/*.jpg' -vf "tblend=all_mode=average,framestep=2" -r 60 run3.mp4