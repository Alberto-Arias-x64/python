from bokeh.plotting import Figure, output_file, show

output_file('grafica.html')
fig=Figure()

total_vals = int(input("cuantos valores putto?"))
x_vals = list(range(total_vals))
y_vals = []

for x in x_vals:
    val=int(input(f"valor Y para {x} "))
    y_vals.append(val)

fig.line(x_vals, y_vals)
show(fig)