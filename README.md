# URLWizard
This Python script provides a graphical user interface (GUI) for performing various web-related tasks such as handling cookies, joining URLs, and parsing URLs. It utilizes the tkinter library for the GUI components and standard Python libraries for web-related functionality.


# Features
Handle Cookies
This feature allows you to retrieve and display cookies from a specified URL. It uses the http.cookiejar and urllib.request modules to handle HTTP cookies.

Join URLs
This feature enables you to join multiple URLs to a base URL and display the resulting URLs. It utilizes the urllib.parse.urljoin function to join the URLs.

Parse URL
This feature parses a provided URL and displays its components such as the network location (netloc), query string, and parsed query parameters. It uses the urllib.parse.urlparse function for URL parsing.

# Usage
Enter a URL in the text entry field.
Click the corresponding button to perform the desired action.
The output will be displayed in the text area below.
Dependencies
tkinter: Standard GUI library for Python.
http.cookiejar: Library for handling HTTP cookies.
urllib.request: Library for opening URLs.
urllib.parse: Library for parsing URLs.

