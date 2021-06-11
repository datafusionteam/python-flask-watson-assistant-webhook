# NodeJS Webhook for IBM Cloud Functions

This module contains code which implements an order-status webhook in JavaScript for IBM Cloud Functions. In 
order to edit and deploy your changes you first need to follow these setup steps.

## Setup

1. First, follow [this tutorial](https://cloud.ibm.com/docs/openwhisk?topic=openwhisk-cli_install) on how to install and setup the `ibmcloud` CLI.
2. Next, if you haven't already, you will need to create a namespace and target a resource group by following [these steps](https://cloud.ibm.com/docs/openwhisk?topic=openwhisk-namespaces).
3. Lastly, you will need to target a namespace by following [these steps](https://cloud.ibm.com/docs/openwhisk?topic=openwhisk-namespaces#targeting-namespaces).

## Development

Assuming you have NodeJS already installed, run the following command in this directory:

```
npm install
```

This should generate a `node_modules` folder which contains all the packages needed to execute your webhook. If you want to add a package simply run `npm install` followed by the name of the package.

## Building

To build a distributable for your webhook simply run the following command:

```
npm run build
``` 

This will create a `dist/` directory containing a file named `bundle.js` which contains your compiled webhook code.

## Deployment

Before deployment, make sure you have changed the webhook package name. This can be found inside `package.json` under the script command `deploy`. The default package name is `order-status-webhook`. When you are ready to deploy your built code run the following command:

```
npm run deploy
```

This should deploy your packaged code to IBM Cloud Functions if you did the setup correctly. You can find your webhook by navigating to the functions service on IBM cloud, clicking actions, and finding the action which matches the package name you configured.