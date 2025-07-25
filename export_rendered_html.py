from playwright.sync_api import sync_playwright

def export_rendered_html(url, output_file):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()  # new context to avoid login issues
        page = context.new_page()
        
        # Go to Google with full load wait
        page.goto(url, wait_until="networkidle")

        # Save the final HTML content
        content = page.content()
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        
        print(f"Saved: {output_file}")
        browser.close()

# Load Google and save as HTML
save_rendered_html("https://www.google.com/", "output/saved_google.html")
