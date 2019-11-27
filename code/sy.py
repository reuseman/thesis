def compute_sy(bpm_list):
  return list(map(lambda x: 63 if x >= 315 else floor(x / 5), bpm_list)) 
