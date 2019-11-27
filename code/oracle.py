def compute_oracle(patient_af_events, annot_qrs, record_len=9205760):
  binary_af_samples = [0] * record_len
  for af_records in patient_af_events:
    binary_af_samples[af_records[0] : af_records[1] + 1] = map(
      lambda x: 1, binary_af_samples[af_records[0] : af_records[1] + 1]
    )
     
  binary_af_qrs = list()
  start_value = annot_qrs.sample[0]
    for i in range(1, len(annot_qrs.sample)):
      end_value = annot_qrs.sample[i] + 1
      
      ones = binary_af_samples[start_value:end_value].count(1)
      interval_length = end_value - start_value
      percentage_of_ones = ones / interval_length
      # Method A
      element = 1 if percentage_of_ones > 0.5 else 0
      binary_af_qrs.append(element)
      start_value = end_value + 1
      
    return binary_af_qrs
