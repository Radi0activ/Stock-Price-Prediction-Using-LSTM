""" Importing plotly module for interactive visualisation of the Closing Prices of Stock Shares. """

import plotly.graph_objects as go


def plot_basic(stocks, title):
    
    """
    Plots basic plotly plot.
    
    :param stocks: DataFrame having all the necessary data.
    :param title: Title of the plot.
    """
    
    trace1 = go.Scatter(
        x = stocks.index,
        y = stocks.Close,
        mode = "lines",
        name = "Data",
        )
    layout = go.Layout(
        title = title,
        xaxis = {"title": "Date"},
        yaxis = {"title": "Close"},
        )
    fig = go.Figure(data = [trace1], layout = layout)
    fig.show()
    
    
def plot_epochs_loss(epochs, loss_train):
    
    """
    Prints a plotly plot for the Epochs vs Loss.
    
    :param epochs: List of the number of epochs.
    :param loss_train: List of the respective training loss.
    """
        
    trace1 = go.Scatter(
        x = epochs,
        y = loss_train,
        mode = "lines",
        name = "Data",
        )
    layout = go.Layout(
        title = "Epochs vs Training Loss",
        xaxis = {"title": "Epochs"},
        yaxis = {"title": "Training Loss"},
        )
    fig = go.Figure(data = [trace1], layout = layout)
    fig.show()
    
def plot_lstm_prediction(close_train, date_train, close_test, date_test, prediction, title):
    
    """
    Prints a plotly plot for train, test and prediction against date.
        
    :param close_train: numpy array of training dataset.
    :param date_train: pandas Series that contains the respective dates for data points in close_train.
    :param close_test: numpy array of testing dataset.
    :param date_test: pandas Series that contains the respective dates for data points in close_test.
    :param prediction: numpy array of predicted values by the model.
    :param title: Title of the plot.
    """
    
    trace1 = go.Scatter(
        x = date_train,
        y = close_train,
        mode = "lines",
        name = "Data",
        )
    trace2 = go.Scatter(
        x = date_test,
        y = prediction,
        mode = "lines",
        name = "Prediction",
        )
    trace3 = go.Scatter(
        x = date_test,
        y = close_test,
        mode ="lines",
        name = "Ground Truth",
        )
    layout = go.Layout(
        title = title,
        xaxis = {"title": "Date"},
        yaxis = {"title": "Close"},
        )
    fig = go.Figure(data = [trace1, trace2, trace3], layout = layout)
    fig.show()
    
    

def plot_lstm_forecasting(close_train, date_train, close_test, date_test, prediction, forecast_dates, forecast, title):
    
    """
    Prints a plotly plot for train, test, prediction and forecasting  against date.
        
    :param close_train: numpy array of training dataset.
    :param date_train: pandas Series that contains the respective dates for data points in close_train.
    :param close_test: numpy array of testing dataset.
    :param date_test: pandas Series that contains the respective dates for data points in close_test.
    :param prediction: numpy array of predicted values by the model.
    :param forecast: numpy array of forecasted prices by the model.
    :param forecast_dates: list of the respective future dates for data points in forecast.   
    :param title: Title of the plot.
    """
    
    trace1 = go.Scatter(
        x = date_train,
        y = close_train,
        mode = "lines",
        name = "Data",
        )
    trace2 = go.Scatter(
        x = date_test,
        y = prediction,
        mode = "lines",
        name = "Prediction",
        )
    trace3 = go.Scatter(
        x = date_test,
        y = close_test,
        mode = "lines",
        name = "Ground Truth",
        )
    trace4 = go.Scatter(
        x = forecast_dates,
        y = forecast,
        mode ="lines",
        name = "Future",
        )
    layout = go.Layout(
        title = title,
        xaxis = {"title": "Date"},
        yaxis = {"title": "Close"},
        )
    fig = go.Figure(data = [trace1, trace2, trace3, trace4], layout = layout)
    fig.show()