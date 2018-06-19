from datetime import datetime
import json
from pprint import pprint
from django.db.utils import IntegrityError
from roomservice.utils.parser import univis_lectures_parser
from roomservice.models import Lecture, LectureSpecifiaction, OrgUnit, LectureType

import logging

logger = logging.getLogger(__name__)

# CONFIG Fakultaet
FAKULTAET_GuK = "Fakult%E4t%20Geistes-%20und%20Kulturwissenschaften"
FAKULTAET_SoWi = "Fakult%E4t%20Sozial-%20und%20Wirtschaftswissenschaften"
FAKULTAET_HuWi = "Fakult%E4t%20Humanwissenschaften"
FAKULTAET_WIAI = "Fakult%E4t%20Wirtschaftsinformatik"


# CONFIG ROOMS
def univis_rooms(fakultaet):
    return "http://univis.uni-bamberg.de/prg?search=rooms&department=" + fakultaet + "&show=xml"


# CONFIG LECTURES
def univis_lectures(fakultaet):
    return "http://univis.uni-bamberg.de/prg?search=lectures&department=" + fakultaet + "&show=exml"


def getJsonFromFile(path):
    with open(path, "r") as file:
        return json.load(file)


def writeUnivisLectureTermsInDB(lecture):
    logger.info('WTF')
    if 'terms' in lecture:
        if type(lecture['terms']['term']) == list:
            for term in lecture['terms']['term']:
                if 'exclude' in term:
                    logger.info('EXCLUDE: {}'.format(term['exclude']))
                try:
                    starttime = "00:00"
                    # term_obj = Lecture_Terms.objects.create(starttime=starttime)
                    if 'starttime' in term:
                        starttime = term['starttime']
                        # term_obj.starttime = datetime.strptime(starttime, "%H:%M")
                    # term_obj.save()
                    if 'room' in term:
                        room_id = term['room']['UnivISRef']['@key']
                        # term_obj.room.add(Room.objects.get(key=room_id))
                    # lecture_obj.term.add(term_obj)
                except IntegrityError as err:
                    logger.exception(err)

        else:
            try:
                univis_starttime = "00:00"
                # term_obj = Lecture_Terms.objects.create(starttime=univis_starttime)
                if 'starttime' in lecture['terms']['term']:
                    univis_starttime = lecture['terms']['term']['starttime']
                    # term_obj.starttime = datetime.strptime(univis_starttime, '%H:%M')
                # term_obj.save()
                if 'room' in lecture['terms']['term']:
                    room_id = lecture['terms']['term']['room']['UnivISRef']['@key']
                    # Room.objects.get(key=room_id)
                    # term_obj.room.add(Room.objects.get(key=room_id))
                # term_obj.save()
                # lecture_obj.term.add(term_obj)
            except IntegrityError as err:
                logger.exception(err)


def writeUnivisLectureDataInDB(data):
    for lecture in data:
        univis_key = lecture['@key']
        univis_id = lecture['id']
        name = lecture['name']
        orgname, _ = OrgUnit.objects.get_or_create(title=lecture['orgname'])

        short = None
        if 'short' in lecture:
            short = lecture['short']

        ects_cred = None
        if 'ects_cred' in lecture:
            ects_cred = float(str(lecture['ects_cred']).replace(',', '.'))

        sws = None
        if 'sws' in lecture:
            sws = float(str(lecture['sws']).replace(',', '.'))

        url_description = None
        if 'url_description' in lecture:
            url_description = lecture['url_description']

        turnout = None
        if 'turnout' in lecture:
            turnout = lecture['turnout']

        organizational = None
        if 'organizational' in lecture:
            organizational = lecture['organizational']

        time_description = None
        if 'time_description' in lecture:
            time_description = lecture['time_description']

        summary = None
        if 'summary' in lecture:
            summary = lecture['summary']

        type = None
        if 'type' in lecture:
            type, _ = LectureType.objects.get_or_create(name=lecture['type'])

        logger.info(name)
        lecture_obj, _ = Lecture.objects.update_or_create(univis_id=univis_id, univis_key=univis_key, title=name,
                                                          orgname=orgname, short=short, ects=ects_cred,
                                                          sws=sws, url_description=url_description,
                                                          estimated_visitor=turnout, organizational=organizational,
                                                          time_description=time_description, summary=summary, type=type)

        lecture_specs_options = LectureSpecifiaction.objects.all()
        for lecture_spec in lecture_specs_options:
            univis_id = lecture_spec.univis_id.lower()
            if univis_id in lecture and lecture[univis_id] == 'ja':
                lecture_obj.specification.add(lecture_spec)

        orgunits = None
        if 'orgunits' in lecture:
            for orgunit in lecture['orgunits']:
                if len(orgunit) > 0:
                    for orgunit in str(lecture['orgunits']['orgunit']).strip("[]").split(','):
                        cleaned_orgunit = orgunit.strip().strip("'").strip("'")
                        orgunit, _ = OrgUnit.objects.get_or_create(title=cleaned_orgunit)
                        lecture_obj.orgunits.add(orgunit)

                    # TODO: Check xml syntax #orgunit problem
                    pass
                else:
                    orgunit, _ = OrgUnit.objects.get_or_create(title=orgunit)
                    lecture_obj.orgunits.add(orgunit)

        # logger.info(lecture_obj)
        #     if 'dozs' in lecture:
        #         lecturer_id = dict(lecture['dozs']['doz']['UnivISRef'])['@key']
        # lecture_obj = Lecture.objects.create(univis_ref=key, univis_id=univis_id, name=name, short=short,
        #                                      type=lecture_type, lecturer_id=lecturer_id)
        # writeUnivisLectureTermsInDB(lecture, lecture_obj)
        # writeUnivisLectureTermsInDB(lecture)
        # lecture_obj.save()
        # logger.info("Lecture: {}".format(lecture_obj.short))
        # except IntegrityError as err:
        #     logger.warning('Lecture already exists')
        # logger.exception(err)


def showStatus(status: str):
    return "\nStatus: {status}\n\tLectures: {lectures}\n\tLecture Specifcation: {lecture_specs}\n\tLectureType: {lecture_type}\n\tOrg Unit: {orgunit}\n\n" \
        .format(
        status=status,
        lectures=Lecture.objects.count(),
        lecture_specs=LectureSpecifiaction.objects.count(),
        lecture_type=LectureType.objects.count(),
        orgunit=OrgUnit.objects.count()
    )


def main():
    # get food jsons
    logger.info(showStatus("Start SoWi:"))
    writeUnivisLectureDataInDB(univis_lectures_parser.parsePage(univis_lectures(FAKULTAET_SoWi)))
    logger.info("----------------------------------------------------------------------------------------")

    logger.info(showStatus("Start GuK:"))
    writeUnivisLectureDataInDB(univis_lectures_parser.parsePage(univis_lectures(FAKULTAET_GuK)))
    logger.info("----------------------------------------------------------------------------------------")

    logger.info(showStatus("Start HuWi:"))
    writeUnivisLectureDataInDB(univis_lectures_parser.parsePage(univis_lectures(FAKULTAET_HuWi)))
    logger.info("----------------------------------------------------------------------------------------")

    logger.info(showStatus("Start WIAI:"))
    writeUnivisLectureDataInDB(univis_lectures_parser.parsePage(univis_lectures(FAKULTAET_WIAI)))
    pprint("----------------------------------------------------------------------------------------")

    logger.info(showStatus("Finished:"))


if __name__ == '__main__':
    main()
