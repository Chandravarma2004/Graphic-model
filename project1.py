import tkinter as tk

# Sample data for the scatter plot
data_points = [(10, 30), (20, 50), (30, 40), (40, 10), (50, 20)]

# Create the Tkinter window
root = tk.Tk()
root.title("Scatter Plot using Tkinter")

# Set the size of the canvas
canvas_width = 400
canvas_height = 400
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Function to draw the scatter plot
def draw_scatter_plot(points):
    for x, y in points:
        # Scale the data points to fit inside the canvas
        scaled_x = x * (canvas_width / 100)
        scaled_y = canvas_height - (y * (canvas_height / 100))
        # Draw a point on the canvas
        canvas.create_oval(scaled_x - 5, scaled_y - 5, scaled_x + 5, scaled_y + 5, fill="blue")

# Call the function to draw the scatter plot with the sample data
draw_scatter_plot(data_points)

# Run the Tkinter main loop
root.mainloop()
