#!/usr/bin/python3
import argparse
import json
import os


def parse_file(name: str):
    """
    Input file parser
    :param name: source file path / name
    :type name: str
    :return: generator with phrases to add to intent
    :rtype: generator of str
    """
    with open(name, 'r', encoding='utf-8') as fl:
        return (x.strip() for x in fl.readlines())


def form_json(data: iter, target):
    """
    Appends new pharses to basic intent structure
    :param data: iterable with phrases
    :type data: iterable
    :param target: result filename with extension
    :type target: str
    :return: None
    :rtype: None
    """
    base = BaseStruct(target.replace('.json', ''))
    for x in data:
        base.add_case(UserInput(x))

    with open(target, 'w') as resfl:
        json.dump(base.intent, resfl)
        resfl.close()


class BaseStruct:
    def __init__(self, name):
        self.intent = {
            "id": "",
            "name": name,
            "auto": True,
            "contexts": [],
            "responses": [
                {
                    "resetContexts": False,
                    "affectedContexts": [],
                    "parameters": [],
                    "messages": [
                        {
                            "type": 0,
                            "speech": "Lorem ipsum"
                        }
                    ],
                    "defaultResponsePlatforms": {},
                    "speech": []
                }
            ],
            "priority": 500000,
            "cortanaCommand": {
                "navigateOrService": "NAVIGATE",
                "target": ""
            },
            "webhookUsed": False,
            "webhookForSlotFilling": False,
            "lastUpdate": 1528120747,
            "fallbackIntent": False,
            "events": [],
            "userSays": [],
            "followUpIntents": [],
            "templates": []}

    def add_case(self, case):
        self.intent['userSays'].append(case.user_case)


class UserInput:
    def __init__(self, text):
        self.user_case = {
            "id": "",
            "data": [
                {
                    "text": "{t}".format(t=text),
                    "userDefined": False
                }
            ],
            "isTemplate": False,
            "count": 0,
            "updated": 0,
            "isAuto": False
        }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Form intent json for DialogFlow from text file with phrases")
    parser.add_argument('-i', dest='file_path', type=str, help='Path to file with phrases', required=True)
    parser.add_argument('-o', dest='json_path', type=str, help='Path to result json', required=True)
    args = parser.parse_args()
    if os.path.exists(args.file_path) and os.path.isfile(args.file_path):
        fileContent = parse_file(args.file_path)
        if not os.path.exists(args.json_path):
            form_json(fileContent, args.json_path)
        else:
            print('File {fp} already exists.'.format(fp=args.json_path))
            prompt = input('Overwrite? Y/N\n')
            if prompt.strip().casefold() in {'y', 'yes'}:
                print('Overwriting...')
                form_json(fileContent, args.json_path)
            else:
                print('Exiting...')
                exit(0)
    else:
        print('File {fp} not found'.format(fp=args.file_path))
        exit(1)
