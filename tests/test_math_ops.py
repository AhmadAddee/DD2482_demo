import pytest, subprocess
from pathlib import Path

program = str(Path(__file__).parents[1].absolute() / "application.bat")

def test_add_happy():
    out = subprocess.check_output([program, "math", "add", "2", "3"], text=True, shell=True)
    assert float(out) == 5

def test_add_negative():
    out = subprocess.check_output([program, "math", "add", "-2", "-3"], text=True, shell=True)
    assert float(out) == -5

def test_add_mixed_signs():
    out = subprocess.check_output([program, "math", "add", "-2", "3"], text=True, shell=True)
    assert float(out) == 1

def test_add_big_int():
    out = subprocess.check_output([program, "math", "add", "10000000000000000000000000000000000000000000", "1"], text=True, shell=True)
    assert float(out) == 1e+43

def test_add_decimals():
    out = subprocess.check_output([program, "math", "add", "2.3", "4.5"], text=True, shell=True)
    assert float(out) == 6.8

def test_add_zero():
    out = subprocess.check_output([program, "math", "add", "0", "1"], text=True, shell=True)
    assert float(out) == 1

def test_sub_happy():
    out = subprocess.check_output([program, "math", "sub", "5", "3"], text=True, shell=True)
    assert float(out) == 2

def test_sub_negative():
    out = subprocess.check_output([program, "math", "sub", "-2", "-3"], text=True, shell=True)
    assert float(out) == 1

def test_sub_mixed_signs():
    out = subprocess.check_output([program, "math", "sub", "-2", "3"], text=True, shell=True)
    assert float(out) == -5

def test_sub_big_int():
    out = subprocess.check_output([program, "math", "sub", "10000000000000000000000000000000000000000000", "1"], text=True, shell=True)
    assert float(out) == 1e+43

def test_sub_decimals():
    out = subprocess.check_output([program, "math", "sub", "2.3", "4.5"], text=True, shell=True)
    assert float(out) == -2.2

def test_sub_zero():
    out = subprocess.check_output([program, "math", "sub", "0", "1"], text=True, shell=True)
    assert float(out) == -1

def test_mul_happy():
    out = subprocess.check_output([program, "math", "mul", "5", "3"], text=True, shell=True)
    assert float(out) == 15

def test_mul_negative():
    out = subprocess.check_output([program, "math", "mul", "-2", "-3"], text=True, shell=True)
    assert float(out) == 6

def test_mul_mixed_signs():
    out = subprocess.check_output([program, "math", "mul", "-2", "3"], text=True, shell=True)
    assert float(out) == -6

def test_mul_big_int():
    out = subprocess.check_output([program, "math", "mul", "10000000000000000000000000000000000000000000", "2"], text=True, shell=True)
    assert float(out) == 2e+43

def test_mul_decimals():
    out = subprocess.check_output([program, "math", "mul", "2.3", "4.5"], text=True, shell=True)
    assert float(out) == 10.35

def test_mul_zero():
    out = subprocess.check_output([program, "math", "mul", "0", "1"], text=True, shell=True)
    assert float(out) == 0

def test_div_happy():
    out = subprocess.check_output([program, "math", "div", "8", "2"], text=True, shell=True)
    assert float(out) == 4

def test_div_negative():
    out = subprocess.check_output([program, "math", "div", "-6", "-3"], text=True, shell=True)
    assert float(out) == 2

def test_div_mixed_signs():
    out = subprocess.check_output([program, "math", "div", "-6", "3"], text=True, shell=True)
    assert float(out) == -2

def test_div_big_int():
    out = subprocess.check_output([program, "math", "div", "10000000000000000000000000000000000000000000", "2"], text=True, shell=True)
    assert float(out) == 5e+42

def test_div_decimals():
    out = subprocess.check_output([program, "math", "div", "2.3", "4.5"], text=True, shell=True)
    assert float(out) == 0.5111111111111111

def test_div_zero():
    out = subprocess.check_output([program, "math", "div", "0", "1"], text=True, shell=True)
    assert float(out) == 0

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        subprocess.check_output([program, "math", "div", "1", "0"], text=True, shell=True)

def test_mean_happy():
    out = subprocess.check_output([program, "math", "mean", [1, 2, 3, 4]], text=True, shell=True)
    assert float(out) == 2.5

@pytest.mark.slow
def test_stddev_slowish():
    # Simulate heavier computation by larger dataset
    data = list(range(1000))
    out = subprocess.check_output([program, "math", "stddev", data.__str__()], text=True, shell=True)
    #val = math_ops.stddev(data)
    assert float(out) > 0

def test_stddev_single_value():
    with pytest.raises(ValueError):
        subprocess.check_output([program, "math", "stddev", [1]], text=True, shell=True)
        #math_ops.stddev([1])
