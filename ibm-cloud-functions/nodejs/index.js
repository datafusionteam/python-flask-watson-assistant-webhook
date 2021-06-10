const data = require("./data.json");

function main({ orderId, customerId }) {
  const customers = data.customers;
  const orders = data.orders;

  if (!orderId && !customerId) {
    return makeResponse({
      error: "Order id or customer id is required."
    }, 400)
  }

  // See if we can find an order that matches the ID given
  if (orderId) {
    const order = orders.find((order) => order.id === orderId);

    if (!order) {
      return makeResponse({
        text: `Sorry, I could not find an order with ID ${orderId}.`,
      });
    }

    const shippingStatus = getShippingStatus(
      order.shipping_status,
      order.shipping_provider
    );
    return makeResponse({
      text: `Your order for ${order.title} ${shippingStatus}. The tracking number is ${order.tracking_number}.`,
    });
  }

  // If no order ID is given then we can find three of the customers orders
  const customer = customers.find((customer) => customer.id === customerId);

  if (!customer) {
    return makeResponse({
      text: `Sorry, I could not find a customer with ID ${customerId}.`,
    });
  }

  const potentialCustomerOrders = customer.orders;
  potentialCustomerOrders.length = 3; // limit the orders to just three

  const options = potentialCustomerOrders.map((order) => ({
    label: `Order #${order}`,
    value: { input: { text: `What is the status of order ${order}` } },
  }));
  // Form a response that matches the structure of an options message from the docs
  const orderOptionsResponse = {
    response_type: "option",
    title: `Okay ${customer.name}. Which order do you want the status for?`,
    description: "",
    options,
  };
  return makeResponse({
    generic: [orderOptionsResponse],
  });
}

function makeResponse(body, statusCode = 200) {
  return {
    headers: { "Content-Type": "application/json" },
    statusCode,
    body,
  };
}

function getShippingStatus(status, provider) {
  switch (status) {
    case "IN_PROGRESS":
      return `is being processed by ${provider}`;
    case "SHIPPED":
      return `is being shipped by ${provider}`;
    case "DELIVERED":
      return `was delivered by ${provider}`;
    default:
      return "";
  }
}

global.main = main;
