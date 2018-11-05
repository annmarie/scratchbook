import requests

def get_forecast(ll):
    url = 'https://api.darksky.net/forecast'
    key = 'dcb4f74964e7a1327be2b2b23557c927'
    return requests.get('{}/{}/{}'.format(url, key, ll))

def simple_forecast(latlong):
    resp = get_forecast(latlong)
    rset = resp.json()
    summary = [
        rset['currently']['summary']+".",
        rset['minutely']['summary'],
        rset['hourly']['summary'],
        rset['daily']['summary'],
    ]
    return " ".join(summary)

def simple_forecast_by_key(key):
    latlongs = {
        'LIC': '40.741897,-73.954211',
        'NYU': '40.729932,-73.998405',
        'W57': '40.765565,-73.979787',
    }
    return simple_forecast(latlongs[key])


if __name__ == '__main__':
    forecasts = []
    for key in ['LIC', 'W57', 'NYU']:
        forecasts.append(key+': '+simple_forecast_by_key(key))

    for forecast in forecasts:
        print(forecast)
        print('---')

