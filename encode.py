import wave


class AutismActivator:
    def __init__(self, audio_file: str, secret_msg: str, output_file: str) -> None:
        self.audio_file = audio_file
        self.secret_msg = secret_msg
        self.output_file = output_file

    def activate_autism(self) -> None:
        print("Autism Activating...")
        with wave.open(self.audio_file, mode='rb') as audio:
            frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
            secret_msg = self._prepare_secret_msg(frame_bytes)
            bits = self._get_bits(secret_msg)
            self._modify_frame_bytes(frame_bytes, bits)
            self._write_modified_audio(frame_bytes, audio)

        print("Autism Activated!!")

    def _prepare_secret_msg(self, frame_bytes: bytearray) -> str:
        secret_msg = self.secret_msg + \
            int((len(frame_bytes) - (len(self.secret_msg) * 8 * 8)) / 8) * '#'
        return secret_msg

    def _get_bits(self, secret_msg: str) -> list[int]:
        bits = list(map(int, ''.join([bin(ord(char)).lstrip(
            '0b').rjust(8, '0') for char in secret_msg])))
        return bits

    def _modify_frame_bytes(self, frame_bytes: bytearray, bits: list[int]) -> None:
        for i, bit in enumerate(bits):
            frame_bytes[i] = (frame_bytes[i] & 254) | bit

    def _write_modified_audio(self, frame_bytes: bytearray, audio: wave.Wave_read) -> None:
        with wave.open(self.output_file, 'wb') as output:
            output.setparams(audio.getparams())
            output.writeframes(bytes(frame_bytes))


if __name__ == "__main__":
    audio_file = input("Audio file: ")
    secret_msg = input("Secret message: ")
    output_file = input("Output file: ")

    autism_activator = AutismActivator(audio_file, secret_msg, output_file)
    autism_activator.activate_autism()
