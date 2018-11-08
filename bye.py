import simplejson, urllib

GEOCODE_BASE_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

def geocode(address, **geo_args):
    geo_args.update({
        'address': address
    })

    url = GEOCODE_BASE_URL + '?' + urllib.urlencode(geo_args)
    result = simplejson.load(urllib.urlopen(url))

    print simplejson.dumps([s['formatted_address'] for s in result['results']], indent=2)

if __name__ == '__main__':
    geocode(address="San+Francisco")
