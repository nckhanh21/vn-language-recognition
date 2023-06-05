import json
import requests
import os

url = 'https://api.fpt.ai/hmi/tts/v5'

# word_list = ['chó', 'mèo', 'gà .', 'trâu', 'chim', 'mưa', 'hoa', 'cây', 'gió','nước', 'chuột', 'bò .', 'rắn', 'ếch', 'sét', 'lúa', 'ruộng', 'sáng', 'tối', 'lạnh']
word_list = ['người', 'nghĩa', 'hoàng', 'khánh']

output_folder = "mp3file"

# Tạo thư mục nếu chưa tồn tại

for word in word_list:
    payload = word
    headers = {
        'api-key': 'pihWGTkrrHvppTPSx4n7xw2kiCvKRXPv',
        'speed': '-0.5',
        'voice': 'linhsan'
    }

    response = requests.request('POST', url, data=payload.encode('utf-8'), headers=headers)
    print(response.text)

    response_json = json.loads(response.text)
    audio_url = response_json['async']
    #download audio file from url and save it to output_folder folder mp3 file
    r = requests.get(audio_url)
    filename = os.path.join(output_folder, word.replace(' ', '_')  + '.mp3')
    open(filename, 'wb').write(r.content)
    print(f"Đã lưu file âm thanh: {filename}")


# print(response.text["async"])
# print async of response
# print(json.parse(response.text)["async"])

