import json
import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta

def lambda_handler(event, context):
    
    #   making first api call to get airport code for flight ticket search 
    #   API: https://rapidapi.com/DataCrawler/api/tripadvisor16
    #       - Searches for airport by city
    url = "https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchAirport"

    querystring = {"query": event['location']}

    headers = {
	    "X-RapidAPI-Key": "b98119d8c5msh632f046e3eb67a4p108477jsn0f102cf7978c",
	    "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    #print(response.json())
    res = response.json()
    #print(res)
    
    #   check if one valid airport in country
    if not res['data']:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: No Airports Found')
        }
        
    #   get first airport
    print(res['data'][0]['airportCode'])
    airCode = res['data'][0]['airportCode']
    # get date one and two month(s) from current date 
    dateLeaving = datetime.now().date() + relativedelta(months=1)
    dateReturn = datetime.now().date() + relativedelta(months=1,weeks=1)
    print('Leaving date: ',dateLeaving)
    print('Return date: ',dateReturn)
    #   search flights using the resulting airport code and dates leaving and returning
    #   *all flights assume leaving from LAX airport and landing in the country's capital 
    url = "https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchFlights"

    querystring = {"sourceAirportCode":"LAX","destinationAirportCode": airCode,"date": dateLeaving,"itineraryType":"ROUND_TRIP","sortOrder":"PRICE","numAdults":"1","numSeniors":"0","classOfService":"ECONOMY","returnDate": dateReturn,"pageNumber":"1","currencyCode":"USD"}

    headers = {
	    "X-RapidAPI-Key": "b98119d8c5msh632f046e3eb67a4p108477jsn0f102cf7978c",
	    "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    res = response.json()
    #print('Response: ',res)
    
    #   Search through res to find ticket price information
    #   Add costs and total tickets to calculate average ticket cost
    priceTotal = 0
    totalTickets = 0
    ticketCount = len(res['data']['flights'])
    print(ticketCount)
    #   Looping through res to get all ticket prices
    for x in range(ticketCount):
        #   Ticket prices are in this array called 'purchaseLinks'
        for y in range(len(res['data']['flights'][x]['purchaseLinks'])):
            print('Price: $',res['data']['flights'][x]['purchaseLinks'][y]['totalPrice'])
            #   Recording/Updating data
            priceTotal = priceTotal + res['data']['flights'][x]['purchaseLinks'][y]['totalPrice']
            totalTickets = totalTickets +1
            
    if totalTickets == 0:
        return {
            'statusCode' : 401,
            'body' : 'Error: No Tickets found ' 
        }
    averagePrice = priceTotal/totalTickets 
    print('Total Tickets :',totalTickets)
    print('Average Price :',averagePrice)
    #   return costs to the main function
    send = {'prices': averagePrice, 'ticketCount': totalTickets}
    return {
        'statusCode': 200,
        'body': json.dumps(send)
    }
