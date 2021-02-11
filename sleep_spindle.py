import numpy as np

def sleep_spindle_match(sampling_freq):
    freq = 13 #Hz

    x = np.arange(0,1,1.0/sampling_freq)
    y = np.sin(2 * np.pi * freq * x + (np.pi/2)) * np.cos(np.pi * x + (np.pi/2))

    spindle = {'x':x, 'y':y}

    print(spindle)

    return spindle