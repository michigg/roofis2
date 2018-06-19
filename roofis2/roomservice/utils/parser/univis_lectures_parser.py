import requests
import datetime
import xmltodict
import json
from pprint import pprint


def loadPage(url: str):
    return requests.get(url).content


def getDay():
    return datetime.datetime.today().strftime("%A, %d.%m.%Y")


def getLectures(dict: dict):
    lectures = []
    for lecture in dict['UnivIS']['Lecture']:
        lectures.append(lecture)
    return lectures


def parsePage(url):
    page = loadPage(url)
    dict = xmltodict.parse(page)
    lectures = getLectures(dict)
    return lectures

# parsePage(    "http://univis.uni-bamberg.de/prg?search=lectures&department=Fakult%E4t%20Geistes-%20und%20Kulturwissenschaften&show=exml")
