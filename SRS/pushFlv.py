import subprocess
from django.conf import settings
# streamToFrame(VIDEO_URL, timeSeg, outVideoDir, reSize, fourcc)

root_path = settings.ROOT_PATH
file_name_path = settings.OUTVIDEODIR
server_address = settings.STREAMURL
# ts_filename = "partVideo"
# mp4ToTs = root_path+" -y -i "+file_name_path+" -codec copy -bsf h264_mp4toannexb -map 0 -f segment -segment_list partVideo.m3u8 -segment_time 1 "+ts_filename+".ts"
# tsToM3u8 = root_path+" -i "+ts_filename+".ts -c copy -map 0 -f segment -segment_time 10 -segment_list "+ts_filename+".m3u8 "+ts_filename+"%03d.ts"
# mp4ToServer = root_path + ' -y -i ' + file_name_path + ' -c:v copy -c:a copy -f hls -hls_flags split_by_time -hls_time 1 ../u3m8/high.m3u8'
# mp4ToServer = root_path + ' -re -y -i ' + file_name_path + ' -vcodec copy -acodec copy -f flv rtmp://'+server_address+'/live/livestream'


def pushFlv(root_path, file_name_path, server_address):
    mp4ToServer = root_path + ' -re -y -i ' + file_name_path + ' -vcodec copy -acodec copy -f flv rtmp://' + server_address + '/live/livestream'
    subprocess.call(mp4ToServer, shell=True)
    pass