import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

# Đường dẫn đến thư mục chứa các file cần chuyển đổi
folder_path = 'mp3file'
folder_ouput = 'outdb'


listfiledir=os.listdir(folder_path)
#sort list file's time
listfiledir.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

# key = ['bò', 'chim', 'chuột', 'chó', 'cây', 'gió', 'gà', 'hoa', 'lúa', 'lạnh','mèo', 'mưa', 'nước', 'ruộng', 'rắn', 'sáng', 'sét', 'trâu', 'tối', 'ếch']
key = ['hoàng', 'khánh', 'nghĩa', 'người']



# Lặp qua tất cả các file trong thư mục và chuyển đổi định dạng
count=0
count1=0
for filename in listfiledir:
    print(filename)
    if filename.endswith('.mp3'):
        input_path = os.path.join(folder_path, filename)
        output_path = os.path.join(folder_ouput, key[count]  + '.wav')
        ffmpeg_extract_audio(input_path, output_path)
        count+=1
        print(count)

# import os
# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

# # Đường dẫn đến thư mục chứa các file cần chuyển đổi
# folder_path = 'D:\Workspace\CSDLDPT\hcsdldpt\data\data2'
# folder_ouput = 'D:\Workspace\CSDLDPT\hcsdldpt\data\data2wav'

# listfiledir=os.listdir(folder_path)
# #sort list file's time
# listfiledir.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

# key = ['cho', 'meo', 'ga', 'trau', 'chim', 'mua', 'hoa', 'cay', 'gio','nuoc', 'chuot', 'bo', 'ran', 'ech', 'set', 'lua', 'ruong', 'sang', 'toi', 'lanh']

# # Lặp qua tất cả các file trong thư mục và chuyển đổi định dạng
# count=0
# count1=0
# for filename in listfiledir:
#     print(filename)
#     if filename.endswith('.m4a'):
#         if(count%2==0):
#             input_path = os.path.join(folder_path, filename)
#             output_path = os.path.join(folder_ouput, key[count1]+ "3" + '.wav')
#             ffmpeg_extract_audio(input_path, output_path)
#             count+=1
#         else:
#             input_path = os.path.join(folder_path, filename)
#             output_path = os.path.join(folder_ouput, key[count1]+ "4" + '.wav')
#             ffmpeg_extract_audio(input_path, output_path)
#             count+=1
#             count1+=1
