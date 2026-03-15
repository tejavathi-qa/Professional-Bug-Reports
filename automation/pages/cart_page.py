from .base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_total = ".cart_total_price"
        self.quantity_input = "#quantity"
        self.add_to_cart_btn = ".add-to-cart"

    def set_quantity(self, qty):
        self.page.fill(self.quantity_input, str(qty))

    def add_product_to_cart(self):
        self.page.click(self.add_to_cart_btn)

    def get_first_product_total(self):
        return self.page.locator(self.cart_total).first.inner_text()
