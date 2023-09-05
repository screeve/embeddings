import os
import numpy as np
from gensim.models import KeyedVectors

VECTOR_PATH = os.path.join(os.path.dirname(__file__), 'data', 'word2vec.wordvectors')
VECTOR_SIZE = 300


class Word2VecModel:
    def __init__(self) -> None:
        self._vector = KeyedVectors.load(VECTOR_PATH)

    def __call__(self, word: str) -> np.ndarray:
        try:
            return self._vector[word]
        except KeyError:
            return np.zeros(VECTOR_SIZE)
