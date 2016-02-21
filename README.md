# EVE Notifications - RSS Settings
This is a settings service to expose the storage and searching of user settings
for the [RSS provider](https://github.com/Regner/en-rss).

# External API

## External
Route: ``/external/``

### GET
* Auth: False

Details about all of the RSS feeds to be tracked by the RSS provider along with
if the feed is a CCP official source or a third-party source.

```
{
  "cz": {
    "url": "http://crossingzebras.com/feed/",
    "official": false,
    "name": "Crossing Zebras"
  },
  "eve-news": {
    "url": "http://newsfeed.eveonline.com/en-US/44/articles/page/1/20",
    "official": true,
    "name": "EVE Online News"
  },
  "eve-blogs": {
    "url": "http://newsfeed.eveonline.com/en-US/2/articles/page/1/20",
    "official": true,
    "name": "EVE Online Dev Blogs"
  },
  "eve-dev-blogs": {
    "url": "http://newsfeed.eveonline.com/en-US/95/articles",
    "official": true,
    "name": "EVE Online Developers Dev Blogs"
  },
  "en24": {
    "url": "http://evenews24.com/feed/",
    "official": false,
    "name": "EVE News 24"
  }
}
```

## External Character Settings
Route: ``/external/characters/<character_id>/

### GET
* Auth: True

Get the settings for a given character ID.

```
{
    "cz": true,
    "eve-news": true,
    "eve-blogs" false,
    "eve-dev-blogs": true,
    "en24": false
}
```

### PUT
* Auth: True

Allows the updating of the settings for a given character. When putting to this
resource all possible settings must be sent. These settings can be gotten from
the /external/ resource.

```
{
    "cz": true,
    "eve-news": true,
    "eve-blogs" false,
    "eve-dev-blogs": true,
    "en24": false
}
```

## Internal
Route: ```/internal/<string:feed_id>```

### GET
Auth: False

Returns a list of all character IDs that have subscribed to a given feed ID.

```
[
    9000001,
    9000002,
    9000003
]
```
