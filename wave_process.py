import wave
import numpy as np
import matplotlib
matplotlib.use('svg')
import matplotlib.pyplot as plt
import math
from scipy import nanmean

# Created input file with:
# mpg123  -w 20130509talk.wav 20130509talk.mp3
wr = wave.open('riversandroads.wav', 'r')
par = list(wr.getparams()) # Get the parameters from the input.
# This file is stereo, 2 bytes/sample, 44.1 kHz.
par[3] = 0 # The number of samples will be set by writeframes.

# Open the output file
#ww = wave.open('riversandroads-filtered.wav', 'w')
#ww.setparams(tuple(par)) # Use the same parameters as the input file.

lowpass = 21 # Remove lower frequencies.
highpass = 9000 # Remove higher frequencies.

sz = wr.getframerate() # Read and process 1 second at a time.
c = int(wr.getnframes()/sz) # whole file
trackl = [];
trackr = [];
for num in range(c):
	print('Processing {}/{} s'.format(num+1, c))
	da = np.fromstring(wr.readframes(sz), dtype=np.int16)
	left, right = da[0::2], da[1::2] # left and right channel
	#lf, rf = np.fft.rfft(left), np.fft.rfft(right)
	#lf[:lowpass], rf[:lowpass] = 0, 0 # low pass filter
	#lf[55:66], rf[55:66] = 0, 0 # line noise
	#lf[highpass:], rf[highpass:] = 0,0 # high pass filter
	#nl, nr = np.fft.irfft(lf), np.fft.irfft(rf)
	#ns = np.column_stack((nl,nr)).ravel().astype(np.int16)
	#ww.writeframes(ns.tostring())
	R = 100;
	pad_size = math.ceil(float(left.size)/R)*R - left.size;
	arr_l_padded = np.append(left, np.zeros(pad_size)*np.NaN);
	l = nanmean(arr_l_padded.reshape(-1,R), axis=1);
	arr_r_padded = np.append(right, np.zeros(pad_size)*np.NaN);
	r = nanmean(arr_r_padded.reshape(-1,R), axis=1);
	trackl.extend(l)
	trackr.extend(r)
sections = 10
sect_size = (np.size(trackl)-1)/sections
for section in range(0,sections):
	frames = section * sect_size + np.arange(sect_size)
	l = trackl[np.min(frames):np.max(frames)+1]
	r = trackr[np.min(frames):np.max(frames)+1]
	avg = np.divide(np.add(l,r),2.0);
	fig = plt.figure(num=section+1,figsize=(16, 1.8), dpi=300)
	a = plt.axes([0, 0, 1, 1])
	plt.plot(frames,avg,'k-')
	plt.axis('off')
	maximum = np.max([np.max(trackl),np.max(trackr)]);
	plt.ylim(-maximum,maximum);
	plt.xlim(np.min(frames),np.max(frames));
	plt.savefig('line_%d.svg' % (section+1))
# Close the files.
wr.close()
#ww.close()