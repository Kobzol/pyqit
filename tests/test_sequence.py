
from testutils import init
init()

import haydi as hd # noqa
import itertools  # noqa


def test_sequence_iterate():
    s = hd.Sequence(hd.Range(3), 2)
    result = list(s)
    expected = list(itertools.product(range(3), range(3)))
    assert set(result) == set(expected)
    assert len(result) == len(expected)
    s.size == len(expected)


def test_sequence_iterate_empty():
    assert list(hd.Sequence(hd.Range(3), 0)) == [()]


def test_sequence_generate():
    s = hd.Sequence(hd.Range(3), 5)
    result = list(s.generate(200))
    assert len(result)
    for r in result:
        assert len(r) == 5
        for x in r:
            assert 0 <= x < 3


def test_sequence_iter_set():
    r2 = hd.Range(4)
    p = hd.Sequence(r2, 3)

    a = list(p)
    b = []
    for i in xrange(p.size + 10):
        it = iter(p)
        it.set_step(i)
        l = list(it)
        if l:
            b.append(l[0])
    assert a == b


def test_sequence_iter_copy():
    r2 = hd.Range(3)
    s = hd.Sequence(r2, 4)

    it = iter(s)
    it2 = it.copy()

    assert list(it) == list(it2)


def test_sequence_name():
    s = hd.Sequence(hd.Range(10), 2, "TestSequence")
    assert s.name == "TestSequence"
