import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from founded_year_text import get_founded_text
import pandas
from collections import defaultdict


def main():
    parser = argparse.ArgumentParser(description='Запустить сайт винодельни.')
    parser.add_argument('--excel-path', default='wines_catalog.xlsx', help='Путь к Excel-файлу с данными о вине')
    args = parser.parse_args()

    excel_wines = pandas.read_excel(args.excel_path, sheet_name='Лист1')
    excel_wines = excel_wines.where(pandas.notna(excel_wines), None)
    wines = excel_wines.to_dict(orient='records')

    grouped_wines = defaultdict(list)
    for wine in wines:
        grouped_wines[wine["Категория"]].append(wine)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        founded_text=get_founded_text(),
        grouped_wines=grouped_wines
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()