from moviepy.editor import TextClip

with open('fonts.txt', 'w') as f:
    fonts_list = TextClip.list('font')
    for x in fonts_list:
        f.write(str(x) + "\n")