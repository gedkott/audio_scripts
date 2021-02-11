import numpy as np
 
import wave
 
import struct
 
import matplotlib.pyplot as plt

num_samples = 48000
 
# The sampling rate of the analog to digital convert
 
sampling_rate = 48000.0
 
amplitude = 16000
 
file = "test.wav"

nframes=num_samples
 
comptype="NONE"
 
compname="not compressed"
 
nchannels=1
 
sampwidth=2

from sleep_spindle import sleep_spindle_match

x = sleep_spindle_match(44100)
plt.plot(x['x'], x['y'])
plt.savefig('sleepspindle.png')

wav_file=wave.open(file, 'w')
 
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))

for s in x['y']:
   wav_file.writeframes(struct.pack('h', int(s*amplitude)))