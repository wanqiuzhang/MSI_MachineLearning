import numpy as np
from numpy import ndarray


def make_image(rows : list, nrows : int, ncols : int, grid2row : dict) -> ndarray: # very inefficient implementation but doesnt matter
    """Makes a 2d image from row indices in raw data."""
    img = np.zeros((nrows, ncols))
    for r in range(nrows):
        for c in range(ncols):
            try:
                row = grid2row[(r, c)]
                img[r, c] = rows[row]
            except:
                pass
    return img

def make_image_real(rows : list, nrows : int, ncols : int, real_rows_xy : list) -> ndarray:
    """Makes a 2d image from real rows with data (i.e., rows in real_rows)."""
    img = np.zeros((nrows, ncols))
    for idx, val in enumerate(rows):
        x, y = real_rows_xy[idx]
        img[x, y] = val
    return img