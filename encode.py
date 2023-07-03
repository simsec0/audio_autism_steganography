import wave

autism_audio_file = input("audiofile: ")
string = input("secretmsg: ")
output = input("outputfile: ")

def autism_is_power(autism_audio_file, string, output):
      print ("Autism Activating...")
      autism_audio = wave.open(autism_audio_file, mode='rb')
      autism_frame_bytes = bytearray(list(autism_audio.readframes(autism_audio.getnframes())))
      string = string + int((len(autism_frame_bytes)-(len(string)*8*8))/8) *'#'
      bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
      for i, bit in enumerate(bits):
        autism_frame_bytes[i] = (autism_frame_bytes[i] & 254) | bit
      frame_modified = bytes(autism_frame_bytes)
      with wave.open(output, 'wb') as fd:
        fd.setparams(autism_audio.getparams())
        fd.writeframes(frame_modified)
      autism_audio.close()
      print ("Autism Activated!!")
      
autism_is_power(autism_audio_file, string, output)