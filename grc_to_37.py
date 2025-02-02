""" A Python version of the bash script grc_to_37.sh
    Usage,
    
        python.exe grc_to_37.py grc_file_name_to_convert.grc

    Freeware by: Steven C. Hageman July 6, 2024
    
    Based on the GNU Radio grc_to_37.sh LINUX script.
    
    Written in Python 3.12
"""
import sys
import os


# Conversion Keys
list_of_block_changes = [
    "gr_peak_detector2_fb/blocks_peak_detector2_fb",
    "gr_short_to_float/blocks_short_to_float",
    "gr_diff_phasor_cc/digital_diff_phasor_cc",
    "blks2_logpwrfft_x/logpwrfft_x",
    "gr_rms_xx/blocks_rms_xx",
    "gr_probe_density_b/digital_probe_density_b",
    "gr_mute_xx/blocks_mute_xx",
    "gr_agc_xx/analog_agc_xx",
    "gr_ctcss_squelch_ff/analog_ctcss_squelch_ff",
    "gr_diff_encoder_bb/digital_diff_encoder_bb",
    "gr_pll_refout_cc/analog_pll_refout_cc",
    "gr_uchar_to_float/blocks_uchar_to_float",
    "gr_interp_fir_filter_xxx/interp_fir_filter_xxx",
    "gr_udp_sink/blocks_udp_sink",
    "gr_and_xx/blocks_and_xx",
    "gr_keep_one_in_n/blocks_keep_one_in_n",
    "gr_vector_sink_x/blocks_vector_sink_x",
    "gr_freq_xlating_fir_filter_xxx/freq_xlating_fir_filter_xxx",
    "gr_float_to_int/blocks_float_to_int",
    "gr_file_source/blocks_file_source",
    "gr_float_to_short/blocks_float_to_short",
    "gr_fft_vxx/fft_vxx",
    "gr_quadrature_demod_cf/analog_quadrature_demod_cf",
    "gr_file_sink/blocks_file_sink",
    "gr_pfb_clock_sync_xxx/digital_pfb_clock_sync_xxx",
    "gr_multiply_const_vxx/blocks_multiply_const_vxx",
    "gr_peak_detector_xb/blocks_peak_detector_xb",
    "gr_noise_source_x/analog_noise_source_x",
    "gr_simple_framer/digital_simple_framer",
    "gr_delay/blocks_delay",
    "gr_pfb_synthesizer_ccf/pfb_synthesizer_ccf",
    "gr_short_to_char/blocks_short_to_char",
    "gr_chunks_to_symbols_xx/digital_chunks_to_symbols_xx",
    "gr_interleaved_short_to_complex/blocks_interleaved_short_to_complex",
    "gr_frequency_modulator_fc/analog_frequency_modulator_fc",
    "gr_xor_xx/blocks_xor_xx",
    "gr_dpll_bb/analog_dpll_bb",
    "gr_threshold_ff/blocks_threshold_ff",
    "gr_nop/blocks_nop",
    "gr_unpack_k_bits_bb/blocks_unpack_k_bits_bb",
    "gr_max_xx/blocks_max_xx",
    "gr_int_to_float/blocks_int_to_float",
    "gr_stream_to_streams/blocks_stream_to_streams",
    "blks2_wfm_rcv/analog_wfm_rcv",
    "gr_fractional_interpolator_xx/fractional_interpolator_xx",
    "gr_conjugate_cc/blocks_conjugate_cc",
    "blks2_fm_demod_cf/analog_fm_demod_cf",
    "gr_fir_filter_xxx/fir_filter_xxx",
    "gr_null_source/blocks_null_source",
    "gr_complex_to_arg/blocks_complex_to_arg",
    "gr_pwr_squelch_xx/analog_pwr_squelch_xx",
    "gr_descrambler_bb/digital_descrambler_bb",
    "gr_copy/blocks_copy",
    "gr_complex_to_mag/blocks_complex_to_mag",
    "gr_throttle/blocks_throttle",
    "gr_additive_scrambler_bb/digital_additive_scrambler_bb",
    "gr_wavfile_sink/blocks_wavfile_sink",
    "gr_vector_source_x/blocks_vector_source_x",
    "gr_moving_average_xx/blocks_moving_average_xx",
    "gr_char_to_short/blocks_char_to_short",
    "blks2_fm_deemph/analog_fm_deemph",
    "gr_pll_freqdet_cf/analog_pll_freqdet_cf",
    "gr_or_xx/blocks_or_xx",
    "blks2_fm_preemph/analog_fm_preemph",
    "blks2_wfm_tx/analog_wfm_tx",
    "gr_stream_to_vector/blocks_stream_to_vector",
    "gr_glfsr_source_x/digital_glfsr_source_x",
    "gr_map_bb/digital_map_bb",
    "gr_sig_source_x/analog_sig_source_x",
    "gr_transcendental/blocks_transcendental",
    "gr_skiphead/blocks_skiphead",
    "gr_hilbert_fc/hilbert_fc",
    "blks2_nbfm_rx/analog_nbfm_rx",
    "random_source_x/analog_random_source_x",
    "gr_complex_to_real/blocks_complex_to_real",
    "gr_null_sink/blocks_null_sink",
    "gr_float_to_complex/blocks_float_to_complex",
    "gr_multiply_xx/blocks_multiply_xx",
    "gr_simple_correlator/digital_simple_correlator",
    "gr_sample_and_hold_xx/blocks_sample_and_hold_xx",
    "blks2_pfb_channelizer_ccf/pfb_channelizer_ccf",
    "gr_goertzel_fc/goertzel_fc",
    "gr_complex_to_mag_squared/blocks_complex_to_mag_squared",
    "gr_packed_to_unpacked_xx/blocks_packed_to_unpacked_xx",
    "blks2_standard_squelch/analog_standard_squelch",
    "blks2_am_demod_cf/analog_am_demod_cf",
    "gr_and_const_xx/blocks_and_const_xx",
    "gr_unpacked_to_packed_xx/blocks_unpacked_to_packed_xx",
    "gr_probe_avg_mag_sqrd_x/analog_probe_avg_mag_sqrd_x",
    "gr_channel_model/channels_channel_model",
    "gr_divide_xx/blocks_divide_xx",
    "gr_simple_squelch_cc/analog_simple_squelch_cc",
    "gr_message_source/blocks_message_source",
    "gr_sub_xx/blocks_sub_xx",
    "gr_stream_mux/blocks_stream_mux",
    "gr_burst_tagger/blocks_burst_tagger",
    "gr_float_to_uchar/blocks_float_to_uchar",
    "gr_scrambler_bb/digital_scrambler_bb",
    "gr_streams_to_vector/blocks_streams_to_vector",
    "gr_add_xx/blocks_add_xx",
    "gr_feedforward_agc_cc/analog_feedforward_agc_cc",
    "gr_iir_filter_ffd/iir_filter_ffd",
    "blks2_stream_to_vector_decimator/blocks_stream_to_vector_decimator",
    "gr_pn_correlator_cc/digital_pn_correlator_cc",
    "gr_streams_to_stream/blocks_streams_to_stream",
    "gr_rational_resampler_base_xxx/rational_resampler_base_xxx",
    "gr_vector_to_streams/blocks_vector_to_streams",
    "gr_interleave/blocks_interleave",
    "gr_add_const_vxx/blocks_add_const_vxx",
    "gr_message_sink/blocks_message_sink",
    "gr_complex_to_imag/blocks_complex_to_imag",
    "gr_vco_f/blocks_vco_f",
    "gr_deinterleave/blocks_deinterleave",
    "gr_argmax_xx/blocks_argmax_xx",
    "gr_not_xx/blocks_not_xx",
    "gr_udp_source/blocks_udp_source",
    "gr_nlog10_ff/blocks_nlog10_ff",
    "gr_diff_decoder_bb/digital_diff_decoder_bb",
    "gr_phase_modulator_fc/analog_phase_modulator_fc",
    "gr_complex_to_interleaved_short/blocks_complex_to_interleaved_short",
    "gr_float_to_char/blocks_float_to_char",
    "gr_head/blocks_head",
    "gr_fft_filter_xxx/fft_filter_xxx",
    "gr_cpfsk_bc/analog_cpfsk_bc",
    "gr_vector_to_stream/blocks_vector_to_stream",
    "gr_agc2_xx/analog_agc2_xx",
    "gr_pll_carriertracking_cc/analog_pll_carriertracking_cc",
    "gr_repeat/blocks_repeat",
    "gr_filter_delay_fc/filter_delay_fc",
    "blks2_rational_resampler_xxx/rational_resampler_xxx",
    "gr_char_to_float/blocks_char_to_float",
    "gr_integrate_xx/blocks_integrate_xx",
    "gr_wavfile_source/blocks_wavfile_source",
    "gr_complex_to_float/blocks_complex_to_float",
    "gr_single_pole_iir_filter_xx/single_pole_iir_filter_xx",
    "blks2_nbfm_tx/analog_nbfm_tx",
    "blks2_wfm_rcv_pll/analog_wfm_rcv_pll",
    "const_source_x/analog_const_source_x",
    "blks2_pfb_arb_resampler_ccf/pfb_arb_resampler_xxx"
]

# Get the file name from the command line
filename = sys.argv[-1]

if not filename.endswith('.grc'):
    print('This script only works on ".grc" files.')
    sys.exit(-1)

# Read in the file
with open(filename, 'r') as file:
    filedata = file.read()

# Check to see if this file needs updating
if not "gr_" in filedata:
    print('Your .grc file does not need updating.')
    sys.exit(-1)

# Check for WX GUI Controls
if "wx." in filedata:
    print('FYI: Your .grc file contains WX GUI Controls.\nThey are not included with recent GNU Radio Companion Versions.')

# Replace the target string(s)
for block_change_data in list_of_block_changes:
    old, new = block_change_data.split('/')
    filedata = filedata.replace(old, new)

# Make a backup of the file
cmd_str = 'copy ' + filename + ' ' + filename + '.bak'
try:
    os.popen(cmd_str)
except:
    print('Could not make a backup file.')
    sys.exit(-1)

# Write the file out again
with open(filename, 'w') as file:
    file.write(filedata)

sys.exit(0)
