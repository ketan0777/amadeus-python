from amadeus.client.decorator import Decorator
from amadeus.reference_data.locations._airports import Airports


class Locations(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.airports = Airports(client)

    def get(self, **params):
        '''
        Returns details for a specific airport.

        .. code-block:: python


            from amadeus import Location

            client.reference_data.locations.get(
                keyword='lon',
                subType=Location.ANY
            )

        :param keyword: keyword that should represent the  start of
            a word in a city or airport name or code

        :param subType: a comma seperate list of location types to search
            for. You can use :class:`amadeus.Location` as a helper for this.

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v1/reference-data/locations', **params)
