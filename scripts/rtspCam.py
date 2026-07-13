import cv2
import numpy as np

# RTSP URLs
rtsp_urls = [
    "rtsp://172.22.215.144:8080/h264_opus.sdp",
    "rtsp://192.0.0.4:8080//h264_opus.sdp"
]

caps = [cv2.VideoCapture(url, cv2.CAP_FFMPEG) for url in rtsp_urls]

# Check streams
for i, cap in enumerate(caps):
    if not cap.isOpened():
        print(f"❌ Error: Unable to open Camera {i+1}")
        exit()
    else:
        print(f"✅ Camera {i+1} opened successfully")

while True:
    frames = []

    for cap in caps:
        ret, frame = cap.read()
        if not ret:
            frame = np.zeros((480, 640, 3), dtype=np.uint8)  # fallback black frame
        frames.append(frame)

    # Resize frames to same height
    height = 480
    resized_frames = [
        cv2.resize(frame, (int(frame.shape[1] * height / frame.shape[0]), height))
        for frame in frames
    ]

    # Combine side-by-side
    combined_frame = np.hstack(resized_frames)

    cv2.imshow("RTSP Cameras - Side by Side (Press Q to exit)", combined_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
for cap in caps:
    cap.release()

cv2.destroyAllWindows()
