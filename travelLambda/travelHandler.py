import json
import boto3

client = boto3.client('lambda')

def lambda_handler(event, context):
    
    #Setting data to be passed as a parameter to the lambda function
    data = {'to' : event['to'], 'from' : event['from']}
    
    
    #  * Calling locationHandler Lambda function
    response = client.invoke(
        FunctionName='locationHandler',
        InvocationType='RequestResponse',
        Payload=json.dumps(data),
    )
    #Decoding response we get from calling the lambda function to get our country's capital city
    res = response['Payload'].read().decode('unicode_escape')
    resData = json.loads(res)
    capital = resData.get('body', None)
    print('Country Capital: ',capital)
    capital = str(capital)


    #  * Calling priceHandler Lambda function
    #print('Country :',event['to'])
    data2 = {'to' : event['to']}
    response2 = client.invoke(
        FunctionName='priceHandler',
        InvocationType='RequestResponse',
        Payload=json.dumps(data2),
    )
    res = response2['Payload'].read().decode('utf-8')
    # Need to parse the response we get from priceHandler 
    resData = json.loads(res)
    print('Price Handler result: ', res)
    priceTourist = -1   #default values in case of failed response
    priceLocal = -1
    # Error Handling : if no body in response
    if 'body' in resData:
        bodyData = json.loads(resData['body'])
        #want to keep them as floats because we don't preform any opertions with them 
        priceTourist = bodyData.get('tourist', None)    # string acting like a float
        priceLocal = bodyData.get('local', None)        # string acting like a float
        if priceTourist is not None and priceLocal is not None:
            print('Price Per Day(Tourist): ', priceTourist)
            print('\n')
            print('Price Per Day(Local): ', priceLocal)
        else:
            print('No price info found')
    else:
        print('No body found in Price Handler response')
        
        
    #  * Calling flightPriceHandler Lambda function 
    data1 = {'location' : capital}
    response1 = client.invoke(
        FunctionName='flightPriceHandler',
        InvocationType='RequestResponse',
        Payload=json.dumps(data1),
    )
    #   Getting Price of flights to selected country
    res = response1['Payload'].read().decode('utf-8')
    # Need to parse response from flightPriceHandler
    resData = json.loads(res)
    print('Flight Price Handler result: ', res)
    # Error Handling : if no response(often because of latency and unreliable API)
    flightPrices = 0
    ticketCount = 0
    if 'body' in resData:
        bodyData = json.loads(resData['body'])
        flightPrices = bodyData.get('prices', None)
        ticketCount = bodyData.get('ticketCount', None)
    else:
        print('No body found in Flight Handler response')
    
    if flightPrices is not None and ticketCount is not None:
        print('Average Flight Prices :', flightPrices)
        print('\n')
        print('Ticket count: ', ticketCount)
        
    #   Condense all our retrieved data to return to main application    
    result = {'priceTourist' : priceTourist, 'priceLocal' : priceLocal, 'flightPrices' : flightPrices, 'tickets' : ticketCount}    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
