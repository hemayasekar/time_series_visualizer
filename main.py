# # This entrypoint file to be used in development. Start by reading README.md
# import time_series_visualizer
# from unittest import main

# # Test your function by calling it here
# time_series_visualizer.draw_line_plot()
# time_series_visualizer.draw_bar_plot()
# time_series_visualizer.draw_box_plot()


# # Run unit tests automatically
# main(module='test_module', exit=False)
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

# Call each function to view the plots
draw_line_plot()
draw_bar_plot()
draw_box_plot()

