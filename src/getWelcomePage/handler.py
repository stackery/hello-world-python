def handler(message, context):
    print(message)
    with open('welcome.html') as f:
        responseBody = f.read()

    response = {
        'statusCode': 200,
        'headers': { 'Content-Type': 'text/html' },
        'body': responseBody
     }
    return response

