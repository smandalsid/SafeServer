import wave

def divfuncaudio(src):
    song=wave.open(src, mode='rb')
    # Read frames and convert to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))
    firsthalf=frame_bytes[:len(frame_bytes)//2]
    secondhalf=frame_bytes[len(frame_bytes)//2:]
    with wave.open(src[:-4]+"left.wav", 'wb') as fd:
        fd.setparams(song.getparams())
        fd.writeframes(firsthalf)
    song.close()
    with wave.open(src[:-4]+"right.wav", 'wb') as fd:
        fd.setparams(song.getparams())
        fd.writeframes(secondhalf)
    song.close()