import subprocess

# Path ke video lokal
video_path = "video/video_mu.mp4"

# RTMP endpoint YouTube
rtmp_url = "rtmp://a.rtmp.youtube.com/live2"
stream_key = "GANTI_DENGAN_STREAM_KEY_KAMU"

def start_stream():
    command = [
        "ffmpeg",
        "-re",
        "-stream_loop", "-1",
        "-i", video_path,
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-maxrate", "3000k",
        "-bufsize", "6000k",
        "-pix_fmt", "yuv420p",
        "-g", "50",
        "-c:a", "aac",
        "-b:a", "128k",
        "-f", "flv",
        f"{rtmp_url}/{stream_key}"
    ]

    subprocess.call(command)

if __name__ == "__main__":
    print("Mulai streaming ke YouTube...")
    start_stream()
