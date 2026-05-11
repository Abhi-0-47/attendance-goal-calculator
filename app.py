from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate():
    result = None
    if request.method == 'POST':
        attended = int(request.form['attended'])
        total = int(request.form['total'])
        target = int(request.form['target'])
        
        current_perc = (attended / total) * 100
        
        if current_perc >= target:
            # Calculate how many they can miss
            can_miss = 0
            temp_total = total
            while ((attended / (temp_total + 1)) * 100) >= target:
                can_miss += 1
                temp_total += 1
            result = f"You have {current_perc:.2f}% attendance. You can miss {can_miss} more classes."
        else:
            # Calculate how many they need to attend
            must_attend = 0
            temp_attended = attended
            temp_total = total
            while ((temp_attended / temp_total) * 100) < target:
                must_attend += 1
                temp_attended += 1
                temp_total += 1
            result = f"You have {current_perc:.2f}% attendance. You need to attend {must_attend} more classes to hit {target}%."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5001) # Using port 5001 so it doesn't clash with the tracker