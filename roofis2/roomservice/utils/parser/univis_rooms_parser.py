import requests
import xmltodict


def loadPage(url: str):
    return requests.get(url).content


def getRoom(dict: dict):
    rooms = []
    for room in dict['UnivIS']['Room']:
        rooms.append(room)
    return rooms


def getPersons(dict: dict):
    persons = []
    for person in dict['UnivIS']['Person']:
        persons.append(person)
    return persons


def parsePage(url):
    page = loadPage(url)
    dict = xmltodict.parse(page)
    rooms = getRoom(dict)
    return rooms
