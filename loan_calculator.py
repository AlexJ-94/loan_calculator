import json


def main():
    names = json.loads(open('loan_information.json').read())
    for name in names:
        print(name)


main()
