import wave as w
while True:
    with w.open (input ("Source: ") + ".wav") as s:
        params = s.getparams ()
        frames = list (s.readframes (params [3]))
    with w.open (input ("Result: ") + ".wav", "wb") as r: 
        r.setparams (params)
        var, interval, speed, repeat = int (input ("Variation: ")), int (input ("Interval: ")), input ("Change speed (Y/y): ") in ["y", "Y"], int (input ("Repeat #: "))
        slow = [j for j in frames for i in range (var)]
        fast = frames [ : : var]
        frames = [] 
        for i in range (len (fast) // interval):
            frames.extend (slow [i * interval * (var - 1) : (i + 1) * interval * (var - 1)])
            frames.extend (fast [i * interval : (i + 1) * interval])
        frames.extend (slow [(i + 1) * interval * (var - 1) : (i + 1) * interval * (var - 1) + (params [3] - s.getnframes ())])
        r.writeframes (bytes (frames [ : : (var - 1) * speed + 1] * repeat))
    input (f"Done! ({str (s.tell ())}, {str (r.tell () // repeat)})")
