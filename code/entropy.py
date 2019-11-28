def get_pimap(n, cons):
  pi = lambda i: int(-cons / log(n, 2) * i * log(i, 2))
  return [pi(p / n) for p in range(1, n + 1)]

pi_map = get_pimap(127, 1000000)
 
def compute_entropy(wv_list):
  nu = list([0] * 127)
  sh2 = list()
  for i in range(0, len(wv_list)):
    nu.pop(0)
    nu.append(wv_list[i])
    # Number of occurrences of an element are counted
    a = dict()
    for j in nu:
      a[j] = (a[j] + 1) if j in a else 1

    k = len(a)
    sh1 = sum([pi_map[a[element] - 1] for element in a])
    sh2.append(k / 127000000 * sh1)
  
  return sh2
