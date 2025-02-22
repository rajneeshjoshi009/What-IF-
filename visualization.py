import plotly.graph_objects as go
import pandas as pd

def create_simulation_plot(simulation_results):
    """
    Create an interactive plot showing simulation results
    
    Parameters:
    -----------
    simulation_results : dict
        Dictionary containing simulation results
    """
    fig = go.Figure()
    
    # Add mean line
    fig.add_trace(
        go.Scatter(
            x=simulation_results['years'],
            y=simulation_results['mean_values'],
            name='Expected Growth',
            line=dict(color='rgb(31, 119, 180)', width=2)
        )
    )
    
    # Add confidence interval
    fig.add_trace(
        go.Scatter(
            x=simulation_results['years'] + simulation_results['years'][::-1],
            y=list(simulation_results['percentile_75']) + 
               list(simulation_results['percentile_25'])[::-1],
            fill='toself',
            fillcolor='rgba(31, 119, 180, 0.2)',
            line=dict(color='rgba(255,255,255,0)'),
            name='Confidence Interval'
        )
    )
    
    # Add best and worst cases
    fig.add_trace(
        go.Scatter(
            x=simulation_results['years'],
            y=simulation_results['best_case'],
            name='Best Case',
            line=dict(color='rgba(0, 255, 0, 0.5)', dash='dash')
        )
    )
    
    fig.add_trace(
        go.Scatter(
            x=simulation_results['years'],
            y=simulation_results['worst_case'],
            name='Worst Case',
            line=dict(color='rgba(255, 0, 0, 0.5)', dash='dash')
        )
    )
    
    fig.update_layout(
        title='Investment Growth Simulation',
        xaxis_title='Years',
        yaxis_title='Investment Value ($)',
        hovermode='x unified',
        plot_bgcolor='white',
        paper_bgcolor='white',
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        )
    )
    
    return fig
