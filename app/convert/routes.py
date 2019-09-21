from flask import Blueprint, render_template, jsonify, request

from utils import int_to_roman, roman_to_int

convert = Blueprint('convert', __name__)


@convert.route('/bg_convert')
def bg_convert():
    try:
        roman_input = request.args.get('roman', 0, type=str)
        arabic_input = request.args.get('arabic', 0, type=str)
        if roman_input != "" and arabic_input == "":
            roman_numb = roman_input
            arabic_numb = roman_to_int(roman_input)
            text = 'Convertation to arabic have been made successful'
            return jsonify(roman_numb=roman_numb, arabic_numb=arabic_numb, text=text)
        elif roman_input == "" and arabic_input != "":
            roman_numb = int_to_roman(int(arabic_input))
            arabic_numb = arabic_input
            text = 'Convertation to roman have been made successful'
            return jsonify(roman_numb=roman_numb, arabic_numb=arabic_numb, text=text)
        else:
            text = 'Convertation failed! Please enter only one number to convert'
            return jsonify(roman_numb='', arabic_numb='', text=text)
    except Exception as e:
        return jsonify(text=str(e))


@convert.route('/')
def init():
    return render_template('layout.html')
