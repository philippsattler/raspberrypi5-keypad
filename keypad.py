from gpiozero import LED, Button
from time import sleep

keypad_rows = [14, 15, 18, 23]
keypad_columns = [24, 25, 8, 7]

row_leds = [LED(pin) for pin in keypad_rows]
col_buttons = [Button(pin) for pin in keypad_columns]
matrix_keys = [['1', '2', '3', 'A'],
		['4', '5', '6', 'B'],
		['7', '8', '9', 'C'],
		['*', '0', '#', 'D']]

not_pressed_keys = set([])

row1 = set([0, 1, 2, 3])

print("Please press a button")

def scankeys():  
	for row, row_led in enumerate(row_leds):
		row_leds[row].on()
		for col, col_button in enumerate(col_buttons):
			if col_button.is_pressed:
				not_pressed_keys.add(row)
				if(len(not_pressed_keys) == 3):
					pressed_row = set(row1) - set(not_pressed_keys)
					print('Pressed: ', matrix_keys[sum(pressed_row)][col])
					pressed_row.clear()
					not_pressed_keys.clear()
					sleep(0.5)
		row_leds[row].off()

try:
	while True:
		scankeys()
except KeyboardInterrupt:
	pass
