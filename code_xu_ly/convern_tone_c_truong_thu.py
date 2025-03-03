# import mido

# def transpose_to_c_major(mid):
#     transposition = -12  # Transpose to C major
    
#     # Create a new MIDI file for the transposed version
#     new_mid = mido.MidiFile()

#     for track in mid.tracks:
#         new_track = mido.MidiTrack()
#         for msg in track:
#             if msg.type == 'note_on' or msg.type == 'note_off':
#                 # Transpose note
#                 new_note = msg.note + transposition
#                 # Ensure note is within MIDI range
#                 if new_note < 0:
#                     new_note = 0
#                 elif new_note > 127:
#                     new_note = 127
#                 new_msg = msg.copy(note=new_note)  # Copy the message with the new note
#                 new_track.append(new_msg)
#             else:
#                 new_track.append(msg)  # Copy non-note messages directly
#         new_mid.tracks.append(new_track)

#     return new_mid

# def transpose_to_c_minor(mid):
#     transposition = -12  # Transpose to C minor
    
#     # Create a new MIDI file for the transposed version
#     new_mid = mido.MidiFile()

#     for track in mid.tracks:
#         new_track = mido.MidiTrack()
#         for msg in track:
#             if msg.type == 'note_on' or msg.type == 'note_off':
#                 # Transpose note
#                 new_note = msg.note + transposition
#                 # Ensure note is within MIDI range
#                 if new_note < 0:
#                     new_note = 0
#                 elif new_note > 127:
#                     new_note = 127
#                 new_msg = msg.copy(note=new_note)  # Copy the message with the new note
#                 new_track.append(new_msg)
#             else:
#                 new_track.append(msg)  # Copy non-note messages directly
#         new_mid.tracks.append(new_track)

#     return new_mid

# # Function to save the transposed MIDI file
# def save_transposed_midi(mid, output_file_path):
#     mid.save(output_file_path)
#     print(f"Saved transposed MIDI to {output_file_path}")

# # Example usage
# input_file_path = 'c:/Users/LAPTOP24H/Downloads/merged_midis2/e1/waldstein_3_clip_13.mid'  # Replace with your MIDI file path
# output_file_path_major = 'c:/Users/LAPTOP24H/Downloads/merged_midis2/e1/waldstein_3_clip_13_major.mid'  # Output for C major
# output_file_path_minor = 'c:/Users/LAPTOP24H/Downloads/merged_midis2/e1/waldstein_3_clip_13_minor.mid'  # Output for C minor

# # Load MIDI file
# mid = mido.MidiFile(input_file_path)

# # Transpose and save to C major
# mid_major = transpose_to_c_major(mid)  # No need to copy now
# save_transposed_midi(mid_major, output_file_path_major)

# # Transpose and save to C minor
# mid_minor = transpose_to_c_minor(mid)  # No need to copy now
# save_transposed_midi(mid_minor, output_file_path_minor)

# print("Transposition complete.")


#part 2

import os
import mido

def transpose_to_c_major(mid):
    transposition = -12  # Transpose to C major
    new_mid = mido.MidiFile()

    for track in mid.tracks:
        new_track = mido.MidiTrack()
        for msg in track:
            if msg.type == 'note_on' or msg.type == 'note_off':
                new_note = msg.note + transposition
                new_note = max(0, min(new_note, 127))  # Ensure note is within MIDI range
                new_msg = msg.copy(note=new_note)  # Copy the message with the new note
                new_track.append(new_msg)
            else:
                new_track.append(msg)  # Copy non-note messages directly
        new_mid.tracks.append(new_track)

    return new_mid

def transpose_to_c_minor(mid):
    transposition = -12  # Transpose to C minor
    new_mid = mido.MidiFile()

    for track in mid.tracks:
        new_track = mido.MidiTrack()
        for msg in track:
            if msg.type == 'note_on' or msg.type == 'note_off':
                new_note = msg.note + transposition
                new_note = max(0, min(new_note, 127))  # Ensure note is within MIDI range
                new_msg = msg.copy(note=new_note)  # Copy the message with the new note
                new_track.append(new_msg)
            else:
                new_track.append(msg)  # Copy non-note messages directly
        new_mid.tracks.append(new_track)

    return new_mid

def save_transposed_midi(mid, output_file_path):
    mid.save(output_file_path)
    print(f"Saved transposed MIDI to {output_file_path}")

def process_folder(input_folder_path, output_folder_path_major, output_folder_path_minor):
    """Process all MIDI files in the input folder and save transpositions to the output folders."""
    if not os.path.exists(output_folder_path_major):
        os.makedirs(output_folder_path_major)
    
    if not os.path.exists(output_folder_path_minor):
        os.makedirs(output_folder_path_minor)

    for root, dirs, files in os.walk(input_folder_path):
        for filename in files:
            if filename.lower().endswith('.mid'):
                input_file_path = os.path.join(root, filename)

                # Load MIDI file
                mid = mido.MidiFile(input_file_path)

                # Transpose and save to C major
                mid_major = transpose_to_c_major(mid)
                relative_path = os.path.relpath(root, input_folder_path)  # Get the relative path
                output_file_path_major = os.path.join(output_folder_path_major, relative_path, f"{os.path.splitext(filename)[0]}_major.mid")
                os.makedirs(os.path.dirname(output_file_path_major), exist_ok=True)  # Create output directory if it doesn't exist
                save_transposed_midi(mid_major, output_file_path_major)

                # Transpose and save to C minor
                mid_minor = transpose_to_c_minor(mid)
                output_file_path_minor = os.path.join(output_folder_path_minor, relative_path, f"{os.path.splitext(filename)[0]}_minor.mid")
                os.makedirs(os.path.dirname(output_file_path_minor), exist_ok=True)  # Create output directory if it doesn't exist
                save_transposed_midi(mid_minor, output_file_path_minor)

    print("Transposition complete.")

# Example usage
input_folder_path = 'c:/Users/LAPTOP24H/Downloads/nhac beeth/gian du_4_4_clip'  # Change this to your input folder path
output_folder_path_major = 'c:/Users/LAPTOP24H/Downloads/nhac beeth/gian du_4_4_clip_major'  # Output folder for C major
output_folder_path_minor = 'c:/Users/LAPTOP24H/Downloads/nhac beeth/gian du_4_4_clip_minor'  # Output folder for C minor

process_folder(input_folder_path, output_folder_path_major, output_folder_path_minor)
