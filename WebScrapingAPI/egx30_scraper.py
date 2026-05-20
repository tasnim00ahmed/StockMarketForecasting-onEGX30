import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Set up Selenium
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run without GUI
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the webpage
url = "https://www.investing.com/indices/egx30-historical-data"
driver.get(url)

# Wait until the table is fully loaded
try:
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )
    rows = table.find_elements(By.TAG_NAME, "tr")

    data = []
    for row in rows[1:]:  # Skip header row
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) > 6:
            data.append([
                cols[0].text,  # Date
                cols[1].text,  # Price
                cols[2].text,  # Open
                cols[3].text,  # High
                cols[4].text,  # Low
                cols[5].text,  # Vol.
                cols[6].text   # Change %
            ])

    # Save new data to CSV
    new_df = pd.DataFrame(data, columns=["Date", "Price", "Open", "High", "Low", "Vol.", "Change %"])
    new_df.to_csv("egx30_data2.csv", index=False)
    print("New data saved: egx30_data2.csv")

except Exception as e:
    print("Error while extracting data:", e)

finally:
    driver.quit()


# ================= MERGE WITH EXISTING DATA ================= #

# Load old dataset if it exists
if os.path.exists("merged_dataset.csv"):
    old_df = pd.read_csv("merged_dataset.csv")
else:
    old_df = pd.read_csv("EGX30_2000-2025.csv")

# Convert 'Date' column to datetime format
new_df["Date"] = pd.to_datetime(new_df["Date"])
old_df["Date"] = pd.to_datetime(old_df["Date"])

# Clean 'Change %' column
new_df['Change %'] = new_df['Change %'].str.replace('+', '', regex=False)

# Concatenate new data in front of old data
merged_df = pd.concat([new_df, old_df])

# Remove duplicate rows based on 'Date' column (keep latest entry)
merged_df = merged_df.drop_duplicates(subset=["Date"], keep="first")

# Sort by date in descending order (latest first)
merged_df = merged_df.sort_values(by="Date", ascending=False)

# Save the updated dataset
merged_df.to_csv("merged_dataset.csv", index=False)

print("Datasets merged successfully! Updated data saved in merged_dataset.csv")
