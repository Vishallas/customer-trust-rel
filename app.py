from flask import Flask, render_template, request
import os
import joblib
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

model = joblib.load('classifier.joblib')

# Define dictionaries for dropdown options
industries = {
    'None': None,
    'Horizontal': 16,
    'Healthcare': 15,
    'Legal': 17,
    'Energy, Gas, Oil, Utilities': 10,
    'Construction': 7,
    'Entertainment, Hospitality, Travel': 11,
    'Retail': 23,
    'Real Estate & Property Mgt.': 22,
    'Financial Services': 12,
    'Education': 9,
    'Automotive': 1,
    'Sports and Fitness': 24,
    'Food': 13,
    'Logistics, Supply Chain, Transportation': 18,
    'CPG': 4,
    'Agriculture': 0,
    'Non-Profit': 20,
    'Manufacturing': 19,
    'Cannabis': 5,
    'Government': 14,
    'Aviation': 2,
    'Real Estate': 21,
    'BioTech': 3,
    'Cryptocurrency': 8,
    'Clinical': 6
}

categories = {
    'None': None,
    'On-Demand Services': 16,
    'Communications': 7,
    'Analytics and BI': 2,
    'Business Mgt and ERP': 4,
    'Compliance': 8,
    'Practice Management': 18,
    'Sales and Marketing': 20,
    'Logistics and Supply Chain': 14,
    'IT Mgt': 13,
    'Accounting and Finance': 1,
    'Ecommerce': 11,
    'Document Management': 10,
    'HR and Recruiting': 12,
    'Cybersecurity': 9,
    'Cloud and Software Dev Tools': 6,
    'Point of Sale': 17,
    'Marketplace': 15,
    'Automation': 3,
    'Clinical': 5,
    'eLearning': 24,
    'AI and Machine Learning': 0,
    'Virtual Reality': 22,
    'Student Mgt': 21,
    'Practice Mgt': 19,
    'eCommerce': 23
}

c3_options = {
    'None': None,
    'B2B SaaS': 0,
    'B2G': 1
}

c4_options = {
    'None': None,
    'Self-funded': 7,
    'VC-funded': 8,
    'Angel or Seed Funding': 1,
    'Acquired': 0,
    'Public': 6,
    'Private Equity funding': 5,
    'Other': 3,
    'Angel or Seed funding': 2,
    'Private Equity Funding': 4
}

c5_options = {
    'None': None,
    'Small': 0,
    'Startup': 1,
    'Large': 2,
    'Medium': 3
}

@app.route("/", methods=["GET", "POST"])
def index():
    selected_industry = 'None'
    selected_category = 'None'
    selected_c3 = 'None'
    selected_c4 = 'None'
    selected_c5 = 'None'
    result = ''

    if request.method == "POST":
        selected_industry = request.form.get("industry")
        selected_category = request.form.get("category")
        selected_c3 = request.form.get('three')
        selected_c4 = request.form.get('four')
        selected_c5 = request.form.get('five')
        input_data = [
            industries[selected_industry],
            categories[selected_category],
            c3_options[selected_c3],
            c4_options[selected_c4],
            c5_options[selected_c5]
        ]
        prediction = model.predict([input_data])
        result = 'Can trust' if prediction[0] else "Can't be trusted"

    return render_template(
        "index.html",
        industries=industries.keys(),
        categories=categories.keys(),
        c3_options=c3_options.keys(),
        c4_options=c4_options.keys(),
        c5_options=c5_options.keys(),
        selected_industry=selected_industry,
        selected_category=selected_category,
        selected_c3=selected_c3,
        selected_c4=selected_c4,
        selected_c5=selected_c5,
        result=result
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT'), debug=True)
