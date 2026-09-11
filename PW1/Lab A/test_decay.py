import decay

def test_simulate():
    res = decay.simulate(1000, 0.4, 5)
    assert len(res) == 5
    assert res[0] == 1000
