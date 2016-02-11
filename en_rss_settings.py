

from eveauth.contrib.flask import authenticate

from flask import Flask, abort
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)

# App Settings
SERVICES = {
    'eve-news': {'name': 'EVE Online News', 'official': True},
    'eve-blogs': {'name': 'EVE Online Dev Blogs', 'official': True},
    'eve-dev-blogs': {'name': 'EVE Online Developers Dev Blogs','official': True},
    'cz': {'name': 'Crossing Zebras', 'official': False},
    'en24': {'name': 'EVE News 24', 'official': False},
]

# Datastore Settings
DS_CLIENT = datastore.Client()
SETTINGS_KIND = 'EN-RSS-SETTINGS'


class DatastoreClient(object):
    @staticmethod
    def get_client():
        if not hasattr(DatastoreClient, "_client"):
            DatastoreClient._client = datastore.Client()
        return DatastoreClient._client


def get_client():
    return DatastoreClient.get_client()


class Settings(Resource):
    def get(self):
        return SERVICES


class CharacterSettings(Resource):
    @authenticate()
    def get(self, character_id):
        client = get_client()
        character_settings = client.get(client.key(SETTINGS_KIND, character_id))
        
        if character_settings is None:
            abort(404)
        
        return dict(character_settings)
        
        
    @authenticate()
    def put(self, character_id):
        parser = reqparse.RequestParser()
        
        for feed in SERVICES:
            parser.add_argument(feed, type=bool, help=SERVICES[feed]['name'])

        args = parser.parse_args(strict=True)
        
        client = get_client()
        character_settings = client.get(client.key(SETTINGS_KIND, character_id))
        
        if character_settings is None:
            character_settings = datastore.Entity(client.key(SETTINGS_KIND, character_id))
        
        for feed in SERVICES:
            if feed in args:
                character_settings[feed] = args[feed]

        client.put(character_settings)

        return dict(character_settings), 204
    

api.add_resource(Settings, '/en-rss/')
api.add_resource(CharacterSettings, '/en-rss/<int:character_id>/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
