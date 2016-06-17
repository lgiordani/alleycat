from alleycat import helpers as h


def test_insert_multiple_values_in_dictionary():
    adict = {}
    h.insert_multiple_values(adict, 'akey', 'avalue')
    assert adict == {'akey': {'avalue'}}


def test_extract_n_random_couples_from_a_list():
    # Testing random functions is pointless
    # but this test is here to show the usage of
    # get_random_couples and its outputs
    couples = h.get_random_couples(100, ['A', 'B', 'C', 'D'])

    for couple in couples:
        assert couple[0] != couple[1]
