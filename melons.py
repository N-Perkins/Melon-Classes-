"""Classes for melon orders."""
class AbstractMelonOrder(object):
    def __init__(self, species, qty, order_type, tax):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
        self.base_price = 5

    def mark_shipped(self):
        self.shipped = True 


    def get_total(self):
        """Calculate price, including tax."""

        total = (1 + self.tax) * self.qty * self.base_price

        return total


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)




class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17)

        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
