import wave
import struct
import math
import os

# --- CAMBIO CLAVE: Ruta relativa para salir de 'utils' y buscar 'assets' en la raíz ---
base_path = os.path.dirname(os.path.abspath(__file__))
assets_path = os.path.join(base_path, "..", "assets")

if not os.path.exists(assets_path):
    os.makedirs(assets_path)

def create_sound(filename, freq, duration):
    filepath = os.path.join(assets_path, filename)
    sample_rate = 44100
    amplitude = 16000
    wav_file = wave.open(filepath, 'w')
    wav_file.setparams((1, 2, sample_rate, 0, 'NONE', 'not compressed'))
    for i in range(int(sample_rate * duration)):
        value = int(amplitude * math.sin(2 * math.pi * freq * i / sample_rate))
        data = struct.pack('<h', value)
        wav_file.writeframesraw(data)
    wav_file.close()

create_sound("correct.wav", 1000, 0.2)
create_sound("wrong.wav", 300, 0.3)

print(f"✔️ Sonidos generados en: {assets_path}")