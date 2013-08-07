antennas = 16
channels = 128
bandwidth = 0.4 #defined in GHz

#create the instrument
myfxcorrelator = FXCorrelator(antennas, channels, bandwidth)
myfxcorrelator.runILP()