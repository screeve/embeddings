import re
from dataclasses import dataclass, field
from typing import Protocol, List, Dict

from src.embedding.constants import DASH, PUNCTUATIONS


class Tokenizer(Protocol):
    def tokenize(self, text: str) -> List[str]:
        pass


@dataclass
class RegexTokenizer:
    _pattern: str  # pattern for tokens
    _flags: re.RegexFlag = field(default=re.UNICODE | re.MULTILINE | re.DOTALL)
    _special_tokens: Dict[re.Pattern, str] = field(default_factory=dict)
    _regex: re.Pattern = field(init=False)

    def __post_init__(self) -> None:
        self._regex = re.compile(self._pattern, flags=self._flags)

    def __modify_tokens(self, tokens: List[str]) -> List[str]:
        modified_tokens = tokens.copy()
        for idx in range(len(modified_tokens)):
            for pattern, token in self._special_tokens.items():
                modified_tokens[idx] = pattern.sub(token, modified_tokens[idx])
        return modified_tokens

    def add_special_token(self, pattern: re.Pattern | str, token: str) -> None:
        if isinstance(pattern, str):
            pattern = re.compile(pattern)
        self._special_tokens[pattern] = token

    def tokenize(self, text: str) -> List[str]:
        return self.__modify_tokens(self._regex.findall(text))


class WhitespaceTokenizer(RegexTokenizer):
    def __init__(self) -> None:
        RegexTokenizer.__init__(self, r'\S+')


class BasicTokenizer(RegexTokenizer):
    def __init__(self) -> None:
        RegexTokenizer.__init__(self, f'\\w+(?:{DASH}\\w+)*|[{PUNCTUATIONS}]+')


class NumSubTokenizer(BasicTokenizer):
    def __init__(self) -> None:
        BasicTokenizer.__init__(self)
        self.add_special_token(r'\d+', '<NUM>')


class Word2VecTokenizer(NumSubTokenizer):
    pass
