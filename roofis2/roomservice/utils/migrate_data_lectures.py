from datetime import datetime
import json
from pprint import pprint
from django.db.utils import IntegrityError
from roomservice.utils.parser import univis_lectures_parser
from roomservice.models import Lecture, LectureSpecifiaction, OrgUnit, LectureType, LectureTerm

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


def writeUnivisLectureTermsInDB(lecture, lecture_obj):
    if 'terms' in lecture:
        if type(lecture['terms']['term']) == list:
            logger.info(lecture['terms']['term'])
            for term in lecture['terms']['term']:
                logger.info(term)
                exclude = dict(term).get('exclude')
                starttime = dict(term).get('starttime')
                endtime = dict(term).get('endtime')
                startdate = dict(term).get('startdate')
                enddate = dict(term).get('enddate')
                repeat = dict(term).get('repeat')
                room = dict(term).get('room')
                if not room:
                    logger.info('ROOOOOOOOM ___________________________________________')
                    logger.info(lecture['terms'])
                term_obj, _ = LectureTerm.objects.update_or_create(exclude=exclude,
                                                                   repeat=repeat,
                                                                   room=room,
                                                                   lecture=lecture_obj)

                if startdate:
                    term_obj.start_date = dict(term).get('startdate')  # datetime.strptime(startdate, '%Y-%m-%d')
                if enddate:
                    term_obj.end_date = dict(term).get('enddate')  # datetime.strptime(enddate, '%Y-%m-%d')
                if starttime:
                    term_obj.start_time = dict(term).get('starttime')  # datetime.strptime(starttime, '%H:%M')
                if endtime:
                    term_obj.end_time = dict(term).get('endtime')  # datetime.strptime(endtime, '%H:%M'),
                term_obj.save()

        else:
            term = lecture['terms']['term']
            exclude = dict(term).get('exclude')
            starttime = dict(term).get('starttime')
            endtime = dict(term).get('endtime')
            startdate = dict(term).get('startdate')
            enddate = dict(term).get('enddate')
            repeat = dict(term).get('repeat')
            room = dict(term).get('room')
            if not room:
                logger.info('ROOOOOOOOM2 ___________________________________________')
                logger.info(lecture)

            term_obj, _ = LectureTerm.objects.update_or_create(exclude=exclude,
                                                               repeat=repeat,
                                                               room=room,
                                                               lecture=lecture_obj)
            if startdate:
                term_obj.start_date = dict(term).get('startdate')  # datetime.strptime(startdate, '%Y-%m-%d')
            if enddate:
                term_obj.end_date = dict(term).get('enddate')  # datetime.strptime(enddate, '%Y-%m-%d')
            if starttime:
                term_obj.start_time = dict(term).get('starttime')  # datetime.strptime(starttime, '%H:%M')
            if endtime:
                term_obj.end_time = dict(term).get('endtime')  # datetime.strptime(endtime, '%H:%M'),
            term_obj.save()


def writeUnivisLectureDataInDB(data):
    for lecture in data:
        if not 'courses' in lecture:
            lecture = dict(lecture)
            univis_key = lecture['@key']
            univis_id = lecture['id']
            short = lecture.get('short')
            name = lecture['name']
            url_description = lecture.get('url_description')
            turnout = lecture.get('turnout')
            if name == 'Projektpraktikum Mensch-Computer-Interaktion':
                logger.info(lecture)
            organizational = lecture.get('organizational')
            time_description = lecture.get('time_description')
            summary = lecture.get('summary')
            orgname, _ = OrgUnit.objects.get_or_create(title=lecture['orgname'])

            ects_cred = lecture.get('ects_cred')
            if ects_cred:
                ects_cred = float(str(lecture['ects_cred']).replace(',', '.'))

            sws = None
            if 'sws' in lecture:
                sws = float(str(lecture['sws']).replace(',', '.'))

            type = None
            if 'type' in lecture:
                type, _ = LectureType.objects.get_or_create(name=lecture['type'])

            # logger.info(name)
            lecture_obj, _ = Lecture.objects.update_or_create(univis_id=univis_id, univis_key=univis_key, title=name,
                                                              orgname=orgname, short=short, ects=ects_cred,
                                                              sws=sws, url_description=url_description,
                                                              estimated_visitor=turnout, organizational=organizational,
                                                              time_description=time_description, summary=summary,
                                                              type=type)

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
            writeUnivisLectureTermsInDB(lecture, lecture_obj)
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
    # logger.info(showStatus("Start SoWi:"))
    # writeUnivisLectureDataInDB(univis_lectures_parser.parsePage(univis_lectures(FAKULTAET_SoWi)))
    # logger.info("----------------------------------------------------------------------------------------")
    #
    # logger.info(showStatus("Start GuK:"))
    # writeUnivisLectureDataInDB(univis_lectures_parser.parsePage(univis_lectures(FAKULTAET_GuK)))
    # logger.info("----------------------------------------------------------------------------------------")
    #
    # logger.info(showStatus("Start HuWi:"))
    # writeUnivisLectureDataInDB(univis_lectures_parser.parsePage(univis_lectures(FAKULTAET_HuWi)))
    # logger.info("----------------------------------------------------------------------------------------")

    logger.info(showStatus("Start WIAI:"))
    writeUnivisLectureDataInDB(univis_lectures_parser.parsePage(univis_lectures(FAKULTAET_WIAI)))
    pprint("----------------------------------------------------------------------------------------")

    logger.info(showStatus("Finished:"))


if __name__ == '__main__':
    main()
