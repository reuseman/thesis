 def compute_unimol_entropy(bpm_list):
    # Stable BPMs are labeled as 1
    for i in range(0, len(bpm_list)):
        if bpm_list[i] <= 50:
            bpm_list[i] = 0
        elif bpm_list[i] >= 120:
            bpm_list[i] = 2
        else:
            bpm_list[i] = 1

    unimol_entropy = list()

    # Count the number of 1s in a window of 10 elements
    for i in range(9, len(bpm_list)):
        start_index = i - 9
        end_index = i
        entropy = bpm_list[start_index : end_index + 1].count(1)
        unimol_entropy.append(entropy)

    return unimol_entropy
