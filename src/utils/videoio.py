import shutil
import uuid
import subprocess
import os

import cv2

def load_video_to_cv2(input_path):
    video_stream = cv2.VideoCapture(input_path)
    fps = video_stream.get(cv2.CAP_PROP_FPS)
    full_frames = [] 
    while 1:
        still_reading, frame = video_stream.read()
        if not still_reading:
            video_stream.release()
            break 
        full_frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    return full_frames

def save_video_with_watermark(video, audio, save_path, watermark=False):
    temp_file = str(uuid.uuid4())+'.mp4'
    # os.system(cmd)
    try:
        cmd = r'ffmpeg -y -hide_banner -loglevel error -i "%s" -i "%s" -vcodec h264 "%s"' % (video, audio, temp_file)
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except:
        cmd = r'ffmpeg -y -hide_banner -loglevel error -i "%s" -i "%s" -vcodec copy "%s"' % (video, audio, temp_file)
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if not os.path.exists(temp_file):
        print("FFmpeg error")
    shutil.move(temp_file, save_path)