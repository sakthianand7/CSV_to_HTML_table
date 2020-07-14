
import csv
def convert_csv_to_html(data):
  html_content = """
  <html>
  <head>
  <style>
  table {
    width: 25%;
    font-family: "Times New Roman", Times, serif;
    border-collapse: collapse;
  }

  tr:nth-child(odd) {
    background-color: #dddddd;
  }

  td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 6px;
  }
  </style>
  </head>
  <body>
  """
  title="CSV TO HTML TABLE"
  html_content += "<h2>{}</h2><table>".format(title)
  for i, row in enumerate(data):
    html_content += "<tr>"
    for column in row:
        if i == 0:
            html_content += "<th>{}</th>".format(column)
        else:
            html_content += "<td>{}</td>".format(column)
    html_content += "</tr>"

  html_content += """</tr></table></body></html>"""
  return html_content

def main():
  with open('housing_prices.csv',"r") as datafile:
    data = list(csv.reader(datafile))
  html_content=convert_csv_to_html(data)
  with open('housing_prices.html','w') as htmlfile:
    htmlfile.write(html_content)
main()
