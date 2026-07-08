from playwright.sync_api import expect, sync_playwright

LOGIN_HTML = """
<!doctype html>
<html lang="en">
  <body>
    <main>
      <h1>QA Smoke Login</h1>
      <form aria-label="Login form">
        <label for="email">Email</label>
        <input id="email" name="email" type="email" />
        <label for="password">Password</label>
        <input id="password" name="password" type="password" />
        <button type="button" id="submit">Sign in</button>
      </form>
      <p id="status" role="status">Waiting</p>
    </main>
    <script>
      document.getElementById('submit').addEventListener('click', () => {
        const email = document.getElementById('email').value;
        document.getElementById('status').textContent = email.includes('@') ? 'Signed in' : 'Invalid email';
      });
    </script>
  </body>
</html>
"""


def test_real_playwright_chromium_smoke():
    """Run a real browser smoke without external servers, credentials, or paid APIs."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.set_content(LOGIN_HTML)
        expect(page.get_by_role("heading", name="QA Smoke Login")).to_be_visible()
        page.get_by_label("Email").fill("qa@example.test")
        page.get_by_label("Password").fill("synthetic-password")
        page.get_by_role("button", name="Sign in").click()
        expect(page.get_by_role("status")).to_have_text("Signed in")
        browser.close()
