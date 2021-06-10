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
