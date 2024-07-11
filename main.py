from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <div class="content">
            <p>This is our first content</p>
        </div>
        <div class="other">
            <p>This is is another piece of content</p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html, features="html.parser")
all_divs = soup.find_all("div")
for div in all_divs:
  print(div.text)
