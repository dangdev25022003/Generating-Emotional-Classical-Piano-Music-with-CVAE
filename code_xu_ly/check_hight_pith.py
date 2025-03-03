import os
import muspy

def analyze_midi_pitch_range(midi_file):
    try:
        music = muspy.read_midi(midi_file)
        pitches = []
        for track in music.tracks:
            for note in track.notes:
                pitches.append(note.pitch)
        if pitches:
            return min(pitches), max(pitches)
        else:
            return None, None
    except Exception as e:
        print(f"Error processing {midi_file}: {str(e)}")
        return None, None

def analyze_folder(folder_path):
    global_min_pitch = 127
    global_max_pitch = 0
    files_processed = 0
    files_with_notes = 0

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.mid', '.midi')):
            input_path = os.path.join(folder_path, filename)
            min_pitch, max_pitch = analyze_midi_pitch_range(input_path)
            
            if min_pitch is not None and max_pitch is not None:
                global_min_pitch = min(global_min_pitch, min_pitch)
                global_max_pitch = max(global_max_pitch, max_pitch)
                files_with_notes += 1
            
            files_processed += 1
            
            if files_processed % 100 == 0:
                print(f"Processed {files_processed} files...")

    return global_min_pitch, global_max_pitch, files_processed, files_with_notes

# Usage
midi_folder = 'c:/Users/LAPTOP24H/Downloads/merged_midis2_transposed_major_train'  # Replace with your MIDI folder path

min_pitch, max_pitch, total_files, files_with_notes = analyze_folder(midi_folder)

print(f"Analysis complete. Processed {total_files} files.")
print(f"Files containing notes: {files_with_notes}")
print(f"Lowest pitch found: {min_pitch}")
print(f"Highest pitch found: {max_pitch}")
print(f"Recommended pitch range for piano roll: {min_pitch} to {max_pitch}")
