import pyaudio
import wave
import numpy as np
from scipy.fft import fft
import scipy.signal
from ctypes import *
import getch
import scipy
import scipy.fftpack
from matplotlib import pyplot as plt
import scipy.io.wavfile as wavfile
import scipy
import getch

#importing from the scripts.......
from Upsampling import upsample as u
from Quantization import quantization as q
from filter import show_filter as s


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 32000  # "RATE" is the number of samples collected per second.

CHUNK = 512  #"CHUNK" is the  number of frames the (signals are split 
RECORD_SECONDS = 5

WAVE_OUTPUT_FILENAME = "file.wav"
 
audio = pyaudio.PyAudio()

print("Please press space to Record your sound")


char = None
#print(char)
while(char != ord(' ')):
    
    char = getch.getch()
    char = ord(char)
 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print ("recording...")
frames = []
 
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)



# stop Recording
print ("finished recording \n\n\n\n\n")
stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

fs, x = wavfile.read("file.wav")

char = None
while(char != ord(' ')):
    print("***************************************************    Welcome to the Audio Processing Segment      *****************************************************\n\n For UPSAMPLING: Press u \n\n For Showing FILTERED Response: Press s \n\n For QUANTIZATION/DE-QUANTIZATION: Press q \n\n Press space to quit")
    while((char != ord('u')) and (char != ord('q'))and (char != ord(' '))and (char != ord('s'))): 
        char = getch.getch()
        char = ord(char)

    if char == ord('u'):
        n= u.upsample(fs,x)
        char= None

    if char == ord('q'):    
        q.quantization(fs,x)
        char= None

    if char == ord('s'):    
        s.show_filter(fs,x,n)
        char= None
    

