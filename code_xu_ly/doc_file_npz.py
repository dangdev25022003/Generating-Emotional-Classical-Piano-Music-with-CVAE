import numpy as np

# Đọc tệp .npz
file_path = 'c:/Users/LAPTOP24H/Downloads/all_midi_notes_251.npz'
data = np.load(file_path)

# Danh sách các mảng bên trong tệp
print("Các mảng có trong tệp .npz:", data.files)

# Truy cập một mảng cụ thể
for array_name in data.files:
    array_data = data[array_name]
    print(f"Dữ liệu trong mảng '{array_name}':")
    print(array_data.shape)
