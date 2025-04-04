# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import algorithms.dp.job_scheduling as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1792
    module_0.binary_search(int_0, int_0)


def test_case_1():
    int_0 = -1144
    var_0 = module_0.binary_search(int_0, int_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
    module_0.schedule(list_0)


def test_case_3():
    bytes_0 = b"\xef~\xc0\xb1[\xb6:c"
    job_0 = module_0.Job(bytes_0, bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"K\xf1/\xf0+4\x8a\x90\xc2\xf0\xc9\x99b\xf5\xaf\xa8kk\xcfa"
    module_0.schedule(bytes_0)


def test_case_5():
    bytes_0 = b"\xddF\x98e~\xbf8\x02+"
    job_0 = module_0.Job(bytes_0, bytes_0, bytes_0)
    set_0 = {job_0}
    var_0 = module_0.schedule(set_0)
    assert var_0 == b"\xddF\x98e~\xbf8\x02+"


def test_case_6():
    bool_0 = False
    job_0 = module_0.Job(bool_0, bool_0, bool_0)
    job_1 = module_0.Job(job_0, bool_0, bool_0)
    dict_0 = {job_1: job_0, job_1: job_1, job_0: job_0}
    var_0 = module_0.schedule(dict_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_7():
    bool_0 = False
    bool_1 = True
    job_0 = module_0.Job(bool_0, bool_1, bool_0)
    none_type_0 = None
    job_1 = module_0.Job(job_0, bool_0, none_type_0)
    dict_0 = {job_1: job_0, job_1: job_1, job_0: job_0}
    module_0.schedule(dict_0)


def test_case_8():
    bool_0 = True
    bool_1 = False
    job_0 = module_0.Job(bool_1, bool_0, bool_0)
    job_1 = module_0.Job(job_0, bool_0, bool_0)
    dict_0 = {job_1: job_0, job_1: job_1, job_0: job_0}
    var_0 = module_0.schedule(dict_0)
    assert var_0 is True
    bytes_0 = b"M\xc6\xef\xb7\xb9A\xb8L\xefB\tO$A"
    job_2 = module_0.Job(job_1, bytes_0, bytes_0)
    int_0 = -851
    var_1 = module_0.binary_search(int_0, int_0)
    assert var_1 == -1
    bool_2 = False
    job_3 = module_0.Job(var_1, int_0, bool_2)
    assert job_3.start == -1
    job_4 = module_0.Job(var_0, var_0, bool_0)
    assert job_4.start is True
    assert job_4.finish is True
