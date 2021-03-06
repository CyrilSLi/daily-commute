from wave import *
def saw (num, volume):
    ls = []
    for i in range (num):
        ls.append (round (volume / (num - 1) * i))
    return ls
def triangle (num, volume):
    ls, half = [], saw (-(num // -2), volume)
    ls.extend (half)
    if num % 2:
        ls.pop (-1)
    half.reverse ()
    ls.extend (half)
    return ls
def gen_wave (form, length, volume):
    if form.lower () == "square":
        return [volume] * (length // 2) + [0] * -(length // -2)
    if length < 3:
        return [0, volume] [ : length]
    if form.lower () == "saw":
        return saw (length, volume)
    if form.lower () == "triangle":
        return triangle (length, volume)
names = ['C0', 'C#0', 'Db0', 'D0', 'D#0', 'Eb0', 'E0', 'F0', 'F#0', 'Gb0', 'G0', 'G#0', 'Ab0', 'A0', 'A#0', 'Bb0', 'B0', 'C1', 'C#1', 'Db1', 'D1', 'D#1', 'Eb1', 'E1', 'F1', 'F#1', 'Gb1', 'G1', 'G#1', 'Ab1', 'A1', 'A#1', 'Bb1', 'B1', 'C2', 'C#2', 'Db2', 'D2', 'D#2', 'Eb2', 'E2', 'F2', 'F#2', 'Gb2', 'G2', 'G#2', 'Ab2', 'A2', 'A#2', 'Bb2', 'B2', 'C3', 'C#3', 'Db3', 'D3', 'D#3', 'Eb3', 'E3', 'F3', 'F#3', 'Gb3', 'G3', 'G#3', 'Ab3', 'A3', 'A#3', 'Bb3', 'B3', 'C4', 'C#4', 'Db4', 'D4', 'D#4', 'Eb4', 'E4', 'F4', 'F#4', 'Gb4', 'G4', 'G#4', 'Ab4', 'A4', 'A#4', 'Bb4', 'B4', 'C5', 'C#5', 'Db5', 'D5', 'D#5', 'Eb5', 'E5', 'F5', 'F#5', 'Gb5', 'G5', 'G#5', 'Ab5', 'A5', 'A#5', 'Bb5', 'B5', 'C6', 'C#6', 'Db6', 'D6', 'D#6', 'Eb6', 'E6', 'F6', 'F#6', 'Gb6', 'G6', 'G#6', 'Ab6', 'A6', 'A#6', 'Bb6', 'B6', 'C7', 'C#7', 'Db7', 'D7', 'D#7', 'Eb7', 'E7', 'F7', 'F#7', 'Gb7', 'G7', 'G#7', 'Ab7', 'A7', 'A#7', 'Bb7', 'B7', 'C8', 'C#8', 'Db8', 'D8', 'D#8', 'Eb8', 'E8', 'F8', 'F#8', 'Gb8', 'G8', 'G#8', 'Ab8', 'A8', 'A#8', 'Bb8', 'B8']
freqs = [16.35, 17.32, 17.32, 18.35, 19.45, 19.45, 20.6, 21.83, 23.12, 23.12, 24.5, 25.96, 25.96, 27.5, 29.14, 29.14, 30.87, 32.7, 34.65, 34.65, 36.71, 38.89, 38.89, 41.2, 43.65, 46.25, 46.25, 49.0, 51.91, 51.91, 55.0, 58.27, 58.27, 61.74, 65.41, 69.3, 69.3, 73.42, 77.78, 77.78, 82.41, 87.31, 92.5, 92.5, 98.0, 103.83, 103.83, 110.0, 116.54, 116.54, 123.47, 130.81, 138.59, 138.59, 146.83, 155.56, 155.56, 164.81, 174.61, 185.0, 185.0, 196.0, 207.65, 207.65, 220.0, 233.08, 233.08, 246.94, 261.63, 277.18, 277.18, 293.66, 311.13, 311.13, 329.63, 349.23, 369.99, 369.99, 392.0, 415.3, 415.3, 440.0, 466.16, 466.16, 493.88, 523.25, 554.37, 554.37, 587.33, 622.25, 622.25, 659.25, 698.46, 739.99, 739.99, 783.99, 830.61, 830.61, 880.0, 932.33, 932.33, 987.77, 1046.5, 1108.73, 1108.73, 1174.66, 1244.51, 1244.51, 1318.51, 1396.91, 1479.98, 1479.98, 1567.98, 1661.22, 1661.22, 1760.0, 1864.66, 1864.66, 1975.53, 2093.0, 2217.46, 2217.46, 2349.32, 2489.02, 2489.02, 2637.02, 2793.83, 2959.96, 2959.96, 3135.96, 3322.44, 3322.44, 3520.0, 3729.31, 3729.31, 3951.07, 4186.01, 4434.92, 4434.92, 4698.63, 4978.03, 4978.03, 5274.04, 5587.65, 5919.91, 5919.91, 6271.93, 6644.88, 6644.88, 7040.0, 7458.62, 7458.62, 7902.13]
detach = [0.5, 0.25]
while True:
    print ("Input the notes:")
    samp, tempo, result, notes, frames = int (input ()), int (input ()), open ("output.wav", "w"), [], []
    while True:
        raw, note = input ().split (" "), []
        if not raw [0]:
            break
        if len (raw) == 1:
            notes.append (notes [int (raw [0]) - 1])
        else:
            note.append (float (raw [0]) * 60 / tempo)
            for i in range (1, len (raw), 4):
                if raw [i + 2] in names:
                    note.append ((int (raw [i]), raw [i + 1], freqs [names.index (raw [i + 2])], raw [i + 3]))
                else:
                    note.append ((int (raw [i]), raw [i + 1], float (raw [i + 2]), raw [i + 3]))
            notes.append (note)
    result.setparams ((1, 1, samp, round (samp * sum ([i [0] for i in notes])), "NONE", "not compressed"))
    for m in notes:
        globlen = m [0]
        for k, j in enumerate (m [1 : ]):
            volume, form, freq = j [ : 3]
            length = globlen - min (globlen * detach [0], detach [1]) if j [3] == "y" else globlen
            wave = []
            for i in range (1, int (length * freq) + 2):
                wave.extend (gen_wave (form, round (samp / freq * i - len (wave)), volume))
            wave = wave [ : round (length * samp)]
            if j [3] == "y":
                wave.extend ([0] * round ((globlen - length) * samp))
            if k == 0:
                output = wave
            else:
                output = [sum (l) // 2 for l in zip (output, wave)]
        frames.extend (output)
    result.writeframes (bytes (frames))
    result.close ()
    input (f"Done! ({result.tell ()})")
