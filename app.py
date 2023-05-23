import pytesseract
from PIL import Image
import datetime
import sys


def validate_args(arguments):
    """Returns True if arguments are valid, False otherwise"""
    if len(arguments) < 2:
        print("No path to the image is provided")
        return False
    if len(arguments) > 2:
        print("Too many arguments were given")
        return False

    return True


def get_text_from_image(image):    
    """Returns list of text from image"""
    text = pytesseract.image_to_string(image)
    
    return text.split()


def validate_pesel(pesel):
    """Returns True if PESEL is valid, False otherwise"""
    if len(pesel) != 11:
        return False

    # Checksum validation
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
    checksum = sum(int(pesel[i]) * weights[i] for i in range(11)) % 10
    if checksum != 0:
        return False

    # Date of bith validation
    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])

    if month > 80:
        year += 1800
        month -= 80
    elif month > 60:
        year += 2200
        month -= 60
    elif month > 40:
        year += 2100
        month -= 40
    elif month > 20:
        year += 2000
        month -= 20
    else:
        year += 1900

    try:
        birth_date = datetime.date(year, month, day)
    except ValueError:
        return False

    # Serial number validation
    serial_number = int(pesel[6:9])
    if serial_number == 0:
        return False

    return True



if __name__ == "__main__":
    arguments = sys.argv
    if not validate_args(arguments):
        exit()
        
    image = Image.open(arguments[1])
    text = get_text_from_image(image)
    for word in text:
        is_pesel = validate_pesel(word)
        print(f"{word} - {'PESEL' if is_pesel else 'not PESEL'}")