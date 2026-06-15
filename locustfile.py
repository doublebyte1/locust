from locust import HttpUser, task

#wfs = 'https://www.mapsforeurope.org/maps/wfs?SERVICE=WFS&VERSION=1.1.0&REQUEST=GetFeature&typename=ome:egm_wfs_coastl&token=$OEMAPS'

#oaf = 'https://emotional.byteroad.net/collections/hex350_grid_cardio_1920/items?limit=10000'
#oaf = 'https://k8.byteroad.net/collections/cos2018v3/items?limit=50'
#oat='https://tests.byteroad.net/collections/srup_defesa_militar_zonas/tiles/WebMercatorQuad/6/25/30?f=pbf'
#lp = 'https://k8.byteroad.net'

#oam = 'https://ogcapi.dgterritorio.gov.pt/collections/cosc2018'
#oaf = 'https://ogcapi.dgterritorio.gov.pt/collections/srup_arvores_point'
oat = 'https://ogcapi.dgterritorio.gov.pt/collections/srup_arvores_point/tiles'

# oam = 'https://k8.byteroad.net/collections/cosc2018'
# oaf = 'https://k8.byteroad.net/collections/srup_arvores_point'
# oat = 'https://k8.byteroad.net/collections/srup_arvores_point/tiles'

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get(oat)