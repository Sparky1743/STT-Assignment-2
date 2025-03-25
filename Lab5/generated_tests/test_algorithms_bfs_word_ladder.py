# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import algorithms.bfs.word_ladder as module_0


def test_case_0():
    str_0 = "lFq5#M6/:j%"
    bytes_0 = b"t[\xdc\x1dB)\x1cP1\xd8\xf5"
    dict_0 = {str_0: str_0, str_0: str_0, bytes_0: str_0}
    var_0 = module_0.ladder_length(str_0, bytes_0, dict_0)
    assert var_0 == -1
    var_1 = module_0.ladder_length(str_0, dict_0, dict_0)
    assert var_1 == -1


def test_case_1():
    dict_0 = {}
    var_0 = module_0.ladder_length(dict_0, dict_0, dict_0)
    assert var_0 == 0


def test_case_2():
    str_0 = "lFq5#M6/:j%"
    bytes_0 = b"t[\xdc\x1dB)\x1cP1\xd8\xf5"
    var_0 = module_0.ladder_length(str_0, bytes_0, str_0)
    assert var_0 == -1


def test_case_3():
    complex_0 = 4764.9 - 2332.35942j
    dict_0 = {complex_0: complex_0, complex_0: complex_0}
    tuple_0 = (dict_0,)
    var_0 = module_0.ladder_length(tuple_0, dict_0, complex_0)
    assert var_0 == 1
