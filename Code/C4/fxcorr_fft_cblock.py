performance_model = CBlock.getADCModel(self.platforms, bandwidth, input_bitwidth)
data_source = 'PFB'
source_connection = 0 #0 indicates a one-to-one connection
source_bandwidth = 0.4*8
data_sink = 'XEng'
sink_connection_type = 1 #0 indicates an all-to-all connection
sink_bandwidth = 0.4*8
antennas = 16
self.blocks['FFT'] = CBlock(performance_model,data_source,source_connection,source_bandwidth,\
    data_sink,sink_connection_type,fft_out_bandwidth,antennas)
