from tennis.code import run_function


def test_run_function():
    ret_val = run_function("running")
    assert ret_val == "running"
