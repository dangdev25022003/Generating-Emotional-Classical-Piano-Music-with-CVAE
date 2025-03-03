import os
import shutil

def consolidate_midi_files(source_folder, destination_folder):
    # Tạo thư mục đích nếu nó chưa tồn tại
    os.makedirs(destination_folder, exist_ok=True)
    
    # Duyệt qua tất cả các thư mục và tệp trong thư mục nguồn
    for dirpath, dirnames, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.endswith('.mid'):
                # Đường dẫn tệp nguồn
                source_file = os.path.join(dirpath, filename)
                # Đường dẫn tệp đích
                destination_file = os.path.join(destination_folder, filename)
                
                # Sao chép tệp MIDI vào thư mục đích
                if os.path.abspath(source_file) != os.path.abspath(destination_file):  # Check if files are different
                    shutil.copy2(source_file, destination_file)
                print(f'Sao chép {source_file} vào {destination_file}')

# Đường dẫn đến thư mục chứa các thư mục nhỏ
source_folder = 'c:/Users/LAPTOP24H/Downloads/nhac_beeth/data3'
# Đường dẫn đến thư mục lớn hơn nơi bạn muốn gom các tệp MIDI
destination_folder = 'c:/Users/LAPTOP24H/Downloads/nhac_beeth/data3/gom'

# Gọi hàm để thực hiện việc gom tệp
consolidate_midi_files(source_folder, destination_folder)
