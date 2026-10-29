from project import save_account, load_account


def sample_account():
    return {
        "createaccount": {
            "name": "TestUser",
            "pin": "1234"
        },
        "deposit": 0,
        "withdraw": 0,
        "balance": 0,
        "history": []
    }


def test_accountreset():
    account = sample_account()
    account["deposit"] = 1000
    account["withdraw"] = 500
    account["history"].append("old data")

    account["deposit"] = 0
    account["withdraw"] = 0
    account["balance"] = 0
    account["history"] = []

    assert account["deposit"] == 0
    assert account["withdraw"] == 0
    assert account["history"] == []


def test_depositamount():
    account = sample_account()
    account["deposit"] += 500
    assert account["deposit"] == 500


def test_withdrawamount():
    account = sample_account()
    account["deposit"] = 500
    account["withdraw"] += 200
    assert account["withdraw"] == 200


def test_balance_calculation():
    account = sample_account()
    account["deposit"] = 1000
    account["withdraw"] = 400
    account["balance"] = account["deposit"] - account["withdraw"]
    assert account["balance"] == 600


def test_save_loadaccount():
    account = sample_account()
    save_account(account)
    loaded = load_account()

    assert loaded["createaccount"]["name"] == "TestUser"
    assert loaded["deposit"] == 0
