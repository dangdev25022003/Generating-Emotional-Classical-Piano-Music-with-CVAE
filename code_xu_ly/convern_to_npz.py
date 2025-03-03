# import os
# import pretty_midi
# import numpy as np
# import random

# number=random.choices([0,1,2,3],k=251)
# # Hàm chuyển đổi MIDI thành mảng numpy với kích thước cố định 64x71
# def midi_to_fixed_numpy(midi_data, num_timesteps=64, num_pitches=66):
#     notes_matrix = np.zeros((num_timesteps, num_pitches))
    
#     # Đưa các nốt vào trong phạm vi 71 pitch và 64 timestep
#     for instrument in midi_data.instruments:
#         if not instrument.is_drum:
#             for note in instrument.notes:
#                 timestep = int(min(note.start * num_timesteps / midi_data.get_end_time(), num_timesteps - 1))
#                 pitch = int(min(note.pitch - 21, num_pitches - 1))  # Giả định rằng pitch dao động từ 21 đến 91
#                 notes_matrix[timestep, pitch] = 1  # Đánh dấu pitch này đã được chơi tại timestep này
    
#     return notes_matrix

# # Thư mục chứa các file MIDI
# folder_path = 'c:/Users/LAPTOP24H/Downloads/merged_midis2_transposed_major_train'

# # Khởi tạo danh sách để chứa tất cả các mảng 64x71
# all_notes_data = []

# # Duyệt qua tất cả các tệp MIDI trong thư mục
# for filename in os.listdir(folder_path):
#     if filename.endswith('.mid'):
#         # Đọc tệp MIDI
#         file_path = os.path.join(folder_path, filename)
#         try:
#             midi_data = pretty_midi.PrettyMIDI(file_path)
#             # Chuyển đổi MIDI thành numpy array 64x71
#             note_data = midi_to_fixed_numpy(midi_data)
#             all_notes_data.append(note_data)
#         except Exception as e:
#             print(f"Không thể xử lý tệp {filename}: {e}")

# # Chuyển danh sách các mảng thành một mảng numpy với kích thước (số file, 64, 71)
# all_notes_array = np.array(all_notes_data)

# # Kiểm tra xem có đủ số lượng file không
# if all_notes_array.shape[0] == 251:
#     # Bước cuối: Lưu tất cả các dữ liệu nốt vào tệp .npz duy nhất
#     np.savez('c:/Users/LAPTOP24H/Downloads/all_midi_notes_train.npz', all_notes_array,number)
#     print(f"Hoàn thành việc lưu trữ tất cả các tệp MIDI vào all_midi_notes_251.npz với shape {all_notes_array.shape}")
# else:
#     print(f"Số lượng file chưa đủ 251, hiện tại có {all_notes_array.shape[0]} file.")



# dùng  

import os
import pretty_midi
import numpy as np

# Hàm chuyển đổi MIDI thành mảng numpy với kích thước cố định 64x66
def midi_to_fixed_numpy(midi_data, num_timesteps=64, num_pitches=60):
    notes_matrix = np.zeros((num_timesteps, num_pitches))
    
    # Đưa các nốt vào trong phạm vi 66 pitch và 64 timestep
    for instrument in midi_data.instruments:
        if not instrument.is_drum:
            for note in instrument.notes:
                timestep = int(min(note.start * num_timesteps / midi_data.get_end_time(), num_timesteps - 1))
                pitch = int(min(note.pitch - 21, num_pitches - 1))  # Giả định rằng pitch dao động từ 21 đến 86
                notes_matrix[timestep, pitch] = 1  # Đánh dấu pitch này đã được chơi tại timestep này
    
    return notes_matrix

# Đường dẫn đến 4 folder MIDI tương ứng với nhãn 0, 1, 2, và 3
folders = {
    0: 'c:/Users/LAPTOP24H/Downloads/all_4_4_secon_80BPM_major/happy_clip',
    1: 'c:/Users/LAPTOP24H/Downloads/all_4_4_secon_80BPM_major/anger_clip',
    2: 'c:/Users/LAPTOP24H/Downloads/all_4_4_secon_80BPM_major/sasness_clip',
    3: 'c:/Users/LAPTOP24H/Downloads/all_4_4_secon_80BPM_major/relax_clip'
}

# Khởi tạo danh sách để chứa tất cả các mảng 64x66 và các nhãn tương ứng
all_notes_data = []
labels = []

# Duyệt qua từng folder và nhãn tương ứng
for label, folder_path in folders.items():
    # Duyệt qua tất cả các tệp MIDI trong thư mục
    for filename in os.listdir(folder_path):
        if filename.endswith('.mid'):
            # Đọc tệp MIDI
            file_path = os.path.join(folder_path, filename)
            try:
                midi_data = pretty_midi.PrettyMIDI(file_path)
                # Chuyển đổi MIDI thành numpy array 64x66
                note_data = midi_to_fixed_numpy(midi_data)
                all_notes_data.append(note_data)
                labels.append(label)  # Gán nhãn tương ứng cho file
            except Exception as e:
                print(f"Không thể xử lý tệp {filename} trong folder {folder_path}: {e}")

# Chuyển danh sách các mảng thành một mảng numpy với kích thước (số file, 64, 66)
all_notes_array = np.array(all_notes_data)
labels_array = np.array(labels)

# Kiểm tra xem có đủ số lượng file không
if all_notes_array.shape[0] == 241:
    # Bước cuối: Lưu tất cả các dữ liệu nốt và nhãn vào tệp .npz duy nhất
    np.savez('c:/Users/LAPTOP24H/Downloads/all_midi_notes_new_train4.npz', notes=all_notes_array, labels=labels_array)
    print(f"Hoàn thành việc lưu trữ tất cả các tệp MIDI vào all_midi_notes_train.npz với shape {all_notes_array.shape}")
else:
    print(f"Số lượng file chưa đủ 251, hiện tại có {all_notes_array.shape[0]} file.")



