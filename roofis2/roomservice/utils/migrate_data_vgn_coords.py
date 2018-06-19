from apps.donar.models import VGN_Coords


def migrate():
    locations = []
    locations.append(
        {'location': 'Erba', 'vgn_key': 'coord%3A4418901%3A629758%3ANAV4%3ABamberg%2C An der Weberei 5',
         'lat': '49.90316',
         'lon': '10.86932'})
    locations.append(
        {'location': 'Feki', 'vgn_key': 'coord%3A4421412%3A629361%3ANAV4%3ABamberg%2C Feldkirchenstraße 21',
         'lat': '49,9070328',
         'lon': '10,9041714'})
    locations.append(
        {'location': 'Markushaus', 'vgn_key': 'coord%3A4419902%3A630599%3ANAV4%3ABamberg%2C Markusplatz 3',
         'lat': '49.89552',
         'lon': '10.88348'})
    locations.append(
        {'location': 'Austraße', 'vgn_key': 'coord%3A4420153%3A630781%3ANAV4%3ABamberg%2C An der Universität 7',
         'lat': '49.89411',
         'lon': '10.88726'})
    locations.append(
        {'location': 'Kranen', 'vgn_key': 'coord%3A4420141%3A630965%3ANAV4%3ABamberg%2C Am Kranen 10',
         'lat': '49.89259',
         'lon': '10.88701'})
    locations.append(
        {'location': 'Kärntenstr', 'vgn_key': 'coord%3A4421130%3A628738%3ANAV4%3ABamberg%2C Kärntenstraße 7',
         'lat': '49.91256',
         'lon': '10.90028'})
    locations.append(
        {'location': 'Kapellenstr', 'vgn_key': 'coord%3A4421682%3A631169%3ANAV4%3ABamberg%2C Kapellenstraße 13',
         'lat': '49.89063',
         'lon': '10.90846'})
    locations.append(
        {'location': 'Volkspark', 'vgn_key': 'coord%3A4423077%3A629976%3ANAV4%3ABamberg%2C Pödeldorfer Straße 180',
         'lat': '49.90087',
         'lon': '10.92998'})
    locations.append(
        {'location': 'K16', 'vgn_key': 'coord%3A4420069%3A630807%3ANAV4%3ABamberg%2C Kapuzinerstraße 16',
         'lat': '48.127',
         'lon': '11.5572'})
    locations.append(
        {'location': 'Zwinger', 'vgn_key': 'coord%3A4420461%3A631411%3ANAV4%3ABamberg%2C Am Zwinger 4',
         'lat': '49.88843',
         'lon': '10.8918'})
    locations.append(
        {'location': 'AULA', 'vgn_key': 'coord%3A4420062%3A631052%3ANAV4%3ABamberg%2C Dominikanerstraße 2',
         'lat': '49.89165',
         'lon': '10.88602'})
    locations.append(
        {'location': 'Fischstr', 'vgn_key': 'coord%3A4420141%3A630930%3ANAV4%3ABamberg%2C Fischstraße 5',
         'lat': '49.89277',
         'lon': '10.88717'})
    locations.append(
        {'location': 'Fleischstr', 'vgn_key': 'coord%3A4420204%3A630739%3ANAV4%3ABamberg%2C Fleischstraße 2',
         'lat': '49.89453',
         'lon': '10.88791'})
    for location in locations:
        location_obj, created = VGN_Coords.objects.get_or_create(name=location['location'], coords=location['vgn_key'],
                                                                 latitude=location['lat'], longitude=location['lon'])
        if not created:
            print("Duplicate! Start Update: " + location['location'])
            location_obj.name = location['location']
            location_obj.coords = location['vgn_key']
            location_obj.latitude = location['lat']
            location_obj.longitude = location['lon']
