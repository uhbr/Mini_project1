import numpy as np

import matplotlib.pyplot as plt


x = np.arange(0,1,0.01) #Creating a numpy arange that has a step of 0.01
sin_signal = np.sin(2*np.pi*5*x) #a numpy sinusoidal signal of 5Hz sampled every 0.01 sec.


def sampling_sinus(sin_signal):
    '''A function that samples a sinus wave while preserving all max and min points, for a sinus wave (not nessecerily 5Hz and 0.01 sample step)'''
    maxima = [] #empty list of max points
    minima = [] #empty list of min points
    
    # now let's append the empty list by comparing each point in the sinus to the previous and the next one.
    for i in range(1, len(sin_signal) -1):
        if sin_signal[i - 1] < sin_signal[i] and sin_signal[i + 1] < sin_signal[i]: #(only) if the current point is bigger then the previous and the next, then:
            maxima.append(i) #we'll append the max list with the new point.
        elif sin_signal[i - 1] > sin_signal[i] and sin_signal[i + 1] > sin_signal[i]: #(only) if the current point is smaller then the previous and next, then:
            minima.append(i) #we'll append the min list with the new point.

    # after having all the max and min points, we should make a list of all the points:
    all_points = sorted(maxima + minima)
    
    # now, we need to create a new array with all the points.
    sampled_signal = np.array([sin_signal[i] for i in all_points])

    return all_points, sampled_signal


all_points, sampled_signal = sampling_sinus(sin_signal)

plt.plot(x, sin_signal, label="Original Sinusoidal Signal", zorder=1)
plt.scatter(x, sin_signal,color="green", label="Original sine sampling",zorder=2)
plt.scatter(x[all_points], sampled_signal, color='red', marker='^', label="Sampled Points",zorder=4)
plt.plot(x[all_points], sampled_signal, color='pink',linestyle='--', zorder=3)
plt.title("Original and downsampled sinusoidal signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.show()

