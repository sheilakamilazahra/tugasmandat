from flask import Flask, render_template_string
import statistics

app = Flask(__name__)

@app.route('/')
def home():
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # Melakukan analisis data sederhana
    mean_val = statistics.mean(data)
    median_val = statistics.median(data)
    stdev_val = statistics.stdev(data)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Analisis Data Sederhana</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f4; color: #333; }}
            .container {{ background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); max-width: 600px; margin: auto; }}
            h1 {{ color: #0056b3; }}
            ul {{ list-style-type: none; padding: 0; }}
            li {{ margin-bottom: 10px; }}
            strong {{ color: #007bff; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hasil Analisis Data Sederhana</h1>
            <p>Data yang dianalisis: {data}</p>
            <ul>
                <li><strong>Rata-rata (Mean):</strong> {mean_val:.2f}</li>
                <li><strong>Median:</strong> {median_val:.2f}</li>
                <li><strong>Standar Deviasi:</strong> {stdev_val:.2f}</li>
            </ul>
            <p>Aplikasi ini dibuat dengan Python Flask dan dijalankan di Docker.</p>
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    # Flask akan mendengarkan di semua interface yang tersedia (0.0.0.0)
    # dan pada port 5000 (port default Flask)
    app.run(debug=True, host='0.0.0.0', port=5000)