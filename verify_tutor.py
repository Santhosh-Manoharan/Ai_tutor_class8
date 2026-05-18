import os
import time
import subprocess
import requests
from playwright.sync_api import sync_playwright

def verify_app():
    print("Starting Streamlit app...")
    port = "8503"
    process = subprocess.Popen(["streamlit", "run", "app.py", "--server.port", port, "--server.headless", "true"])

    url = f"http://localhost:{port}"
    max_retries = 60
    ready = False
    for i in range(max_retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                ready = True
                break
        except:
            pass
        time.sleep(5)
        print(f"Waiting for app to start... ({i+1}/{max_retries})")

    if not ready:
        print("App failed to start.")
        process.terminate()
        return False

    print("App is ready. Starting Playwright...")

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(url)

            print("Waiting for any text...")
            page.wait_for_load_state("networkidle")

            page.screenshot(path="initial_state.png")
            print("Initial screenshot saved.")

            # Try to find the input and button
            page.get_by_placeholder("e.g., What is photosynthesis?").fill("What is force?")
            page.click('button:has-text("Get Answer")')

            print("Clicked Get Answer, waiting...")
            time.sleep(10) # Wait for some processing

            page.screenshot(path="after_click.png", full_page=True)
            print("Screenshot after click saved.")

            browser.close()
            return True
    except Exception as e:
        print(f"An error occurred during verification: {e}")
        return False
    finally:
        process.terminate()

if __name__ == "__main__":
    verify_app()
