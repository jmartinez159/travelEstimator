

/**
 * @type {import('@types/aws-lambda').APIGatewayProxyHandler}
 */


// exports.handler = async (event) => {

//     console.log(event);
//     const locationId = event.pathParameters.locationId;
//     const location = {'locationId': locationId, 'locationName': locationId };
//     const response = {
//         statusCode: 200,
//         headers: {

//             "Access-Control-Allow-Origin": "*",
//             "Access-Control-Allow-Headers": "*"
//         },
//         body: JSON.stringify(location),        
//     };

//     return response;
// };