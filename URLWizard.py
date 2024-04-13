from tkinter import Tk, Button, Text, Scrollbar, Entry
from http.cookiejar import CookieJar
from urllib.request import build_opener, HTTPCookieProcessor
from urllib.parse import urljoin, urlparse, parse_qs
import datetime

def handle_cookies():
    cookie_jar = CookieJar()
    opener = build_opener(HTTPCookieProcessor(cookie_jar))
    opener.open(url_entry.get())  # Use the user-provided URL
    cookies = list(cookie_jar)
    output_text.insert('end', f"Number of cookies: {len(cookies)}\n")
    for cookie in cookies:
        output_text.insert('end', f"Name: {cookie.name}\n")
        output_text.insert('end', f"Value: {cookie.value}\n")
        output_text.insert('end', f"Domain: {cookie.domain}\n")
        output_text.insert('end', f"Expires: {datetime.datetime.fromtimestamp(cookie.expires)}\n\n")

def join_urls():
    base_url = url_entry.get()  # Use the user-provided base URL
    urls = [
        urljoin(base_url, "about"),
        urljoin(base_url, "files/docs/about"),
        urljoin(base_url, "files/docs/about"),
        urljoin(base_url, "/about"),
        urljoin(base_url, "../about"),
        urljoin(base_url, "http://www.gmail.com/")
    ]
    output_text.insert('end', "\n".join(urls) + "\n")

def parse_url():
    parse = urlparse(url_entry.get())  # Parse the user-provided URL
    output_text.insert('end', f"Netloc: {parse.netloc}\n")
    output_text.insert('end', f"Query: {parse.query}\n")
    output_text.insert('end', f"Parsed Query: {parse_qs(parse.query)}\n")

# GUI setup
root = Tk()
root.title("Web Utilities")

url_entry = Entry(root)
url_entry.grid(row=0, column=0, columnspan=3, sticky='ew')
url_entry.insert(0, "http://www.example.com")  # Default URL

output_text = Text(root, wrap='word')
output_text.grid(row=1, column=0, columnspan=2, sticky='nsew')

scrollbar = Scrollbar(root, command=output_text.yview)
scrollbar.grid(row=1, column=2, sticky='nsew')
output_text['yscrollcommand'] = scrollbar.set

cookie_button = Button(root, text="Handle Cookies", command=handle_cookies)
cookie_button.grid(row=2, column=0, sticky='ew')

url_button = Button(root, text="Join URLs", command=join_urls)
url_button.grid(row=2, column=1, sticky='ew')

parse_button = Button(root, text="Parse URL", command=parse_url)
parse_button.grid(row=2, column=2, sticky='ew')

root.mainloop()
