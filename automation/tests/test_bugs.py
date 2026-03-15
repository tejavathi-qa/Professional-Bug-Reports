import pytest
from playwright.sync_api import expect
from ..pages.cart_page import CartPage

def test_negative_quantity_bug(page):
    """
    Bug #1: Verify that entering a negative quantity results in a negative total.
    """
    cart_page = CartPage(page)
    cart_page.navigate("product_details/1")
    
    # Enter negative quantity
    cart_page.set_quantity(-5)
    cart_page.page.click("button:has-text('Add to cart')")
    
    # View cart
    page.click("u:has-text('View Cart')")
    
    # Verify negative total
    total_text = cart_page.get_first_product_total()
    assert "-" in total_text, f"Expected negative total, but got {total_text}"

def test_server_error_on_unauthenticated_logout(page):
    """
    Bug #2: Verify server error (500) when accessing /logout without being logged in.
    """
    # Navigate directly to logout while unauthenticated
    response = page.goto("https://automationexercise.com/logout")
    
    # Verify status code is 500
    assert response.status == 500, f"Expected 500 status code, but got {response.status}"
    
    # Verify error page content
    page_content = page.content()
    assert "KeyError" in page_content, "Expected 'KeyError' to be present in server error page"

def test_footer_copyright_year(page):
    """
    Bug #7: Verify that the footer copyright year is outdated (2021).
    """
    page.goto("https://automationexercise.com/")
    footer_text = page.locator("footer").inner_text()
    assert "2021" in footer_text, f"Copyright year should be 2021 as per bug report, found: {footer_text}"
