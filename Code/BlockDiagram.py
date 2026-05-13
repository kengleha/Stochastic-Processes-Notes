import graphviz

# Create a Digraph object
dot = graphviz.Digraph(comment='Kalman Filter Flowchart')

# Define nodes and edges
dot.node('Start', 'Start', shape='ellipse')
dot.node('Predict', 'Predict', shape='box')
dot.node('Update', 'Update', shape='box')
dot.node('End', 'End', shape='ellipse')

dot.edge('Start', 'Predict', label='Initialize\nPredicted State Estimate\nPredicted Estimate Covariance')
dot.edge('Predict', 'Update', label='Predicted Measurement\nInnovation\nInnovation Covariance\nOptimal Kalman Gain')
dot.edge('Update', 'Predict', label='Updated State Estimate\nUpdated Estimate Covariance\nMeasurement Post-fit Residual')
dot.edge('Update', 'End', label='A posteriori\nState Estimate')

# Render the flowchart to a PDF file
dot.render('kalman_filter_flowchart', view=True)
