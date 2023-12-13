from moviepy.editor import *
from datetime import datetime

def create_new_video(title):
    now = datetime.now()
    screensize = (1000,500)

    background = VideoFileClip("assets/videos/backgrounds/hearts_ballons.mp4")
    
    # TODO get text autoscaling working
    
    # text = TextClip(txt=title, color='white', bg_color='transparent', font='Comic-Sans-MS', stroke_color='black', stroke_width=5, method="label").set_position(("center","top")).set_start(0).set_duration(5)
    text = TextClip(txt=title, fontsize=100, color='white', bg_color='transparent', font='Comic-Sans-MS', stroke_color='black', stroke_width=5, size = screensize, method="caption").set_position(("center","top")).set_start(0).set_duration(5)

    picture = ImageClip("assets/pictures/spongbob_wow.png").set_start(1).set_duration(7).set_pos(("center","center"))

    final = CompositeVideoClip([background, picture, text])

    current_time = str(now.year) + str(now.month) + str(now.day) + "_" + str(now.hour) + str(now.minute) + str(now.second)
    output_name = "output/short_" + current_time + ".mp4"
    print(output_name)

    print("start")
    final.write_videofile(output_name)
    print("done")