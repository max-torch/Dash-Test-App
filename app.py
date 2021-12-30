from time import time
import json
from urllib.parse import urlparse
import datetime

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import requests
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Global Variables
RESOURCE = 'orders'
FIELDS = [
    'id', 'app_id', 'buyer_accepts_marketing', 'cancel_reason', 'cancelled_at',
    'client_details', 'closed_at', 'contact_email', 'created_at',
    'current_subtotal_price', 'current_total_discounts', 'current_total_price',
    'customer', 'discount_codes', 'email', 'financial_status',
    'fulfillment_status', 'gateway', 'landing_site', 'name', 'order_number',
    'payment_gateway_names', 'phone', 'processed_at', 'processing_method',
    'referring_site', 'source_name', 'subtotal_price', 'total_discounts',
    'total_line_items_price', 'total_outstanding', 'total_price', 'updated_at',
    'billing_address', 'discount_applications', 'line_items', 'refunds',
    'shipping_address'
]
fake = True

# DataFrame that contains Philippines zipcodes mapped to their area and province/city
zipcodes = (
    pd.read_csv("zipcodes.csv")
    .rename(columns={"ZIP Code": "ZIP_Code"})
    .assign(ZIP_Code=lambda x: x.ZIP_Code.astype("object"))
)

# Dictionary from zipcodes DataFrame for Pandas Series.map() method.
zipcodesdict = pd.Series(zipcodes["Province or city"].values, index=zipcodes["ZIP_Code"]).to_dict()

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


###########################

server = app.server

def prepare_layout():
    layout = html.Div([
        html.H2('Hello World'),
        dcc.Dropdown(
            id='dropdown',
            options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
            value='LA'
        ),
        html.Div(id='display-value')
    ])
    return layout

app.layout = prepare_layout

@app.callback(dash.dependencies.Output('display-value', 'children'),
                [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)