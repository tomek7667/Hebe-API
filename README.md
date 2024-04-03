# Hebe API

[![Test](https://github.com/tomek7667/Hebe-API-python/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/tomek7667/Hebe-API-python/actions/workflows/test.yml)
Unofficial library for programmatic access to your Hebe account and your orders.

Unofficial library for programmatic access to your Hebe account and your orders.

JS/TS equivalent can be found at the [hebe-api npm package](https://www.npmjs.com/package/hebe-api)


## ▶️ Use

Install the package

```
pip3 install hebe-api
```

## 📖 Getting Started

### Obtaining Hebe security token

```python
from hebe_api import Hebe

hebe = Hebe("HEBE_USERNAME", "HEBE_PASSWORD")
hebe.authenticate()
print(hebe.token)
# T2a...................
```

or

```python
from hebe_api import Hebe

hebe = Hebe()
hebe.authenticate("HEBE_USERNAME", "HEBE_PASSWORD")
print(hebe.token)
# E9U...................
```

### Obtaining user orders

```python
# Default values are as follows:
orders = hebe.get_orders(start=0, max_orders=100)

# order attributes
order = orders[0]
order.id # str
order.position # int (index in the array, used for retrieving the order products)
order.date # str
order.price # float
order.price_str # str
order.packs # int
```

### Obtaining products of particular order

```python
# Default values are as follows:
products = hebe.get_order_products(order)

# product attributes
product = products[0]
product.title # str
product.subtitle # str
product.total_price_str # str
product.package_price_str # str
product.total_price # float
product.package_price # float
product.quantity # int
```

### Obtaining all products

```python
# Default values are as follows:
all_products = hebe.get_all_products(max_orders=100)
```

## Roadmap

-   polish API supporting:
    -   [x] auth
    -   [x] get orders
    -   [x] get products
-   `.com` hebe API support
    -   [ ] auth
    -   [ ] get orders
    -   [ ] get products
