import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("butenkosergii")
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    assert r["total_count"] == 58
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] != 0

# Мої тести GitHub

@pytest.mark.emoji
def test_emojis_in_list(github_api):
    r = github_api.get_list_of_emojis()
    assert r["100"]== "https://github.githubassets.com/images/icons/emoji/unicode/1f4af.png?v8"
       

@pytest.mark.emoji
def test_len_emoji_list(github_api):
    r = github_api.get_list_of_emojis()
    assert len(r) == 1935


@pytest.mark.commits
def test_commiter_info(github_api):
    r = github_api.get_list_commits("MariiaKursa", "KursaFirstRepos")
    assert {"email": "mariiaperun97@gmail.com"}
    assert {"name": "Mariia Kursa"}


@pytest.mark.commits
def test_commiter_info_with_wrong_data(github_api):
    r = github_api.get_list_commits("mariku", "wrong_data")
    assert r["message"] == "Not Found"
