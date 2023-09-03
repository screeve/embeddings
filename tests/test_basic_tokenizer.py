from embedding.tokenizer import Tokenizer


def test_whitespace_tokenizer(whitespace_tokenizer: Tokenizer) -> None:
    assert len(whitespace_tokenizer.tokenize('გიორგი მიდის   სახლში')) == 3
    assert whitespace_tokenizer.tokenize('გიორგი   მიდის სახლში') == ['გიორგი', 'მიდის', 'სახლში']
    assert len(whitespace_tokenizer.tokenize('გიორგი მიდის სახლში.')) == 3
    assert whitespace_tokenizer.tokenize('გიორგი მიდის სახლში.') == ['გიორგი', 'მიდის', 'სახლში.']
    assert len(whitespace_tokenizer.tokenize('გიორგი, მიდი სახლში.')) == 3
    assert whitespace_tokenizer.tokenize('გიორგი, მიდი სახლში.') == ['გიორგი,', 'მიდი', 'სახლში.']


def test_basic_tokenizer(basic_tokenizer: Tokenizer) -> None:
    assert len(basic_tokenizer.tokenize('გიორგი მიდის   სახლში')) == 3
    assert basic_tokenizer.tokenize('გიორგი   მიდის სახლში') == ['გიორგი', 'მიდის', 'სახლში']
    assert len(basic_tokenizer.tokenize('გიორგი მიდის სახლში.')) == 4
    assert basic_tokenizer.tokenize('გიორგი მიდის სახლში.') == ['გიორგი', 'მიდის', 'სახლში', '.']
    assert len(basic_tokenizer.tokenize('გიორგი, მიდი სახლში.')) == 5
    assert basic_tokenizer.tokenize('გიორგი, მიდი სახლში.') == ['გიორგი', ',', 'მიდი', 'სახლში', '.']
    assert basic_tokenizer.tokenize('გიორგი, მიდი სახლ-კარში.') == ['გიორგი', ',', 'მიდი', 'სახლ-კარში', '.']
    assert basic_tokenizer.tokenize('გიორგი ცხოვრობდა მე-15 საუკუნეში?!') == ['გიორგი', 'ცხოვრობდა', 'მე-15',
                                                                              'საუკუნეში', '?!']


def test_basic_tokenizer_with_number_substitution(basic_tokenizer_with_number_replacement: Tokenizer) -> None:
    assert basic_tokenizer_with_number_replacement.tokenize('გიორგი '
                                                            'ცხოვრობდა '
                                                            'მე-15 '
                                                            'საუკუნეში?!') == ['გიორგი', 'ცხოვრობდა', 'მე-<NUM>',
                                                                               'საუკუნეში', '?!']
    assert basic_tokenizer_with_number_replacement.tokenize('მე '
                                                            'მაქვს '
                                                            '35 '
                                                            'ვაშლი.') == ['მე', 'მაქვს', '<NUM>',
                                                                          'ვაშლი', '.']
