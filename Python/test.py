import numpy as np
from processing_audio import performProcessing

def test_lpf_constant_signal():
    data = np.ones(10)
    result = performProcessing(data, window_size=3, lpFilter=True)
    assert all(abs(x - 1.0) < 1e-6 for x in result), "LPF failed on constant signal"

def test_hpf_constant_signal():
    data = np.ones(10)
    result = performProcessing(data, window_size=3, lpFilter=False)
    assert all(abs(x) < 1e-6 for x in result), "HPF should zero constant input"

def test_lpf_impulse_signal():
    data = np.zeros(10)
    data[0] = 1
    result = performProcessing(data, window_size=3, lpFilter=True)
    assert result[0] == 1
    assert all(x <= 1.0 and x >= 0.0 for x in result), "LPF on impulse should decay"

def test_hpf_impulse_signal():
    data = np.zeros(10)
    data[0] = 1
    result = performProcessing(data, window_size=3, lpFilter=False)
    assert result[0] > 0
    assert any(abs(x) > 1e-3 for x in result), "HPF on impulse should not be all zero"

def test_invalid_window_size():
    data = np.random.rand(10)
    result = performProcessing(data, window_size=0, lpFilter=True)
    assert isinstance(result, list), "Should return a list"
    # Depending on your implementation, this should probably raise or return unchanged
