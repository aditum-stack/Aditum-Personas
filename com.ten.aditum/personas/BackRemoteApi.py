import json
from entity.Person import *

import requests

personUrl = "http://localhost:9006/person"
recordUrl = "http://localhost:9006/record"

headers = {'content-type': 'application/json'}


def getForAllPerson():
    """
    获取所有person
    :return: person[]
    """
    return requests.get(personUrl, params={}, headers=headers).json().get("data")


def getForAllRecord():
    """
    获取所有record
    :return: record[]
    """
    return requests.get(recordUrl, params={}, headers=headers).json().get("data")


def getForRecordByPersonId(personId):
    """
    获取指定person的所有record
    :param personId: personId
    :return: record[]
    """
    request = {"personnelId": personId}
    return requests.get(recordUrl, params=request, headers=headers).json().get("data")


personList = getForAllPerson()
recordList = getForAllRecord()

for person in personList:
    print(person)

    personEntity = Person(person)

    recordByPersonId = getForRecordByPersonId(personEntity.personnelId)

    for record in recordByPersonId:
        print(record)




# print(getForAllPerson())
# print(json.loads(getForPerson(requestData).text).get("data")[0])
