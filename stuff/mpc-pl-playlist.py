import os
import cv2


def get_video_duration(file_path):
    video = cv2.VideoCapture(file_path)
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    return frame_count / fps


def format_duration(seconds):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02}:{seconds:02}"


def get_videos_sorted_by_duration(folder_path):
    videos = []
    for file in os.listdir(folder_path):
        if file.endswith(('.mp4', '.mkv', '.mov')):
            file_path = os.path.join(folder_path, file)
            duration = get_video_duration(file_path)
            videos.append((file, duration))
    return sorted(videos, key=lambda x: x[1])


folder_path = ''

sorted_videos = get_videos_sorted_by_duration(folder_path)
for n, (video, duration) in enumerate(sorted_videos, start=1):
    print(f"{n},type,0")
    print(f"{n},label,{format_duration(duration)} {video.rsplit('.', 1)[0].replace('.', ' ')}")
    print(f"{n},filename,{video}")

########################################################################################################################
# EXAMPLE:
########################################################################################################################
# MPCPLAYLIST
# 1,type,0
# 1,label,(21:03) Whose Line Is It Anyway US S16E17 1080p WEB h264-BAE
# 1,filename,Whose.Line.Is.It.Anyway.US.S16E17.1080p.WEB.h264-BAE.mkv
