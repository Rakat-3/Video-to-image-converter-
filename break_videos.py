import cv2
import os

# Input and output paths
video_folder = r"S:\2Rakat\Videos"
output_folder = r"S:\2Rakat\Videos\images"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all video files in the folder
for filename in os.listdir(video_folder):
    if filename.endswith(".mp4"):
        video_path = os.path.join(video_folder, filename)
        name_only = os.path.splitext(filename)[0]

        # Open video file
        cap = cv2.VideoCapture(video_path)
        frame_count = 0
        img_index = 1

        # Read each frame
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Optional: save every frame (you can skip some if you want fewer images)
            frame_count += 1

            # Example: save every 10th frame (you can adjust this)
            if frame_count % 10 == 0:
                img_name = f"{name_only}_{img_index}.jpg"
                img_path = os.path.join(output_folder, img_name)
                cv2.imwrite(img_path, frame)
                img_index += 1

        cap.release()
        print(f"Done extracting: {filename} -> {img_index-1} images")

print("All videos processed successfully!")
