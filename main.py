from code.create_video import create_new_video
from code.create_tts import create_new_tts_file

# text = str(input())
# text_list = list(['test', 'test2', 'this is a sentence'])
# print(text_list)

# for text in text_list:
#     create_new_video(text)
    
print("Title: ")
title = str(input())
create_new_tts_file(title)
create_new_video(title)
