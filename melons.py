"""Classes for melon orders."""
class AbstractMelonOrder(object):
    def __init__(self, species, qty, order_type, tax):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
    
        
    def mark_shipped(self):
        self.shipped = True 


    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        total = (1 + self.tax) * self.qty * self.base_price
        christmas_total = (1 + self.tax) * self.qty * (1.5 * self.base_price)
        if species != "Christmas Melons":
            return total
        else: 
            return christmas_total



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
        self.flat_fee = 3
        if qty < 10: 
            return self.flat_fee + total 
        else:
            return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
