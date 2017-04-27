from growth import *

def test_growth():
    assert growth(3, 2) == 4.5
    assert growth(4, 2) == 8.0

def test_collector_returns_tuple():
    assert type(collector(((2,3), (4,7), (7,9)))) == tuple

def test_collector_returns_summed_values():
    results = collector(((2,3), (4,7), (7,9)))
    assert results[0] == 2**2/float(3) + 4**2/float(7) + 7**2/float(9)
    assert results[1] == 2+4+7

def test_calculate():
    average_growth(((2,3),(3,4)))

def test_with_some_nans():
    results = collector(((float('nan'), float('nan')), (4,7), (7,9)))
    assert results[0] == 0 + 4**2/float(7) + 7**2/float(9)

def test_with_all_nans():
    results = average_growth(((float('nan'), float('nan')), (float('nan'), float('nan'))))
    assert results == 0

def test_with_all_zeros():
    results = average_growth(((0,0), (0,0)))
    assert results == 0

def test_with_infinite_growth():
    # we assume origin is .1...
    results = average_growth(((5,0), (0,0)))
    assert results == math.log((5**2/.1)/5)

def test_with_infinite_gdp():
    results = average_growth(((float('inf'), 0), (0,0)))
    assert results == 0
