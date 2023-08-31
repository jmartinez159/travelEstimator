import json
import requests

def lambda_handler(event, context):
    
    #Setting up Cost of Living API
    # Examples of resulting calls is on - https://rapidapi.com/emir12/api/nomad-list-cities
    
    url = "https://nomad-list-cities.p.rapidapi.com/nomad-list/latin-america"

    querystring = {"size":"20","page":"1","sort":"desc","sort_by":"overall_score"}

    headers = {
	    "X-RapidAPI-Key": "b98119d8c5msh632f046e3eb67a4p108477jsn0f102cf7978c",
	    "X-RapidAPI-Host": "nomad-list-cities.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    res = response.json()   #saving response for traversal
    
    #Storing total cost per day if person is not local 
    totalCostTourist = 0
    #Soring total cost for local
    totalCostLocal = 0
    #how many cities found in nomad-list-cities api for country entered in search
    cityCount = 0
    #iterating through list of data in res 
    for i in range(len(res)):
        #if we find a match then we save data to pass down
        if res[i]['country'] == event['to']:
            cityCount = cityCount +1
            print(res[i]['name'])
            totalCostTourist = totalCostTourist + res[i]['cost_for_nomad_in_usd']/30
            totalCostLocal = totalCostLocal + res[i]['cost_for_local_in_usd']/30
    
    #If city was found then we display our data         
    if cityCount == 0:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: No cities found in that country')
        }
        
    data = {}
    data['tourist'] = totalCostTourist/cityCount
    data['local'] = totalCostLocal/cityCount
    print(data)

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }
