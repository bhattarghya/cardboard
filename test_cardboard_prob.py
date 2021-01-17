from cardboard_prob import cardboard


def test_cardboard():
    assert cardboard([(1,5,10),(4,6,8),(10,15,10),(11,12,8)])==[(1,10),(5,8),(6,0),(10,10),(15,0)]
    assert cardboard([(1,10,4),(1,8,6),(1,6,8)])==[(1,8),(6,6),(8,4),(10,0)]
    assert cardboard([(0,6,2),(5,10,8),(7,8,12)])==[(0,2),(5,8),(7,12),(8,8),(10,0)]
    assert cardboard([]) is None
