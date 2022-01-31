from wave import *
from random import randint
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
            notes.append ([float (raw [0]) * 60 / tempo] + [raw [1]] + [int (i) for i in raw [2 : ]])
    result.setparams ((1, 1, samp, round (samp * sum ([i [0] for i in notes])), "NONE", "not compressed"))
    for m in notes:
        length, direction, volume, change, repeat = m
        for i in range (repeat):
            if direction == "down":
                frames.extend ([randint (0, max (0, volume - i // change)) for i in range (round (samp * length / repeat))])
            if direction == "up":
                frames.extend ([randint (0, 0 if i // change > volume else volume) for i in range (round (samp * length / repeat))])
    result.writeframes (bytes (frames))
    result.close ()
    input (f"Done! ({result.tell ()})")
