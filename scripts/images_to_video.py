import os
import moviepy.video.io.ImageSequenceClip

image_folder = "C:/del/"
fps = 5

print(os.listdir(image_folder))
image_files = [
    os.path.join(image_folder, img)
    for img in os.listdir(image_folder)
    if img.endswith(".png")
]
print(image_files)
clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile("c:/delvide/my_videoTest.mp4")
