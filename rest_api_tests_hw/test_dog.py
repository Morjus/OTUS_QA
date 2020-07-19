import pytest


def test_get_random_dog(api_client_for_dog):
    res = api_client_for_dog.get("breeds/image/random")
    res_json = res.json()
    assert res_json["status"] == "success"


@pytest.mark.parametrize("breed", [
    "afghan",
    "basset",
    "blood",
    "english",
    "ibizan",
    "plott",
    "walker"
])
def test_get_sub_breads(api_client_for_dog, breed):
    res = api_client_for_dog.get("breed/hound/list")
    res_json = res.json()
    assert breed in res_json["message"]


@pytest.mark.parametrize("file", ['.jpg', '.jpeg', '.JPG', '.txt'])
def test_get_breed_images(api_client_for_dog, file):
    res = api_client_for_dog.get("breed/hound/images")
    res_json = res.json()
    result = '\n'.join(res_json["message"])
    assert file in result


@pytest.mark.parametrize("breed", [
    "african",
    "boxer",
    "entlebucher",
    "elkhound",
    "shiba",
    "whippet",
    "spaniel"
])
def test_get_random_breed_images(api_client_for_dog, breed):
    res = api_client_for_dog.get(f"breed/{breed}/images/")
    res_json = res.json()
    assert res_json["status"] == "success"


@pytest.mark.parametrize("number_of_images", [i for i in range(1, 10)])
def test_get_few_sub_breed_random_images(api_client_for_dog, number_of_images):
    res = api_client_for_dog.get(f"breed/hound/afghan/images/random/{number_of_images}")
    res_json = res.json()
    assert len(res_json["message"]) == number_of_images
