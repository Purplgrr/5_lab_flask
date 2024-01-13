import constants as constants
from app import app
from flask import render_template, request
from calculation import solve_operations

@app.route('/', methods=['GET', 'POST'])
def index():
    input_type = '1'
    
    base = 0
    height = 0
    
    side_a = 0
    side_b = 0
    
    angle_a = 0
    angle_b = 0

    operation_list = []

    result = ''

    if 'show' in request.form:
        input_type = request.form.get('input')
        base = request.form.get('base')
        height = request.form.get('height')
        operation_list = request.form.getlist('operation')

        if input_type == '1':
            if side_a:
                side_a = request.form.get('side_a')
            if side_b:
                side_b = request.form.get('side_b')
        else:
            if angle_a:
                angle_a = request.form.get('angle_a')
            if angle_b:
                angle_b = request.form.get('angle_b')
    if 'solve' in request.form:
        input_type = request.form.get('input')
        base = int(request.form.get('base'))
        height = int(request.form.get('height'))
        operation_list = request.form.getlist('operation')

        if input_type == '1':
            side_a = int(request.form.get('side_a'))
            side_b = int(request.form.get('side_b'))
        else:
            angle_a = int(request.form.get('angle_a'))
            angle_b = int(request.form.get('angle_b'))
        
        result = solve_operations(
            input_type, 
            operation_list,
            (base, height, side_a, side_b, angle_a, angle_b)
        )

    html = render_template(
        'index.html',
        input_type=input_type,
        operations = constants.operations,
        base=base,
        height=height,
        operation_list=operation_list,
        side_a=side_a,
        side_b=side_b,
        angle_a=angle_a,
        angle_b=angle_b,
        result=result,
        len=len,
        str=str,
    )
    return html