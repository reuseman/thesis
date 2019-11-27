 def compute_bpm(qrs_ann_list, frequency=250):
  bpm_list = list()

  for i in range(0, len(qrs_ann_list) - 1):
    dist = qrs_ann_list[i + 1] - qrs_ann_list[i]
    bpm = 60 / (dist / frequency)
    bpm_list.append(bpm)

  return bpm_list
