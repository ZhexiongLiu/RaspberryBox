# RaspberryBox

This project builds an Raspberry Box that can print out a ramdom poem through a physical printer by hitting a button.

Please note users may need to install Python3 with the packages `rpi.gpio`, `pandas`, `glob2`, `tables`, and `pdfminer.six`.

# Run Code

Navigate to the current directory and run the following commands in the terminal.

If you need convert a `.pdf` to a `.txt` file, please run`python3 pdf2text.py` first. 

Otherwise, please run `python3 text2hdf.py` which converts the `.txt` files to a overall`.hdf` file.

If you need set up a new printer, please run`python3 printer.py`for testing.

For the Raspberry Pi, plesae ensure correctly connect the harwares and run `python3 button.py`.

# Useful Instruction

Here are useful instructions that may help you set up the hardwares: [Printer and CUPS](https://learn.adafruit.com/networked-thermal-printer-using-cups-and-raspberry-pi), [GPIO](https://www.raspberrypi.org/documentation/usage/gpio/).
