import json


def main(params):
    order_id = params.get("orderId")
    customer_id = params.get("customerId")

    if order_id is None and customer_id is None:
        raise ValueError("Order id or customer id is required.")

    with open("data.json") as f:
        data = json.loads(f.read())
        orders = data.get("orders")
        customers = data.get("customers")

        # See if we can find an order that matches the ID given
        if order_id is not None:
            order = next((order for order in orders if order.get("id") == order_id), None)

            if order is None:
                return {
                    "text": f"Sorry, I could not find an order with ID {order_id}"
                }

            shipping_status = get_shipping_status(order.get("shipping_status"), order.get("shipping_provider"))
            return {
                "text": f"Your order for {order.get('title')} {shipping_status}. "
                        f"The tracking number is {order.get('tracking_number')}."
            }

        # If no order ID is given then we can find three of the customers orders
        customer = next((customer for customer in customers if customer.get("id") == customer_id), None)

        if customer is None:
            return {
                "text": f"Sorry, I could not find a customer with ID {customer_id}."
            }

        potential_orders = customer.get("orders", [])[:3]
        # Generate a mapping of order number to option objects from the docs
        order_options_map = lambda order_num: {
            "label": f"Order #{order_num}",
            "value": {"input": {"text": f"What is the status of order {order_num}"}}
        }
        options = list(map(order_options_map, potential_orders))
        # Form a response that matches the structure of an options message from the docs
        order_options_response = {
            "response_type": "option",
            "title": f"Okay, {customer.get('name')}. Which order do you want the status for?",
            "description": "",
            "options": options
        }
        return {
            "generic": [order_options_response]
        }


def get_shipping_status(status, provider):
    """Get the shipping status text

    :param status: One of (IN_PROGRESS, SHIPPED, or DELIVERED)
    :param provider: Shipping provider of the order
    :return: Shipping status text
    """
    if status == "IN_PROGRESS":
        return f"is being processed by {provider}"
    elif status == "SHIPPED":
        return f"is being shipped by {provider}"
    elif status == "DELIVERED":
        return f"was delivered by {provider}"
    else:
        return ""
