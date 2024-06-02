import subprocess
import os
import math
from decouple import config
from time import sleep
from moviepy.editor import VideoFileClip

from main.utils import logger

MAX_SPLIT_SIZE = config("MAX_SPLIT_SIZE", default=2*1024)

def split_video(video_path:str):
    sleep(3)
    clip = VideoFileClip(video_path)
    duration = clip.duration
    half_duration = duration / 2

    base_path, ext = os.path.splitext(video_path)
    base_path = "_".join(base_path.split())
    output_path_template = f"{base_path}_part%2d{ext}"

    file_name = video_path.split("/")[-1]
    directory = video_path.split("/")[0:-1]
    directory = "/".join(directory)
    video_path = f"{directory}/'{file_name}'"


    try:
        split_command = f"ffmpeg -i {video_path} -loglevel fatal -c copy -segment_time {half_duration} -f segment -reset_timestamps 1 {output_path_template}"
        return_code = subprocess.call(split_command, shell=True)
        if return_code != 0:
            logger.error(f"Error: ffmpeg command failed with return code {return_code}")
            return []

        sleep(3)

        video_paths = [f"{base_path}_part0{i}{ext}" for i in range(5) if os.path.exists(f"{base_path}_part0{i}{ext}")]
        return video_paths
    except:
        logger.error("Error")
        return []



def file_split_7z(file_path, split_size=MAX_SPLIT_SIZE):
        file_path_7z_list = []

        origin_file_path = ""
        if os.path.splitext(file_path)[1] == ".7z":
            origin_file_path = file_path
            file_path = os.path.splitext(origin_file_path)[0] + ".7zo"
            os.rename(origin_file_path, file_path)

        fz = os.path.getsize(file_path) / 1024 / 1024
        pa = math.ceil(fz / split_size)
        head, ext = os.path.splitext(os.path.abspath(file_path))
        archive_head = "".join((head, ext.replace(".", "_"))) + ".7z"
        for i in range(pa):
            check_file_name = "{}.{:03d}".format(archive_head, i + 1)
            if os.path.isfile(check_file_name):
                logger.debug("remove exists file | {}".format(check_file_name))
                os.remove(check_file_name)
        cmd_7z = ["7z", "a", "-v{}m".format(split_size), "-y", "-mx0", archive_head, file_path]
        proc = subprocess.Popen(cmd_7z, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate()
        if b"Everything is Ok" not in out:
            logger.error("7z output | {}".format(out.decode("utf-8")))
            logger.error("7z error | {}".format(err.decode("utf-8")))
            return file_path_7z_list

        for i in range(pa):
            file_path_7z_list.append("{}.{:03d}".format(archive_head, i + 1))

        if origin_file_path:
            os.rename(file_path, origin_file_path)
        return file_path_7z_list


def do_file_split(file_path):
        file_path_7z_list = file_split_7z(file_path)
        return file_path_7z_list

