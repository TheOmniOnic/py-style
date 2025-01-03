# Py-Style

`Py-Style` is a Python package designed for terminal formatting. It offers a variety of utilities to enhance the terminal experience, including color formatting, progress bars, and additional tools like `tables`, `rgb_to_ansi`, and `hex_to_ansi`. This package makes it easy to add colors, effects, and progress indicators to your terminal output.

## Features

- **Console Support**: Easily format terminal outputs with various effects such as bold, italic, underlined, and more.
- **Tables**: Tabulate information into beautiful tables.
- **Progress Bars**: Track the progress of long-running operations with customizable progress bars.
- **24-bit Color Support**: Use rich, vibrant colors. If your terminal does not support 24-bit colors, Py-Style will warn you.

## Installation

To install `Py-Style`, simply run:

```bash
pip install py-style
```

## Usage

### Console Formatting

You can format text using various styles. For example:

```python
from py_style import Console

console = Console("MyConsole")
console.print("This is bold text", style="bold")
console.print("This is underlined text", style="underline")
console.print("This is red text", style="fg(red)")
```

### RGB to ANSI Conversion

Use the `rgb_to_ansi` function to convert RGB color values into ANSI codes.

```python
from py_style import rgb_to_ansi

ansi_code = rgb_to_ansi(255, 0, 0)  # Red color
console.print(f"Your RGB to ANSI code: {ansi_code}")
```

### Hexadecimal to ANSI Conversion

Convert hexadecimal color codes to ANSI codes.

```python
from py_style import hex_to_ansi

ansi_code = hex_to_ansi("#FF5733")  # Hex color code
console.print(f"Your Hex to ANSI code: {ansi_code}")
```

### Tables

Create stories or formatted outputs with dynamic content.

```python
from py_style import Table

table = Table(2)
table.add_row("Name", "Age")
table.add_row("John Doe", 28)
table.add_row("Jane Smith", 34)

print(table.get_table())
```

### Progress Bars

Track the progress of long-running tasks with a customizable progress bar.

```python
from py_style import ProgressBar

progress = ProgressBar(100, delay=0.5)
progress.run(style="bold")
```

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
