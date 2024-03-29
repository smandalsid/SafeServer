# Use wave package (native to Python) for reading the received audio file
import wave

def Decode(src):
    # song = wave.open("audio/song_embedded.wav", mode='rb')
    # file=input("Enter name of embedded audio file: ")
    song = wave.open(src, mode='rb')
    print("Decoding...")
    # Convert audio to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    # Extract the LSB of each byte
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    # Convert byte array back to string
    string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
    # Cut off at the filler characters
    decoded = string.split("###")[0]

    # Print the extracted text
    print("Sucessfully decoded: "+decoded)
    song.close()
    return decoded