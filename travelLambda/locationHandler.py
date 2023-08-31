import json
import requests

''' 
This function gets user input from app to search general country information
API : https://rapidapi.com/natkapral/api/countries-cities
'''

def lambda_handler(event, context):
    
    #   Get information from user in event and use it to search
    url = "https://countries-cities.p.rapidapi.com/location/country/list"

    querystring = {"format":"json"}

    headers = {
	    "X-RapidAPI-Key": "b98119d8c5msh632f046e3eb67a4p108477jsn0f102cf7978c",
	    "X-RapidAPI-Host": "countries-cities.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    #print(response.json())
    res = response.json()
    countryCodes = list(res['countries'].keys())    #list of keys for res['countries']
    #   Find country code
    resultCode = 'None' 
    for key in countryCodes:
        #check for matching country
        if res['countries'][key] == event['to']:
            print('Found: ',event['to'], ' -> ',key)
            resultCode = key    #store result
            break
    #   Check if valid code
    if resultCode == 'None':
        return {
            'statusCode' : 100,
            'body' : json.dumps('Error: Country not found')
        }
        
    #    Make second call to API with country code to get country capital
    url = "https://countries-cities.p.rapidapi.com/location/country/" + resultCode

    headers = {
	    "X-RapidAPI-Key": "b98119d8c5msh632f046e3eb67a4p108477jsn0f102cf7978c",
	    "X-RapidAPI-Host": "countries-cities.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    res1 = response.json()
    print(res1['status'])
    
    #   Check response
    if res1['status'] == 'failed':
        return {
            'statusCode' : 401,
            'body' : json.dumps('Error : No Capital found')
        }
        
    print(res1['capital']['name'])
    print(res1['continent']['name'])
    capital = res1['capital']['name']
    #   Return the country's info
    return {
        'statusCode': 200,
        'body': capital
    }
