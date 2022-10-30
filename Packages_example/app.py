# first way to import the entire module

from ecommerce.shipping import calculate_shipping
from ecommerce import shipping

# Second approach
import ecommerce.shipping

ecommerce.shipping.calculate_shipping()
calculate_shipping()
