from embedding.model import Word2VecModel
import numpy as np

from embedding.tokenizer import Tokenizer


def test_out_of_vocabulary_word2vec(word2vec: Word2VecModel) -> None:
    vec = word2vec("NOT IN A DICTIONARY")
    assert all(vec == np.zeros(vec.shape))


def test_sentence_word2vec(word2vec: Word2VecModel, word2vec_tokenizer: Tokenizer) -> None:
    sentence = "მე მივდივარ სახლში"
    assert all([all(word2vec(word) != np.zeros(word2vec(word).shape)) for word in word2vec_tokenizer.tokenize(sentence)])
    sentence = "მე მაქვს 5 ვაშლი"
    assert all(
        [all(word2vec(word) != np.zeros(word2vec(word).shape)) for word in word2vec_tokenizer.tokenize(sentence)])

