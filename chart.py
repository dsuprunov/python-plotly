import plotly.graph_objects as go


fig = go.Figure(data=go.Bar(
    x=[1, 2, 3, 4, 5],
    y=[10, 6, 8, 12, 4],
))
fig.show()
