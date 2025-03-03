import os
import mido

def is_4_4_time_signature(mid):
    """Check if the MIDI file is in 4/4 time signature."""
    for track in mid.tracks:
        for msg in track:
            if msg.type == 'time_signature':
                return msg.numerator == 4 and msg.denominator == 4
    return False  # Default to False if no time signature is found

def equalize_note_duration(mid, target_bpm):
    """Equalize the note duration based on the target BPM."""
    original_tempo = 750000  # Default tempo (120 BPM)

    # Find the original tempo
    for track in mid.tracks:
        for msg in track:
            if msg.type == 'set_tempo':
                original_tempo = msg.tempo
                break
        if original_tempo != 750000:
            break

    # Calculate the tempo scaling factor
    tempo_scale = mido.bpm2tempo(target_bpm) / original_tempo

    new_mid = mido.MidiFile()
    new_mid.ticks_per_beat = mid.ticks_per_beat

    for track in mid.tracks:
        new_track = mido.MidiTrack()
        for msg in track:
            new_msg = msg.copy()
            if msg.type in ['note_on', 'note_off']:
                new_msg.time = int(msg.time * tempo_scale)
            new_track.append(new_msg)
        new_mid.tracks.append(new_track)

    return new_mid

def adjust_midi_tempo(input_file, output_file, target_bpm):
    """Adjust the tempo of the MIDI file if it is in 4/4 time signature."""
    mid = mido.MidiFile(input_file)
    
    if not is_4_4_time_signature(mid):
        print(f"Skipping {input_file}: Not in 4/4 time signature")
        return False

    # Equalize note duration based on target BPM
    new_mid = equalize_note_duration(mid, target_bpm)

    # Save the adjusted MIDI
    new_mid.save(output_file)
    return True

def process_folder(folder_path, target_bpm):
    """Process750000 all MIDI files in the specified folder."""
    # Create output folder for 4/4 MIDI files
    output_folder = os.path.join(folder_path, 'c:/Users/LAPTOP24H/Downloads/nhac beeth/thu gian_4_4')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.mid') or filename.lower().endswith('.midi'):
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, f"adjusted_{filename}")
            
            try:
                if adjust_midi_tempo(input_path, output_path, target_bpm):
                    print(f"Processed {filename}: Adjusted tempo and kept the entire track")
                else:
                    print(f"Skipped {filename}: Not in 4/4 time signature")
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

# Usage
folder_path = 'c:/Users/LAPTOP24H/Downloads/nhac beeth/thu gian'  # Change this to your folder path
target_bpm = 120

process_folder(folder_path, target_bpm)
