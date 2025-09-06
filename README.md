# 🎬 NextScene – Content-Based Movie Recommender System

NextScene is a **content-based movie recommender system** that suggests movies similar to a selected movie using **cosine similarity on movie metadata**. The app is built with **Streamlit** and powered by the **TMDB dataset**.

---

## 📊 Dataset

We used the TMDB Movie Metadata dataset, which is available on Kaggle:
🔗 [TMDB Movie Metadata (Kaggle)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

---

## 📦 Pre-trained Files

The required pickle (`.pkl`) files (movies data and similarity matrix) are available here:
🔗 [Google Drive – PKL Files](https://drive.google.com/drive/folders/1yltB5Ieryo6mXRXafNA4eruwrEnE4Gag?usp=drive_link)

---

## 🛠️ Requirements

Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt

```
--- 

##▶️ Running the App:
```bash
streamlit run app.py
```
---

##📂 Project Structure:
```bash
├── app.py              # Streamlit web app
├── movie_rec.ipynb     # Jupyter Notebook to preprocess data & generate PKL files
├── requirements.txt    # Required Python libraries
└── README.md           # Project documentation
```
---

##📜 License:

This project is licensed under the MIT License 
