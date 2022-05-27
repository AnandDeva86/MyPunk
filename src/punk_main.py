import click
import logging
from datetime import datetime

from punk_API import PunkAPI
from file_writer import FileWriter

# -----------------------------------------------------------
# File name: punk_main.py
# Author: Anand Devarajan
# Date created: 1/04/2022
# Date last modified: 3/04/2022
# Python Version: >3.6
# -----------------------------------------------------------

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


@click.group()
@click.pass_context
def main(ctx):
    """ beers
    brewed-from <month-year>
    brewed-until <month-year>
    --output-format <csv>
    --output-path </file_path/file_name.csv>
    """

    if ctx.obj is None:
        ctx.obj = {}
    api_response = PunkAPI()
    json_data = api_response.get_data()
    ctx.obj['data'] = json_data.json()


@click.group(chain=True)
@click.pass_context
def beers(ctx):
    parse_json = ctx.obj['data']
    for i in range(len(parse_json)):
        parse_json[i]['first_brewed'] = datetime.strptime(parse_json[i]['first_brewed'], "%m/%Y")
    ctx.obj['data'] = parse_json


@beers.command('brewed-from')
@click.argument('date_from')
@click.pass_context
def brewed_from(ctx, date_from: str):
    try:
        datetime_object = datetime.strptime(date_from, '%m-%Y')
        parse_json = ctx.obj['data']

        def condition(dic):
            """ filter based on the date given"""
            return dic['first_brewed'] >= datetime_object

        filtered_json = [d for d in parse_json if condition(d)]
        ctx.obj['data'] = filtered_json
    except:
        logging.error("date-until data format not supported")


@beers.command('brewed-until')
@click.argument('date_until')
@click.pass_context
def brewed_until(ctx, date_until: str):
    try:
        datetime_object = datetime.strptime(date_until, '%m-%Y')
        parse_json = ctx.obj['data']

        def condition(dic):
            """ filter based on the date given"""
            return dic['first_brewed'] <= datetime_object

        filtered_json = [d for d in parse_json if condition(d)]
        ctx.obj['data'] = filtered_json
    except:
        logging.error("date-until data format not supported")


@beers.command('--output-format')
@click.argument('output_format')
@click.pass_context
def save_format(ctx, output_format: str):
    ctx.obj['output_format'] = output_format


@beers.command('--output-path')
@click.argument('file_name')
@click.pass_context
def save_file(ctx, file_name: str):
    if ctx.obj is not None:
        parse_json = ctx.obj['data']
        output_format = ctx.obj['output_format']

        write_file = FileWriter()
        write_file.write_csv(parse_json, output_format, file_name)


main.add_command(beers)

if __name__ == '__main__':
    main()
