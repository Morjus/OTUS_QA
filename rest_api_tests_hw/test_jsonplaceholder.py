import pytest

@pytest.mark.parametrize('userId', [0, 'a'])
def test_get_empty(api_jsonplaceholder, userId):
    res = api_jsonplaceholder.get(
        path="/posts",
        params={'userId': userId}
    )
    print(res.json())
    assert res.json() == []


@pytest.mark.parametrize('userId, exp_id', [(1, 1), (3, 3)])
def test_get_posts_filter(api_jsonplaceholder, userId, exp_id):
    res = api_jsonplaceholder.get(
        path="/posts",
        params={'userId': userId}
    )
    all_posts_len = len(res.json())
    for post in range(all_posts_len):
        assert res.json()[post]["userId"] == exp_id


@pytest.mark.parametrize('postId, exp_id', [(1, 1),(1, 2),(1, 3),(1, 4),(1, 5)])
def test_get_comments(api_jsonplaceholder, postId, exp_id):
    res = api_jsonplaceholder.get(
        path="/comments",
        params={'postId': postId}
    )
    all_posts_len = len(res.json())
    assert res.json()[exp_id-1]["id"] == exp_id


@pytest.mark.parametrize("input_id, output_id", [(123456, "123456"), (-1, "-1"), (0, "0")])
@pytest.mark.parametrize("input_body, output_body", [("IT IS BODY", "IT IS BODY"), (0, "0"), (" ", " ")])
@pytest.mark.parametrize("input_title, output_title",
                         [("IT IS TITLE", "IT IS TITLE"), (10000, "10000"), ("$&^@", "$&^@")])
def test_post_posts(api_jsonplaceholder, input_id, output_id, input_body, output_body, input_title, output_title):
    res = api_jsonplaceholder.post(
        path="/posts",
        data={"title": input_title,
              "body": input_body,
              "userId": input_id}
    )
    assert res.json()["title"] == output_title
    assert res.json()["body"] == output_body
    assert res.json()["userId"] == output_id


@pytest.mark.parametrize("input_id",[i for i in range(1,11)])
def test_users(api_jsonplaceholder,input_id):
    res = api_jsonplaceholder.get(
        path="/users",
        params={"id": input_id}
    )
    assert res.json()[0]["username"] != ""