# Berlin Apartment Listing Scraper

This Python script automates the process of checking several German real estate websites for new apartment listings in Berlin. It uses Selenium WebDriver to scrape the websites, keeps track of listings already seen, and sends notifications for new finds.

**Note:** This script currently uses `mac_notifications` and is therefore primarily designed for macOS users.

## Features

* **Multi-Website Scraping:** Checks the following websites for new apartment listings:
    * Deutsche Wohnen (`Workspacelinks`) - *Currently commented out in main execution*
    * Heimstaden (via ImmobilienScout24 portal) (`Workspacelinks_heimstaden`)
    * Berlinhaus (`Workspacelinks_berlinhaus`) - *Currently commented out in main execution*
    * Living in Berlin (`Workspacelinks_livingInBerlin`)
    * InBerlin Wohnen (`Workspacelinks_inberlin`) - *Currently commented out in main execution*
* **Duplicate Prevention:** Stores links of found listings in `retrieved_links.txt` to avoid repeated notifications for the same apartment.
* **Desktop Notifications:** Uses the `mac_notifications` library to send a native macOS notification when new listings are detected.
* **Headless Mode:** Can be configured to run Chrome in headless mode (without a visible browser window), which is useful for running on servers or in the background.
* **(Experimental/Commented Out) Auto-Apply Functionality:** Includes a `fill_and_send` function designed to automatically fill application forms (currently **not** used or fully implemented).

## Prerequisites

1.  **Python 3:** Ensure you have Python 3 installed.
2.  **Google Chrome:** The script uses Chrome, so you need it installed.
3.  **ChromeDriver:** You need the ChromeDriver executable that matches your installed Chrome version.
    * Download it from the [official ChromeDriver website](https://chromedriver.chromium.org/downloads).
    * Make sure the script knows where to find it (see Configuration).
4.  **macOS:** Required for the desktop notification feature using `mac_notifications`.

## Installation

1.  **Clone the Repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-directory>
    ```
2.  **Set up a Virtual Environment (Recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  **Install Dependencies:**
    ```bash
    pip install selenium mac_notifications
    ```

## Configuration

Before running the script, you **must** configure a few things:

1.  **ChromeDriver Path:**
    * In the script, update the `chromedriver_path` variable to the correct location of your downloaded ChromeDriver executable:
        ```python
        chromedriver_path = "/path/to/your/chromedriver"
        ```
    * Alternatively, ensure the ChromeDriver executable is in your system's PATH. If it is, you can potentially remove the `executable_path` argument when initializing `webdriver.Chrome`.

2.  **File Paths:**
    * The script currently uses an absolute path for `retrieved_links.txt`:
        ```python
        apartment_links_file = open('/Users/sunil.vaggannavar/project-appartment/retrieved_links.txt', 'r+')
        # ... and similar paths inside the functions
        ```
    * **Change these paths** to a suitable location on your system. Using relative paths might be more portable:
        ```python
        # Example using a relative path (assuming the file is in the same directory as the script)
        import os
        script_dir = os.path.dirname(__file__) # Gets the directory where the script is located
        links_file_path = os.path.join(script_dir, 'retrieved_links.txt')
        apartment_links_file = open(links_file_path, 'r+')
        # Make similar changes inside the fetch functions
        ```
    * Ensure the `retrieved_links.txt` file exists (it can be empty initially) or modify the script to create it if it doesn't.

3.  **Headless Mode:**
    * To run Chrome without a visible window (e.g., on a server), ensure this line is **uncommented**:
        ```python
        chrome_options.add_argument("--headless")
        ```
    * To see the browser operate, **comment out** this line:
        ```python
        # chrome_options.add_argument("--headless")
        ```

4.  **Enabled Scrapers:**
    * In the main execution block at the bottom of the script, uncomment the `Workspacelinks_*` functions for the websites you want to check. Currently, only `Workspacelinks_heimstaden` and `Workspacelinks_livingInBerlin` are active.

5.  **(Optional) Search Criteria:**
    * The `target_url` variables within each `Workspacelinks_*` function contain specific search parameters (location, area, radius, price, etc.). You may want to adjust these URLs to match your desired apartment criteria.

## Usage

1.  **Ensure Configuration is Done:** Double-check the ChromeDriver path, file paths, and desired scrapers.
2.  **Activate Virtual Environment (if used):**
    ```bash
    source venv/bin/activate
    ```
3.  **Run the Script:**
    ```bash
    python your_script_name.py # Replace your_script_name.py with the actual filename
    ```
4.  **Check Output:**
    * The script will print some basic information to the console.
    * If new listings are found, it will update `retrieved_links.txt` and you should receive a macOS notification.

## Important Considerations

* **Website Changes:** Web scraping scripts are fragile. If the websites change their structure (HTML, CSS classes, IDs), the script may break and will need updating.
* **Ethical Use & Rate Limiting:** Avoid running the script too frequently. Excessive requests can overload the websites' servers and might get your IP address blocked. Consider adding `time.sleep()` delays between requests or function calls if running in a loop.
* **Error Handling:** The script has basic functionality but lacks robust error handling. It might crash if elements aren't found or if there are network issues.
* **Auto-Apply Feature (`fill_and_send`):**
    * This function is **experimental and currently disabled**.
    * It requires significant setup (populating `form_data` with your personal details).
    * The placeholder `for i in range(...)` loops should be removed or replaced with proper waits (`time.sleep` or Selenium explicit/implicit waits).
    * **WARNING:** Auto-filling forms may be against the Terms of Service of some websites. Use with extreme caution and at your own risk.

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests. Areas for improvement include:
* Adding error handling.
* Making file paths configurable via arguments or a config file.
* Refactoring for better code reuse.
* Adding support for other operating systems (alternative notification systems).
* Improving the reliability of selectors.
* Adding proper delays instead of placeholder loops.

## License

