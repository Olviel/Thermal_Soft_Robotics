import matplotlib.pyplot as plt
from datetime import datetime
import os

def save_plot(name):
    # Get the current time
    now = datetime.now()

    # Format the time as a string
    time_string = now.strftime("%Y%m%d_%H%M%S")

    # Specify the path to the 'figures' folder within the current directory
    folder_path = 'figures/'

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Create the filename with the folder path, time string, and given name
    filename = os.path.join(folder_path, f'{time_string}_{name}.svg')

    # Save the plot with the generated filename
    plt.savefig(filename)

    # Show the plot (optional)
    plt.show()