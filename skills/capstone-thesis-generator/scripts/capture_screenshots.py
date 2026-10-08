#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated Live Web Application Screenshot Capture via Headless Selenium
Logs into local or remote web systems and captures clean, high-resolution
desktop (1440x900) and mobile responsive (390x844) PNG screenshots.
"""

import os
import time
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def capture_application_screens(base_url, login_url, username, password, routes, output_dir="screenshots"):
    """
    Automates authentication and captures screenshots of specified application routes.
    """
    os.makedirs(output_dir, exist_ok=True)

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1440,900')

    driver = webdriver.Chrome(options=options)
    captured = {}

    try:
        # 1. Capture Login Page
        print(f"Navigating to login: {login_url}")
        driver.get(login_url)
        time.sleep(1.5)
        login_img = os.path.join(output_dir, "01_login.png")
        driver.save_screenshot(login_img)
        captured["login"] = login_img
        print(f"Captured: {login_img}")

        # 2. Perform Login
        if username and password:
            try:
                u_input = driver.find_element(By.ID, "username")
                p_input = driver.find_element(By.ID, "password")
                u_input.send_keys(username)
                p_input.send_keys(password)
                
                # Submit button
                submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit'], .btn-submit, input[type='submit']")
                submit_btn.click()
                time.sleep(2)
                print(f"Logged in successfully. Landed on: {driver.current_url}")
            except Exception as e:
                print(f"Warning: Login submission skipped or failed: {e}")

        # 3. Capture Routes
        for idx, (route_name, path) in enumerate(routes.items(), start=2):
            target_url = path if path.startswith("http") else f"{base_url.rstrip('/')}/{path.lstrip('/')}"
            print(f"Navigating to: {target_url}")
            driver.get(target_url)
            time.sleep(2)
            out_file = os.path.join(output_dir, f"{idx:02d}_{route_name}.png")
            driver.save_screenshot(out_file)
            captured[route_name] = out_file
            print(f"Captured: {out_file}")

        # 4. Capture Mobile View for first main route
        if routes:
            first_route = list(routes.values())[0]
            target_url = first_route if first_route.startswith("http") else f"{base_url.rstrip('/')}/{first_route.lstrip('/')}"
            driver.set_window_size(390, 844) # iPhone viewport
            driver.get(target_url)
            time.sleep(2)
            mobile_img = os.path.join(output_dir, "mobile_responsive.png")
            driver.save_screenshot(mobile_img)
            captured["mobile"] = mobile_img
            print(f"Captured: {mobile_img}")

    finally:
        driver.quit()

    return captured

if __name__ == "__main__":
    pass
