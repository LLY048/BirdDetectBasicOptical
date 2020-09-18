import subprocess as sp
import os

def mp42m3u8(ulr):
    # (1)
    # 扫描mp4目录
    #
    # l_file = os.listdir(_d_info["mp4_source"])
    # if len(l_file) < 1:
    #     d_result["errorDetail"] = "无待转换MP4文件"
    # return d_result
    # s_returnInfo = ""
    # for s_file in l_file:
    #     (filename, extension) = os.path.splitext(s_file)
    # if extension == ".mp4":
    #
    # # 开始处理
    #
    # (2)
    # ffmpeg文件放在指定目录，用python调用
    #
    # # root_path为ffmpeg的路径，file_name_path为mp4文件路径，ts_filename转换为ts的文件名
    #
    # mp4ToTs = root_path + " -y -i " + file_name_path + " -vcodec copy -acodec copy -vbsf h264_mp4toannexb " + ts_filename + ".ts"
    #
    # # 把ts转换成m3u8列表，-segment_time 10 参数表示约10秒一段视频，ts_filename为m3u8文件列表的文件名
    # tsToM3u8 = root_path + " -i " + ts_filename + ".ts -c copy -map 0 -f segment -segment_time 10 -segment_list " + ts_filename + ".m3u8 " + ts_filename + "%03d.ts"
    #
    # # 调用subprocess运行命令
    # subprocess.call(mp4ToTs, shell=True)
    # subprocess.call(tsToM3u8, shell=True)
    #
    # 命名运行成功就会在相应目录建好m3u8文件及相应的ts文件。
    #
    # 用在线播放程序直接调用m3u8文件即可实现播放。
    #
    # 问题存疑：用jqueryViDEO.js作为播放器，PC端在线播放不进行缓冲，移动端没此问题。
    pass