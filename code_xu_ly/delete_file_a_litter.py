import os

# Đường dẫn đến thư mục chứa các tệp MIDI
midi_folder_path = 'c:/Users/LAPTOP24H/Downloads/nhac beeth/buon_4_4_clip/adjusted_16752'

# Duyệt qua tất cả các thư mục và tệp trong thư mục và các thư mục con
for root, dirs, files in os.walk(midi_folder_path):
    for midi_filename in files:
        if midi_filename.endswith('.mid'):  # Kiểm tra xem tệp có phải là tệp MIDI không
            midi_file_path = os.path.join(root, midi_filename)

            # Lấy kích thước tệp (tính bằng byte)
            file_size = os.path.getsize(midi_file_path)

            # Kiểm tra nếu kích thước tệp nhỏ hơn hoặc bằng 12KB (12 * 1024 byte)
            if file_size <=  1024:
                # Xóa tệp
                os.remove(midi_file_path)
                print(f"Deleted {midi_filename} from {root}, size was {file_size} bytes")

print("Finished cleaning up small MIDI files.")
