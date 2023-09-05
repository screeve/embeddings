import pytest

from embedding.model import Word2VecModel
from embedding.tokenizer import Tokenizer, WhitespaceTokenizer, BasicTokenizer, NumSubTokenizer, Word2VecTokenizer


@pytest.fixture
def whitespace_tokenizer() -> Tokenizer:
    return WhitespaceTokenizer()


@pytest.fixture
def basic_tokenizer() -> Tokenizer:
    return BasicTokenizer()


@pytest.fixture
def basic_tokenizer_with_number_replacement() -> Tokenizer:
    return NumSubTokenizer()


@pytest.fixture
def word2vec_tokenizer() -> Tokenizer:
    return Word2VecTokenizer()

@pytest.fixture
def word2vec() -> Word2VecModel:
    return Word2VecModel()
