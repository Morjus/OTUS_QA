import pytest


@pytest.mark.parametrize("in_city, out_city",
                         [("san_diego", "San Diego"), ("tucson", "Tucson"), ("mountain_home", "Mountain Home")])
def test_by_city(api_brewery, in_city, out_city):
    res = api_brewery.get(
        path="/breweries",
        params={"by_city": in_city}
    )
    for brewery in res.json():
        assert brewery["city"] == out_city


def test_by_name(api_brewery):
    res = api_brewery.get(
        path="/breweries",
        params={"by_name": "yellowhammer_brewery"}
    )
    assert res.json()[0]["name"] == "Yellowhammer Brewery"


@pytest.mark.parametrize("in_state, out_state",
                         [("ohio", "Ohio"), ("arizona", "Arizona"), ("kentucky", "Kentucky")])
def test_by_state(api_brewery, in_state, out_state):
    res = api_brewery.get(
        path="/breweries",
        params={"by_state": in_state}
    )
    assert res.json()[0]["state"] == out_state


@pytest.mark.parametrize("in_type",
                         ["micro", "regional", "brewpub", "large", "planning", "bar", "contract", "proprietor"])
def test_by_type(api_brewery, in_type):
    res = api_brewery.get(
        path="/breweries",
        params={"by_type": in_type}
    )
    for brewery in res.json():
        assert brewery["brewery_type"] == in_type


@pytest.mark.parametrize("per_page", [i for i in range(1, 51)])
def test_per_page(api_brewery, per_page):
    res = api_brewery.get(
        path="/breweries",
        params={"per_page": per_page}
    )
    assert len(res.json()) == per_page
