from testutils import init
init()

import qit

def test_join_range_iterate():
    d1 = qit.Range(3)
    d2 = qit.Range(0)
    d3 = qit.Range(0)
    d4 = qit.Range(5)

    expected = list(range(3)) + list(range(5))
    j = d1 + d2 + d3 + d4
    result = list(j)
    assert expected == result

def test_join_empty_iterate():
    d2 = qit.Range(0)
    d3 = qit.Range(0)

    j = d2 + d3
    result = list(j)
    assert [] == result

def test_join_int_generate():
    r1 = qit.Range(2)
    r2 = qit.Range(2, 4)
    j = r1 + r2

    result = list(j.generate().take(1000))
    assert set(result) == set(range(4))

def test_join_int_generate2():
    r1 = qit.Values([5000])
    r2 = qit.Range(1000)
    r3 = qit.Values([5001, 5002])

    j = r1 + r2 + r3

    result = list(j.generate().take(3000))
    assert result.count(5000) < 100
    assert result.count(5001) < 100
    assert result.count(5002) < 100

def test_join_int_generate3():
    r1 = qit.Range(2)
    r2 = qit.Range(2, 4)
    r3 = qit.Range(4, 6)

    j = qit.Join((r1, r2, r3), ratios=(1, 0, 1))

    result = list(j.generate().take(1000))
    assert set(result) == set((0, 1, 4, 5))