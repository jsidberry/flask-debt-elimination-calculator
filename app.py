from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage for demo purposes
debts = []

creditors = [
    {"name": "Creditor A", "amount_owed": 5000, "minimum_payment": 100},
    {"name": "Creditor B", "amount_owed": 3000, "minimum_payment": 150},
    # Add more creditors as needed
]

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get form details
        debt_details = {
            'creditor_name': request.form.get('creditor_name'),
            'type_of_credit': request.form.get('type_of_credit'),
            'total_credit_limit': float(request.form.get('total_credit_limit')),
            'current_credit_balance': float(request.form.get('current_credit_balance')),
            'interest_rate': float(request.form.get('interest_rate')),
            'minimum_monthly_payment': float(request.form.get('minimum_monthly_payment'))
        }
        # Add the new debt
        debts.append(debt_details)
        # Redirect to the debt list page
        return redirect(url_for('list_debts'))
    return render_template('index.html')

@app.route('/debts')
def list_debts():
    # No sorting logic here; just pass the debts to the template
    return render_template('debts.html', debts=debts)

@app.route('/creditors')
def show_creditors():
    return render_template('creditors.html', creditors=creditors)

@app.route('/accelerator')
def show_accelerator():
    return render_template('accelerator.html', creditors=creditors)

if __name__ == '__main__':
    app.run(debug=True)

