# QR-Code-Generator

This is a Python script that generates a QR code image based on a given URL. It uses the `qrcode` library to create the QR code and save it as an image file.

## Prerequisites

Make sure you have the following installed:

- Python (version 3 or above)
- The `qrcode` library

You can install the `qrcode` library by running the following command:

```shell
pip install qrcode
```

## Usage

1. Clone the repository or download the `qr_code_generator.py` file.

2. Open a terminal or command prompt and navigate to the directory where the `qr_code_generator.py` file is located.

3. Run the script using the following command:

```shell
python qr_code_generator.py
```

4. Enter the URL you want to generate a QR code for when prompted.

5. Optionally, enter a desired filename for the QR code image. If no filename is provided, the default filename "qrimg.png" will be used.

6. The QR code image will be generated and saved in the same directory.

## Example

Here's an example usage of the script:

```shell
$ python qr_code_generator.py
Enter your URL: https://example.com
Enter the name for your QR Code file ending with .png: my_qr_code.png
```

This will generate a QR code image for the URL "https://example.com" and save it as "my_qr_code.png" in the current directory.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and use this code according to your needs.
