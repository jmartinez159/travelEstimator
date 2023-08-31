import React, { useEffect, useState} from 'react';
import { useLocation } from 'react-router-dom';
import AWS from 'aws-sdk';

AWS.config.update({
    region: 'us-west-1', // e.g., 'us-east-1'
    credentials: {
      accessKeyId: 'xxxxxxxxxxxxxxxx',
      secretAccessKey: 'xxxxxxxxxxxxxxxx'
    }
  });

const lambda = new AWS.Lambda();

const lambdaCountryHandler = async (data) => {
    try{

        const params = {
            FunctionName: 'travelHandler',
            Payload: JSON.stringify(data),
        };

        const response = await lambda.invoke(params).promise();
        const body = JSON.parse(response.Payload);
        console.log('Lambda Response:', response.Payload);
        console.log('Body: ', body['body']); //we want this one because it is the only list of cities
        return body;

    } catch(error){
        console.error('Error calling Lambda function:', error);
    }
}; 

function Results(){

    //getting information passed to us with state, useLocation()
    const {state} = useLocation();
    //Storing capital city of country traveling to 
    const [capital, setCapital] = useState("Loading..."); 
    //Storing countries entered by user 
    const {toCountry, fromCountry} = state;
    //Printing to validate data passed in
    console.log(toCountry, " <- ", fromCountry)
    //Storing it to be passed to Lambda function
    const data = {to: toCountry, from: fromCountry};
    //calling travelHandler lambda function
    useEffect(() => {
        lambdaCountryHandler(data).then(response => {
            //storing response which should be the capital city
            setCapital(response['body'])
        }).catch(error => {
            console.error('Error calling Lambda function:', error);
        });
    }, []);

    //printing results
    console.log('Result :', capital)

    return (
        <div className='Result'>
            <h1> Results </h1>
            <h2> {toCountry} from {fromCountry} </h2>
            <h2> {capital} </h2>
        </div>                
    )
}


export default Results;
