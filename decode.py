import wave


class AutismDecoder:
    def __init__(self, audio_file: str) -> None:
        self.audio_file = audio_file

    def decode_autism(self) -> None:
        print("Activating Autism Decode...")
        with wave.open(self.audio_file, mode='rb') as audio:
            frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
            extracted = self._extract_bits(frame_bytes)
            string = self._convert_to_string(extracted)
            msg = self._extract_message(string)
            print("Autism Decode Activated!!!!!")
            print("The message is: " + msg)

    def _extract_bits(self, frame_bytes: bytearray) -> list[int]:
        extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
        return extracted

    def _convert_to_string(self, extracted: list[int]) -> str:
        string = "".join(chr(int(
            "".join(map(str, extracted[i:i + 8])), 2)) for i in range(0, len(extracted), 8))
        return string

    def _extract_message(self, string: str) -> str:
        msg = string.split("###")[0]
        return msg


if __name__ == "__main__":
    audio_file = input("Autism audio file: ")

    autism_decoder = AutismDecoder(audio_file)
    autism_decoder.decode_autism()
