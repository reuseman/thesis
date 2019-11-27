def compute_wv(sy_list):
  wv_list = list()

  for i in range(2, len(sy_list)):
    wv = (sy_list[i - 2] << 12) + (sy_list[i - 1] << 6) + sy_list[i]
    wv_list.append(wv)

  return wv_list
