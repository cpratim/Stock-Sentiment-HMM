import numpy as np
import pandas as pd


def build_matrix(state_map):
    matrix = []
    for k in sorted(list(state_map.keys())):
        row = []
        for j in sorted(list(state_map[k].keys())):
            row.append(round(state_map[k][j], 3))
        matrix.append(row)
    return np.array(matrix)


def save_matrix(state_map, outfile):
    matrix = build_matrix(state_map)
    df = pd.DataFrame(matrix)
    df.to_csv(outfile)
