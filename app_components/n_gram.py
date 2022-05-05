import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State


layout = [

    dbc.Row(
        html.H2(
            children = 'n-Gram Model',
            id = 'n-gram-title',
            style = {'font-family': 'Secular One'}
        ),
    ),

    html.Br(),

    dcc.Slider(
        min=2,
        max=10,
        step=1,
        value=3,
        id='n-gram-slider',
        disabled=False,
        dots=True,
        marks={ i: {'label': str(i)} for i in range(2, 11) },
    ),

    html.Br(),

    dbc.Textarea(
        id = 'n-gram-text-area',
        placeholder = 'Type something...',
    ),

    html.Br(),

    dbc.Card(
        dbc.CardBody(
            [ 
                html.P(
                    [
                        html.I(className='fa fa-code'),
                        html.Strong('   Console')
                    ]
                ),
                html.P('>>> Previous words: ', id='console-previous-words'),
                html.P('>>> First characters: ', id='console-first-characters'),
                html.P('>>> Suggestions: ', id='console-predictions')
            ]
        ),
        style = {'font-family': 'consolas', 'background-color': '#f2f2f2'} 
    )
]