# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.arrays.rotate as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    set_0 = set()
    bytes_0 = b"\xd6\xddG\x94\xafp\x8e,\xa3]"
    tuple_0 = (bool_0, bytes_0, set_0, bytes_0)
    tuple_1 = (bytes_0, tuple_0, bool_0)
    module_0.rotate_v1(tuple_1, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -1594
    list_0 = [int_0, int_0]
    var_0 = module_0.rotate_v2(list_0, int_0)
    module_0.rotate_v2(int_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    var_0 = module_0.rotate_v3(none_type_0, none_type_0)
    str_0 = "':+jj$\rIlOz%"
    module_0.rotate_v2(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    module_0.rotate_v3(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x96\xdf\x1c\xa6<\x06\xe4\x89\x06\xcai"
    bool_0 = False
    set_0 = set()
    bytes_1 = b"\xd6\xddG\x94\xafp\x8e,\xa3]"
    tuple_0 = (bool_0, bytes_0, set_0, bytes_1)
    tuple_1 = (bytes_0, tuple_0, bool_0)
    var_0 = module_0.rotate_v1(tuple_1, bool_0)
    module_0.rotate_v1(bytes_1, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = -1594
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.rotate_v2(list_0, int_0)
    var_1 = module_0.rotate_v1(var_0, int_0)
    object_0 = module_1.object()
    module_0.rotate_v3(object_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    int_0 = 3963
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.rotate_v2(list_0, int_0)
    var_1 = module_0.rotate_v1(var_0, int_0)
    module_0.rotate_v1(var_0, var_0)
