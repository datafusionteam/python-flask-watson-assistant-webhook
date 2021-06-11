# Python Webhook for IBM Cloud Functions

This module contains code which implements an order-status webhook in python for IBM Cloud Functions. In 
order to edit and deploy your changes you first need to follow these setup steps.

## Setup

1. First, follow [this tutorial](https://cloud.ibm.com/docs/openwhisk?topic=openwhisk-cli_install) on how to install and setup the `ibmcloud` CLI.
2. Next, if you haven't already, you will need to create a namespace and target a resource group by following [these steps](https://cloud.ibm.com/docs/openwhisk?topic=openwhisk-namespaces).
3. Lastly, you will need to target a namespace by following [these steps](https://cloud.ibm.com/docs/openwhisk?topic=openwhisk-namespaces#targeting-namespaces).

## Development

To get setup for development you will first need to create a virtual environment. Execute this command in the current directory.

```
pip install virtualenv
```

Then we will create the virtual environment:

```
virtualenv virtualenv
```

Then activate it:

```
source virtualenv/bin/activate
```

Now you can install any necessary packages that you may need for your webhook. To do this, simply run `pip install` followed by the package name. Finally, you will need to add the package name to `requirements.txt`. 


## Packaging

Before packaging your webhook for the first time you should set the name of your webhook by changing the `PACKAGE_NAME` environment variable.
When you are ready to package your code for deployment run the following command:

```
make package
```

The output should be a zipped file that contains all the code to run the webhook. The name of the zipped file should be the package name you specified before.

## Deployment

To deploy your packaged code run the following command:

```
make deploy
```

This should deploy your packaged code to IBM Cloud Functions if you did the setup correctly. You can find your webhook by navigating to the functions service on IBM cloud, clicking actions, and finding the action which matches the package name you configured.
