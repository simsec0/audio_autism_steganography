import wave

autism_audiofile = input("autism audio file please: ")

def autism_function(autism_audiofile):
    print ("Activating Autism Decode...")
    autism_audio = wave.open(autism_audiofile, mode='rb')
    autism_frame_bytes = bytearray(list(autism_audio.readframes(autism_audio.getnframes())))
    extracted = [autism_frame_bytes[i] & 1 for i in range(len(autism_frame_bytes))]
    string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
    msg = string.split("###")[0]
    print("Autism Decode Activated!!!!!")
    print("The message is: "+msg)
    autism_audio.close()

autism_function(autism_audiofile)
