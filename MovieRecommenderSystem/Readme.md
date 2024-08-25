# 🎬 Movie Recommender System 🍿

A Streamlit-based web application that recommends movies based on user selection. Discover your next favorite film! 🌟

## 📊 Dataset

The movie dataset used in this project is from The Movies Dataset on Kaggle. You can find it here:
[TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## ✨ Features

- 🖥️ User-friendly interface with a sleek dark theme
- 🔽 Movie selection from an easy-to-use dropdown menu
- 🖼️ Fetches and displays eye-catching movie posters
- 🎯 Recommends 5 similar movies based on your selection
- 📱 Responsive design for seamless viewing on various devices

## 🛠️ Technologies Used

- 🐍 Python
- 🌊 Streamlit
- 🐼 Pandas
- 🌐 Requests
- 🥒 Pickle

## 🚀 Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/Abhishek-yadv/MovieRecommenderSystem.git
   cd MovieRecommenderSystem
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Ensure you have the following files in your project directory:
   - `movie_dict.pkl`: Pickle file containing the movie dataframe
   - `similarity.pkl`: Pickle file containing the similarity matrix

## 🎮 Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and go to `http://localhost:8501`

3. Select a movie from the dropdown menu �movie

4. Click on "Get Recommendations" to see similar movies 🔍

## 🧠 How it Works

1. 📊 The app loads pre-processed movie data and a similarity matrix from pickle files.
2. 👆 Users select a movie from the dropdown menu.
3. 🔢 When the user clicks "Get Recommendations", the app finds similar movies based on the similarity matrix.
4. 🖼️ The app fetches movie posters from The Movie Database (TMDb) API.
5. 📺 The recommended movies and their posters are displayed in a visually appealing grid layout.

## 🔑 API Usage

This project uses The Movie Database (TMDb) API to fetch movie posters. Make sure you have a valid API key and replace it in the `fetch_poster` function if necessary.

## 🎨 Customization

You can customize the app's appearance by modifying the custom CSS in the `st.markdown` section of the code. Make it your own! 🖌️

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/Abhishek-yadv/MovieRecommenderSystem/issues) if you want to contribute.

## 👨‍💻 Author

Abhishek Yadav

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Show your support

Give a ⭐️ if this project helped you!

## 📝 Note

This README is part of the Movie Recommender System project. For the most up-to-date information, please visit the [GitHub repository](https://github.com/Abhishek-yadv/MovieRecommenderSystem/tree/main).

Happy movie watching! 🎥🍕
