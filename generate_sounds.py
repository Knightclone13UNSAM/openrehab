import wave
import struct
import math
import os

# Crear carpeta assets si no existe
if not os.path.exists("assets"):
    os.makedirs("assets")

def create_sound(filename, freq, duration):
    sample_rate = 44100
    amplitude = 16000

    wav_file = wave.open(filename, 'w')
    wav_file.setparams((1, 2, sample_rate, 0, 'NONE', 'not compressed'))

    for i in range(int(sample_rate * duration)):
        value = int(amplitude * math.sin(2 * math.pi * freq * i / sample_rate))
        data = struct.pack('<h', value)
        wav_file.writeframesraw(data)

    wav_file.close()

# ✔️ Sonido correcto (agudo, corto)
create_sound("assets/correct.wav", 1000, 0.2)

# ❌ Sonido incorrecto (grave, un poco más largo)
create_sound("assets/wrong.wav", 300, 0.3)

print("Sonidos generados correctamente en /assets")