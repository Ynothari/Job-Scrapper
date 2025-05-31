import webbrowser
import pandas as pd

df = pd.read_csv("jobs.csv")
urls = df[df['site'].isin(['indeed', 'naukri'])]['job_url_direct'].dropna().tolist()

for url in urls:
    webbrowser.open(url)
