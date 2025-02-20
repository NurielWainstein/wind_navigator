import cv2
import os


def create_video_from_images(image_folder, output_video_file, fps=10):
    # Get all the images in the folder, sorted by their filename
    images = [f for f in os.listdir(image_folder) if f.endswith('.png')]
    images.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))  # Sort based on frame number

    # Check if images are available
    if not images:
        print("No images found in the folder.")
        return

    # Get the size of the images
    first_image = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = first_image.shape

    # Initialize the video writer (output MP4 file)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 file
    video = cv2.VideoWriter(output_video_file, fourcc, fps, (width, height))

    # Add each image to the video
    for image_file in images:
        image_path = os.path.join(image_folder, image_file)
        img = cv2.imread(image_path)
        video.write(img)

    # Release the video writer and close the video file
    video.release()
    print(f"Video saved as {output_video_file}")


# Usage
image_folder = 'images/'  # Folder containing your images
output_video_file = 'output_video.mp4'  # The name of the output video
fps = 30  # 0.1 second delay means 10 frames per second (fps)
create_video_from_images(image_folder, output_video_file, fps)
