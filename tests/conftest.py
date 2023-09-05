import pytest
from embedding.tokenizer import Tokenizer, WhitespaceTokenizer, BasicTokenizer, NumSubTokenizer


@pytest.fixture
def whitespace_tokenizer() -> Tokenizer:
    return WhitespaceTokenizer()


@pytest.fixture
def basic_tokenizer() -> Tokenizer:
    return BasicTokenizer()


@pytest.fixture
def basic_tokenizer_with_number_replacement() -> Tokenizer:
    return NumSubTokenizer()

