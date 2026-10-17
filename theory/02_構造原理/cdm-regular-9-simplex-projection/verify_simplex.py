"""Numerical check of the geometric example, not a test of CDM or the source video.

Run with Python 3 and NumPy: python verify_simplex.py
Uses only local calculation. The coordinate model is independently constructed.
"""
import itertools
import json
import math

import numpy as np


def main():
    # Helmert basis: the columns are an orthonormal basis of sum(x_i) = 0.
    basis = np.zeros((10, 9))
    for j in range(9):
        divisor = math.sqrt((j + 1) * (j + 2))
        basis[: j + 1, j] = 1 / divisor
        basis[j + 1, j] = -(j + 1) / divisor
    vertices = basis / math.sqrt(2)
    pairs = list(itertools.combinations(range(10), 2))
    lengths = lambda points: np.array([np.linalg.norm(points[i] - points[j]) for i, j in pairs])
    assert len(pairs) == 45
    assert np.linalg.matrix_rank(vertices[1:] - vertices[0]) == 9
    assert np.allclose(basis.T @ basis, np.eye(9), atol=1e-12)
    assert np.allclose(vertices.mean(axis=0), 0, atol=1e-12)
    assert np.allclose(lengths(vertices), 1, atol=1e-12)
    projection = np.eye(9)[:2]
    assert np.allclose(projection @ projection.T, np.eye(2))
    samples = []
    orderings = []
    for t in [0.17, 0.53, 1.07]:
        rotation = np.eye(9)
        for j in range(2, 9):
            for k in [0, 1]:
                a = t * (j + 1) / (k + 2) + j * .13
                plane = np.eye(9)
                plane[k, k] = plane[j, j] = math.cos(a)
                plane[k, j] = -math.sin(a)
                plane[j, k] = math.sin(a)
                rotation = plane @ rotation
        assert np.allclose(rotation.T @ rotation, np.eye(9), atol=1e-12)
        assert np.isclose(np.linalg.det(rotation), 1, atol=1e-12)
        rotated = vertices @ rotation.T
        assert np.allclose(lengths(rotated), 1, atol=1e-12)
        shadow = rotated @ projection.T
        projected = lengths(shadow)
        assert projected.min() >= 0 and projected.max() <= 1 + 1e-12
        assert np.ptp(projected) > 1e-3
        orderings.append(tuple(np.argsort(projected)))
        samples.append({
            'parameter': t,
            'original_edge_min': float(lengths(rotated).min()),
            'original_edge_max': float(lengths(rotated).max()),
            'shadow_edge_min': float(projected.min()),
            'shadow_edge_max': float(projected.max()),
            'shortest_pair_1_based': [v + 1 for v in pairs[int(np.argmin(projected))]],
        })
    assert len(set(orderings)) > 1
    # A nonzero pair can cancel as vectors while its two endpoints remain distinct.
    a = np.array([1., 0.])
    assert np.allclose(a + (-a), 0) and not np.allclose(a, -a)
    print(json.dumps({
        'status': 'PASS',
        'scope': 'independent geometric example only; does not validate CDM or source-video implementation',
        'vertices': 10, 'edges': 45, 'affine_dimension': 9,
        'rotation_samples': samples,
        'shadow_distance_order_changed': True,
    }, indent=2))


if __name__ == '__main__':
    main()
