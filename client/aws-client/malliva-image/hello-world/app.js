// const axios = require('axios')
// const url = 'http://checkip.amazonaws.com/';
let response;

/**
 *
 * Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format
 * @param {Object} event - API Gateway Lambda Proxy Input Format
 *
 * Context doc: https://docs.aws.amazon.com/lambda/latest/dg/nodejs-prog-model-context.html
 * @param {Object} context
 *
 * Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
 * @returns {Object} object - API Gateway Lambda Proxy Output Format
 *
 */
exports.lambdaHandler = async (event, context) => {
  try {
    console.debug('checking');
    console.debug({ event });

    let a = event.a ?? event.queryStringParameters['a'];
    let b = event.b ?? event.queryStringParameters['b'];
    let product = a * b;

    response = {
      statusCode: 200,
      body: JSON.stringify({
        message: product,
      }),
    };
    console.debug('response');
    console.log(response);
  } catch (err) {
    console.log(err);
    return err;
  }

  return response;
};
