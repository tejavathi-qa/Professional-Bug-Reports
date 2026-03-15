# Professional Bug Reports: Tester's Mindset Showcase 🧪

This repository demonstrates high-quality manual testing and professional bug reporting. Instead of just theorizing, I've conducted a "Bug Bash" on a real-world testing site (**Automation Exercise**) to identify, document, and categorize defects ranging from UI glitches to critical server-side exceptions.

## 🎯 Objective
To showcase the "tester's mindset" by finding non-obvious bugs, including edge cases, security vulnerabilities, and functional failures, and reporting them in an industry-standard format suitable for high-performing engineering teams.

## 🛠️ Testing Methodology
1.  **Exploratory Testing:** Navigated through complex user journeys (Signup, Cart, Contact Us) to identify deviations from expected behavior.
2.  **Boundary Value Analysis:** Tested input fields with extreme values (e.g., negative quantities in the shopping cart).
3.  **Cross-Browser/Responsiveness Testing:** Verified layout stability across different viewport widths.
4.  **Error Handling & Security:** Attempted to trigger server errors and checked for exposed debug information.

## 📄 Artifacts
*   **[Bug Bash Report](Bug-Bash-Session-Report.md):** The comprehensive document containing 15 high-quality bug reports with steps to reproduce, severity levels, and evidence.
*   **[Evidence Folder](evidence/):** A collection of screenshots and log snippets captured during the testing session.
*   **[Automation Suite](automation/):** A Playwright-based Python framework that automates the reproduction of the reported bugs.

## 🤖 Automation Context
The automation suite follows the **Page Object Model (POM)** and is designed to run against the target site to verify the existence of reported defects.

### How to Run:
1.  Navigate to `automation/`
2.  Install dependencies: `pip install -r requirements.txt`
3.  Install Playwright browsers: `playwright install`
4.  Run tests: `pytest tests/test_bugs.py`

## 🚀 Key Bug Highlights
*   **Critical:** Negative order totals allowed in the shopping cart.
*   **Critical:** Server-side `KeyError` at `/logout` exposing Python/Django stack traces.
*   **Security:** Production site running with `DEBUG = True`, exposing sensitive system metadata.
*   **UX/UI:** Significant layout shifts and alignment issues on the Test Cases page.

---
**Author:** [Your Name/Portfolio]
**Target Site:** https://automationexercise.com/
