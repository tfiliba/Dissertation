# 800MHz spectrometer
numchannels = 1024
accumulation_length  = 10
bandwidth = 0.8 #defined in GHz
input_bitwidth = 8
fft_out_bitwidth = 4
    
#create the instrument
myspectrometer = Spectrometer(numchannels, accumulation_length, bandwidth, input_bitwidth, fft_out_bitwidth)
