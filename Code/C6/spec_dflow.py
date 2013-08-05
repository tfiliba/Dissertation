# add the ADC
adc_bw = bandwidth*input_bitwidth
self.blocks['ADC'] = CBlock(CBlock.getADCModel(self.platforms, bandwidth, input_bitwidth),-1,0,0,'PFB',0,adc_bw,antennas)
self.totalblocks += antennas

# add the PFB
self.blocks['PFB'] = CBlock(CBlock.getPFBModel(self.platforms, input_bitwidth, numchannels),'ADC',0,adc_bw,'FFT',0,adc_bw,antennas)
self.totalblocks += antennas

# add the FFT
fft_out_bandwidth = bandwidth* fft_out_bitwidth
self.blocks['FFT'] = CBlock(CBlock.getFFTModel(self.platforms, numchannels),'PFB',0,adc_bw,'VAcc',0,fft_out_bandwidth,antennas)
self.totalblocks += antennas

#add the Vacc
self.blocks['VAcc'] = CBlock(CBlock.getVAccModel(self.platforms, fft_out_bitwidth, accumulation_length),'FFT',0,fft_out_bandwidth,-1,0,0,antennas)
self.totalblocks += antennas