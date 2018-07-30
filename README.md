# Stackery Hello World - Python 3.6

This is a sample template for a serverless AWS Lambda application, written in Python.

This application contains two Lambda Functions.  getWelcomePage function
responds to web request events from an API Gateway endpoint.  logErrors
processes a centralized stream of all Lambda error within this app.

The application arcitecture is defined in template.yaml, a Serverless
Application Model (SAM) template which can be managed through the Stackery UI
at app.stackery.io.

Here is an overview of the files:

```bash
.
├── README.md                   <-- This README file
├── src                         <-- Source code dir for all AWS Lambda functions
│   ├── getWelcomePage          <-- Source code dir for getWelcomePage function
│   │   ├── README.md           <-- Function specific README
│   │   ├── handler.py          <-- Lambda function code
│   │   ├── requirements.txt    <-- Python pip dependencies
│   │   └── welcome.html        <-- HTML welcome page returned by Lambda function
│   └── logErrors               <-- Source code dir for logErrors function
│       ├── README.md           <-- Function specific README
│       ├── handler.py          <-- Lambda function code
│       └── requirements.txt    <-- Python pip dependencies
└── template.yaml               <-- SAM infrastructure-as-code template
```

