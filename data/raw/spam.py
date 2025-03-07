import pandas as pd

url = "https://raw.githubusercontent.com/4GeeksAcademy/NLP-project-tutorial/main/url_spam.csv"

df = pd.read_csv(url)

df.to_csv('spam.csv', index=False)
print("Dataset saved as 'spam.csv'")