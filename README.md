This script uses Playwright for Python to load a webpage in a headless Chromium browser and export its fully rendered HTML. It waits for the page to finish loading (including JavaScript-rendered content), making it ideal for saving dynamic pages that require client-side rendering.

🔧 Features:

  Uses playwright.sync_api for synchronous, simple usage
  
  Waits for network idle to ensure full page load
  
  Saves clean, final HTML output to file
  
  Useful for archiving, scraping, or offline analysis of dynamic websites

📦 Example usage:
  export_rendered_html("https://www.google.com/", "output/saved_google.html")

  
📁 Output: HTML file saved with all client-side rendering included.

