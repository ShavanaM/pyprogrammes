import requests
from bs4 import BeautifulSoup

def print_secret_message(doc_url):
    print("Fetching data from:", doc_url)
    response = requests.get(doc_url)
    response.raise_for_status()

    # Use BeautifulSoup to parse the HTML content.
    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate the first table in the document.
    table = soup.find('table')
    if not table:
        print("No table found in the document.")
        return

    # Extract all rows from the table.
    rows = table.find_all('tr')
    data_rows = []
    for row in rows:
        # Retrieve all cells (both <td> and <th>).
        cells = row.find_all(['td', 'th'])
        # Extract clean text from each cell.
        cell_text = [cell.get_text(strip=True) for cell in cells]
        data_rows.append(cell_text)

    # Debug: Print out the extracted table rows.
    print("Extracted table rows:")
    for row in data_rows:
        print(row)

    if not data_rows or len(data_rows[0]) < 3:
        print("Not enough data found in table rows.")
        return

    # Assume the header row gives the order.
    # For example: ["x-coordinate", "Character", "y-coordinate"]
    header = data_rows[0]

    try:
        x_index = header.index("x-coordinate")
        char_index = header.index("Character")
        y_index = header.index("y-coordinate")
    except ValueError:
        print("Could not find expected header columns. Header found:", header)
        return

    # Process every row after the header row.
    points = []
    max_x = 0
    max_y = 0
    for row in data_rows[1:]:
        if len(row) < 3:
            continue
        try:
            x = int(row[x_index])
            char = row[char_index]
            y = int(row[y_index])
        except ValueError:
            # Skip rows with conversion issues.
            continue
        points.append((x, y, char))
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    # Build a grid filled with spaces.
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Place each character at the specified coordinate.
    for x, y, char in points:
        grid[y][x] = char

    # Print the decoded message grid.
    print("\nDecoded Message:\n")
    for row in grid:
        print(''.join(row))


if __name__ == "__main__":
    # Replace with your actual published Google Doc URL.
    doc_url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
    print_secret_message(doc_url)
