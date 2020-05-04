import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.font as font
try:
	from ctypes import windll
	windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

#Defining Constants
# For length, base unit = meters
len_base = (1, 0.001, 100, 1000, 1000000, 1000000000, 0.0006213689, 1.0936132983, 3.280839895, 39.37007874)
area_base = (1, 0.000001, 10000, 1000000, 1000000000000, 0.0001, 0.000003861018768, 1.1959900463, 10.763910417, 1550.0031, 0.0002471054)
vol_base = (0.001, 0.000000000001, 1, 1000, 0.0000000000002399128636, 0.0013079506,0.0353146667)
wght_base = (1, 1000, 1000000, 0.001, 2.2046244202, 35.273990723, 5000)


#Random Facts
wght_fact = "Weight is the force of gravity \npulling on an object, items weigh \nmuch less on the moon than \nthey do on Earth."
len_fact = "The metric system of measuring\nlength was first adopted in France\nand is currently used by around \n95% of the world population."
vol_fact = "100 cm³ = Volume of a T-Rex brain,\n600 cm³ = Volume of a human brain"
area_fact = "Total area: 510.072 million sq km.\nLand area: 148.94 million sq km.\nWater area: 361.132 million sq km"
temp_fact = "A very notable fact is that\nFahrenheit and Celsius are\nequal at -40 degrees."


#All the variables
CONVERSION_OPTIONS = ("Length", "Temprature", "Area", "Volume", "Weight")
TEMPERATURE_OPTIONS = ("Celsius", "Kelvin", "Fahrenheit")
TEMPERATURE_UNITS = ("°C","K","°F")
LENGTH_OPTIONS = ("Meter", "Kilometer", "Centimeter", "Millimeter", "Micrometer", "Nanometer", "Mile", "Yard", "Foot", "Inch")
LENGTH_UNITS = ("m","km","cm","mm","µm","nm","mi","yd","ft","in")
AREA_OPTIONS = ("Sq. meters", "Sq. Kilometer", "Sq. Centimeter", "Sq. Millimeter", "Sq. Micrometer", "Hectare", "Sq. Mile", "Sq. Yard", "Sq. Foot", "Sq. Inch", "Acre")
AREA_UNITS  = ("m²", "km²", "cm²", "mm²", "µm²", "ha", "mi²", "yd²", "ft²", "in²", "A")
VOLUME_OPTIONS = ("Cubic Meter", "Cubic Kilometer", "Liter", "Milliliter", "Cubic Mile", "Cubic Yard", "Cubic Foot")
VOLUME_UNITS = ("m³","km³","L","mL","mi³","yard³","ft³")
WEIGHT_OPTIONS = ("Kilogram", "Gram", "Milligram", "Metric Ton", "Pound", "Ounce", "Carat")
WEIGHT_UNITS = ("kg","g","mg","mT","lbs","oz", "ct")
ipopt = None
opopt = None
basevalue = 0
basetuple = None


root = tk.Tk()
root.title("Conversion Calculator")
root.geometry("1000x600")
root.maxsize(1000, 600)

#Setting the font size (apart from text box)
font.nametofont("TkDefaultFont").configure(size=10)

#Defining all the tkinter variables
conversion_options_selected = tk.StringVar()
convert_from_list = tk.StringVar(value=None)
convert_to_list = tk.StringVar(value=None)
convert_from = tk.StringVar()
convert_to = tk.StringVar()
input_value = tk.StringVar()
output_value = tk.StringVar(value="Output shown here")
input_unit = tk.StringVar(value="Value")
output_unit = tk.StringVar(value="Value")
quote = tk.StringVar(value="Some Random Fact Here!")
converting_units_list = TEMPERATURE_UNITS


#All Functions




def selecting_conversion_option(event):
	optsel = conversion_options_selected.get()
	global converting_units_list
	global basetuple
	print(optsel)

	if(optsel == "Length"):
		# Showing values in the listboxes (Both from conversion and to conversion)
		convert_from_options.delete(0, "end")
		convert_from_options.insert("end",*LENGTH_OPTIONS)
		convert_to_options.delete(0, "end")
		convert_to_options.insert("end",*LENGTH_OPTIONS)
		# Changing Icon
		image = Image.open("len.png")
		photo = ImageTk.PhotoImage(image)
		img_label.configure(image=photo)
		img_label.image = photo
		# Converting Units List and Base value list
		converting_units_list = LENGTH_UNITS
		basetuple = len_base
		#Setting quote value
		quote.set(len_fact)

	elif(optsel == "Temprature"):
		# Showing values in the listboxes (Both from conversion and to conversion)
		convert_from_options.delete(0, "end")
		convert_from_options.insert("end",*TEMPERATURE_OPTIONS)
		convert_to_options.delete(0, "end")
		convert_to_options.insert("end",*TEMPERATURE_OPTIONS)
		# Changing Icon
		image = Image.open("temp.png")
		photo = ImageTk.PhotoImage(image)
		img_label.configure(image=photo)
		img_label.image = photo
		# Converting Units List
		converting_units_list = TEMPERATURE_UNITS
		basetuple = len_base
		#Setting quote value
		quote.set(temp_fact)

	elif(optsel == "Area"):
		# Showing values in the listboxes (Both from conversion and to conversion)
		convert_from_options.delete(0, "end")
		convert_from_options.insert("end",*AREA_OPTIONS)
		convert_to_options.delete(0, "end")
		convert_to_options.insert("end",*AREA_OPTIONS)
		# Changing Icon
		image = Image.open("area.png")
		photo = ImageTk.PhotoImage(image)
		img_label.configure(image=photo)
		img_label.image = photo
		# Converting Units List
		converting_units_list = AREA_UNITS
		basetuple = area_base
		#Setting quote value
		quote.set(area_fact)

	elif(optsel == "Volume"):
		# Showing values in the listboxes (Both from conversion and to conversion)
		convert_from_options.delete(0, "end")
		convert_from_options.insert("end",*VOLUME_OPTIONS)
		convert_to_options.delete(0, "end")
		convert_to_options.insert("end",*VOLUME_OPTIONS)
		#Changing Icon
		image = Image.open("vol.png")
		photo = ImageTk.PhotoImage(image)
		img_label.configure(image=photo)
		img_label.image = photo
		#Converting Units List
		converting_units_list = VOLUME_UNITS
		basetuple = vol_base
		#Setting quote value
		quote.set(vol_fact)

	elif(optsel == "Weight"):
		# Showing values in the listboxes (Both from conversion and to conversion)
		convert_from_options.delete(0, "end")
		convert_from_options.insert("end",*WEIGHT_OPTIONS)
		convert_to_options.delete(0, "end")
		convert_to_options.insert("end",*WEIGHT_OPTIONS)
		# Changing Icon
		image = Image.open("wght.png")
		photo = ImageTk.PhotoImage(image)
		img_label.configure(image=photo)
		img_label.image = photo
		# Converting Units List
		converting_units_list = WEIGHT_UNITS
		basetuple = wght_base
		#Setting quote value
		quote.set(wght_fact)


def calculate_output(*args):
	try:
		if(conversion_options_selected.get()!="Temprature"):
			ipval = None
			opval = None
			ipval = float(input_value.get())
			basevalue = basetuple[ipopt[0]]
			opval = ipval*((basetuple[opopt[0]])/(basevalue))
			print(f"{ipval} {converting_units_list[convert_from_options.curselection()[0]]} is equal to {opval:.9f} {converting_units_list[convert_to_options.curselection()[0]]}")
			output_value.set(f"{opval:.10f}")
		else:
			ipval = float(input_value.get())
			if(ipopt[0]==0):
				if(opopt[0]==0):
					opval = ipval
					print(f"{ipval} {converting_units_list[convert_from_options.curselection()[0]]} is equal to {opval:.9f} {converting_units_list[convert_to_options.curselection()[0]]}")
					output_value.set(f"{opval:.10f}")
				elif(opopt[0]==1):
					opval = ipval + 273.15 
					print(f"{ipval} {converting_units_list[convert_from_options.curselection()[0]]} is equal to {opval:.9f} {converting_units_list[convert_to_options.curselection()[0]]}")
					output_value.set(f"{opval:.10f}")
				elif(opopt[0]==2):
					opval = (ipval*1.8) + 32 
					print(f"{ipval} {converting_units_list[convert_from_options.curselection()[0]]} is equal to {opval:.9f} {converting_units_list[convert_to_options.curselection()[0]]}")
					output_value.set(f"{opval:.10f}")
			elif(ipopt[0]==1):
				if(opopt[0]==0):
					opval = ipval - 273.15 
					print(f"{ipval} {converting_units_list[convert_from_options.curselection()[0]]} is equal to {opval:.9f} {converting_units_list[convert_to_options.curselection()[0]]}")
					output_value.set(f"{opval:.10f}")
				elif(opopt[0]==1):
					opval = ipval
					print(f"{ipval} {converting_units_list[convert_from_options.curselection()[0]]} is equal to {opval:.9f} {converting_units_list[convert_to_options.curselection()[0]]}")
					output_value.set(f"{opval:.10f}")
				elif(opopt[0]==2):
					opval = (ipval-273.15)*(9/5)+32
					print(f"{ipval} {converting_units_list[convert_from_options.curselection()[0]]} is equal to {opval:.9f} {converting_units_list[convert_to_options.curselection()[0]]}")
					output_value.set(f"{opval:.10f}")
			elif(ipopt[0]==2):
				if(opopt[0]==0):
					opval = (ipval-32)*(5/9) 
					print(f"{ipval} {converting_units_list[convert_from_options.curselection()[0]]} is equal to {opval:.9f} {converting_units_list[convert_to_options.curselection()[0]]}")
					output_value.set(f"{opval:.10f}")
				elif(opopt[0]==1):
					opval = (ipval-32)*(5/9)+273.15
					print(f"{ipval} {converting_units_list[convert_from_options.curselection()[0]]} is equal to {opval:.9f} {converting_units_list[convert_to_options.curselection()[0]]}")
					output_value.set(f"{opval:.10f}")
				elif(opopt[0]==2):
					opval = ipval
					print(f"{ipval} {converting_units_list[convert_from_options.curselection()[0]]} is equal to {opval:.9f} {converting_units_list[convert_to_options.curselection()[0]]}")
					output_value.set(f"{opval:.10f}")
	except ValueError:
		pass


def converting_from(event):
	global ipopt
	ipopt = convert_from_options.curselection()
	input_unit.set(converting_units_list[convert_from_options.curselection()[0]])
	for i in range(len(ipopt)):
		print(convert_from_options.get(ipopt[i]))
		

def converting_to(event):
	global opopt
	opopt = convert_to_options.curselection()
	output_unit.set(converting_units_list[convert_to_options.curselection()[0]])
	for i in range(len(opopt)):
		print(convert_to_options.get(opopt[i]))
		


root.columnconfigure(0, weight=1)

main = ttk.Frame(root, padding=(30,15))
main.grid()



# All the elements of the widget declared

title_label =  ttk.Label(main, text="Conversion Calculator", font=("Segoe UI", 20))

conversion_options = ttk.Combobox(main, textvariable = conversion_options_selected, font=("Segoe UI", 15))
conversion_options["values"] = CONVERSION_OPTIONS
conversion_options["state"] = "readonly"

quote_label =  ttk.Label(main, textvariable=quote, text="Some Random Fact Here!", font=("Segoe UI", 9, "normal", "italic"))

convert_from_options = tk.Listbox(main, listvariable=convert_from_list, height=6, exportselection=False)

image = Image.open("convert.png")
photo = ImageTk.PhotoImage(image)
img_label = ttk.Label(main, image=photo)

convert_to_options = tk.Listbox(main, listvariable=convert_to_list, height=6, exportselection=False)

from_label =  ttk.Label(main,textvariable=input_unit, text="Value")
value_input = ttk.Entry(main, width=30, textvariable=input_value, font=("Segoe UI", 10))

to_label =  ttk.Label(main,textvariable=output_unit, text="Value")
output_display = ttk.Label(main, text="Output shown here", textvariable=output_value, font=("Segoe UI",11,"bold"))

calc_button = ttk.Button(main, text="Calculate", command=calculate_output)

made_by = ttk.Label(main, text="Made with ♥️ by Anmol Tripathi, 2020", font=("Segoe UI", 7))


#Elements location

title_label.grid(column=1,row=0, sticky="W")

conversion_options.grid(column=0, row=1, sticky="W")

quote_label.grid(column=2,row=1, sticky="W")

convert_from_options.grid(column=0,row=2, sticky="W")

img_label.grid(column=1,row=2, sticky="W")

convert_to_options.grid(column=2,row=2, sticky="W")


value_input.grid(column=0, row=3, sticky="W")
from_label.grid(column=0, row=4, sticky="W")
value_input.focus()

output_display.grid(column=2, row=3, sticky="W")
to_label.grid(column=2, row=4, sticky="W")

calc_button.grid(column=1, row=5, columnspan=2, sticky="W")

made_by.grid(column=0, row=6, columnspan=2, sticky="W")



for child in main.winfo_children(): #All the children of the widget
	child.grid_configure(padx=5, pady=10)

#Key Bindings
value_input.bind("<Return>", calculate_output) #For Enter key on keyboard
value_input.bind("<KP_Enter>", calculate_output) #For Keypad Enter
conversion_options.bind("<<ComboboxSelected>>", selecting_conversion_option)
conversion_options.bind("<<ComboboxSelected>>", selecting_conversion_option)
convert_from_options.bind("<<ComboboxSelected>>", selecting_conversion_option)
convert_from_options.bind("<<ListboxSelect>>", converting_from)
convert_to_options.bind("<<ListboxSelect>>", converting_to)


root.mainloop()