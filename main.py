import requests


def api_data():
    response = requests.get("")
    code = response.status_code
    return code


def grapher():
    pass


def cli_interface():
    data = api_data()
    print(data)


if __name__ == '__main__':
    cli_interface()
