import wave

def concatfuncaudio(src1, src2):
    combined=[]
    a1=wave.open(src1, "rb")
    combined.append([a1.getparams(), a1.readframes(a1.getnframes())])
    a2=wave.open(src2, "rb")
    combined.append([a2.getparams(), a2.readframes(a2.getnframes())])

    output=wave.open("media/joined.wav", "wb")
    output.setparams(combined[0][0])

    for i in range(len(combined)):
        output.writeframes(combined[i][1])
    output.close()