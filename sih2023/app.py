from flask import Flask, render_template, request, jsonify
import subprocess
import concurrent.futures
app = Flask(__name__)
import os
STATICFILES_DIRS = [os.path.join(os.getcwd(), 'static')]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_prices', methods=['POST'])
def get_prices():
    product_name = request.form.get('product_name')

    # Paths to your Python scripts
    scripts = {
        'amazon': ['python', os.path.join(os.getcwd(), 'amazon.py'), product_name],
        'flipkart': ['python', os.path.join(os.getcwd(), 'flipkart.py'), product_name],
        'gem': ['python', os.path.join(os.getcwd(), 'gem.py'), product_name],
        'ebay': ['python', os.path.join(os.getcwd(), 'ebay.py'), product_name]
    }

    # Execute scripts concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = {executor.submit(subprocess.check_output, script, text=True): name for name, script in scripts.items()}

        response = {}
        for future in concurrent.futures.as_completed(results):
            script_name = results[future]
            try:
                response[script_name + '_price'] = future.result()
            except subprocess.CalledProcessError as e:
                response[script_name + '_error'] = str(e)
            except Exception as e:
                response[script_name + '_error'] = f'An unexpected error occurred: {str(e)}'

        return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
    

