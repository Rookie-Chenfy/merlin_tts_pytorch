import numpy as np
import os


def get_file_list(labels_dir, wave_dir, train_scale, valid_scale, shuffle_lst=True):

    label_ids = [label_id.replace(".lab", "") for label_id in os.listdir(labels_dir)]
    wav_ids = [wav_id.replace(".wav", "") for wav_id in os.listdir(wave_dir)]

    res1 = list(set(wav_ids).difference(set(label_ids)))
    res2 = list(set(label_ids).difference(set(wav_ids)))

    if res1:
        raise Exception("{0} is in wavs but not in labels".format(res1))
    if res2:
        raise Exception("{0} is in labels but not in wavs".format(res2))

    np.random.seed(1234)

    if shuffle_lst:
        np.random.shuffle(label_ids)
    else:
        label_ids = sorted(label_ids)

    train = int(len(label_ids)*train_scale)
    valid = int(len(label_ids)*valid_scale)
    train_ids = label_ids[0:train]
    valid_ids = label_ids[train:train+valid]

    return train_ids, valid_ids
