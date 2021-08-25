from scipy.fft import fft 
import scipy.signal
from ctypes import *
import struct
import numpy as np
import getch
import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack
import numpy as np
from matplotlib import pyplot as plt
import wave
import pyaudio
from playsound import playsound
import sounddevice as sd
import soundfile as sf


class quantization(object):
    def quantization(fs_rate, signal):
        print(fs_rate)
        fs_original, original = wavfile.read("file.wav")


    #start block-wise signal processing:

    #Quantization, for a signal between -32000 to +32000:
#         q=int((2**15-(-2**15))/(2**N))

#         if quant_type=='Mid-Tread':
#                     #Mid Tread quantization:
#                     indices=np.round(signal/q)
#                     #de-quantization:
#                     quant_tread_rec=indices*q
#         else:
#                     #Mid -Rise quantizer:
#                     indices=np.floor(signal/q)
#                     #de-quantization:
#                     quant_rise_rec=(indices*q+q/2).astype(int)
        N = input("Enter your Bit depth: ")
        N = int(N)
        stepsize=int((2**16-(-2**16))/(2**N))
#Encode
        quant_rise_ind=np.floor(signal/stepsize)
        quant_tread_ind=np.round(signal/stepsize)
#Decode
        quant_rise_rec=quant_rise_ind*stepsize+stepsize/2
        quant_tread_rec=quant_tread_ind*stepsize
        

            #end signal processing
        #signal=np.clip(signal, -2**15,2**15)
        #signal=signal.astype(int)

        FFT_q = abs(scipy.fft.fft(quant_rise_rec))#q
        freqs_q = scipy.fftpack.fftfreq(quant_rise_rec.size)#q

        FFT = abs(scipy.fft.fft(original))#original
        freqs = scipy.fftpack.fftfreq(original.size)#original


        # plt.subplot(411)
        # p1 = plt.plot(quant_rise_rec, "g") # plotting the signal
        # plt.ylabel('Amplitude')
        # plt.subplot(412)
        # p2 = plt.plot(freqs_q, FFT_q, "r") # plotting the complete fft spectrum
        # plt.xlabel('Normalised Frequency response of Original Signal (Hz)')
        # plt.ylabel('Count dbl-sided')
        # plt.subplot(413)
        # p3 = plt.plot(original, "g") # plotting the signal
        # plt.ylabel('Amplitude')
        # plt.subplot(414)
        # p4 = plt.plot(freqs, FFT, "r") # plotting the complete fft spectrum
        # plt.xlabel('Normalised Frequency response of Original Signal (Hz)')
        # plt.ylabel('Count dbl-sided')
        # plt.show()


        plt.plot(original, "b" , label="Original Signal")
        plt.plot(quant_rise_rec, "r",label="Quantised Signal")
        plt.legend(loc="upper left")
        plt.show()




        # wavfile.write("quant.wav",fs_rate,quant_rise_rec)
        # playsound("quant.wav")
        