# 🎬 Movie Recommender System

A machine learning-powered web application that recommends movies based on similarity using content-based filtering. Built with Streamlit and scikit-learn, this system analyzes movie data and suggests the top 10 most similar movies to your selection.

## 🌐 Live Demo

Try the application live here: [Movie Recommender System](https://prashant123-svg-movie-recommender-system-main-qdsf8w.streamlit.app/)

## ✨ Features

- **Interactive UI**: User-friendly interface built with Streamlit
- **Movie Search**: Easily search and select from a database of movies
- **Smart Recommendations**: Get 10 similar movie recommendations using TF-IDF vectorization
- **Fast Similarity Matching**: Uses cosine similarity for efficient movie matching
- **Error Handling**: Graceful handling of invalid movie selections
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## 🛠️ Technologies Used

- **Streamlit** - Web application framework
- **scikit-learn** - Machine learning library (TF-IDF, cosine similarity)
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **Python 3.x** - Programming language

## 📋 Requirements

```
streamlit==1.28.1
scikit-learn==1.3.2
pandas==2.1.3
numpy==1.24.3
```

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Prashant123-svg/Movie-Recommender-System.git
   cd Movie-Recommender-System
   ```

2. **Create a Virtual Environment** (Optional but recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   streamlit run main.py
   ```

5. **Access the App**
   - The application will open in your default browser at `http://localhost:8501`
   - If it doesn't open automatically, navigate to the URL shown in the terminal

## 📖 How to Use

1. **Select a Movie**: Use the dropdown menu to search for or select a movie from the database
2. **Get Recommendations**: Click the "Recommend Movies" button
3. **View Results**: The system will display the top 10 movies most similar to your selection
4. **Repeat**: Try different movies to explore more recommendations

## 🔧 How It Works

The recommendation system uses **content-based filtering** with the following approach:

1. **TF-IDF Vectorization**: Converts movie features (titles, descriptions, etc.) into numerical vectors
2. **Similarity Calculation**: Computes cosine similarity between movies to find the most similar ones
3. **Ranking**: Returns the top 10 movies with the highest similarity scores
4. **Display**: Shows the ranked recommendations to the user

### Algorithm Details
- **Method**: Content-Based Collaborative Filtering
- **Similarity Metric**: Cosine Similarity
- **Vectorization**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Number of Recommendations**: Top 10 similar movies

## 📁 Project Structure

```
movie_recomm/
├── main.py                 # Main Streamlit application
├── requirements.txt        # Project dependencies
├── df.pkl                  # Movie dataset (pickled)
├── indices.pkl             # Movie title to index mapping
├── tfidf.pkl              # TF-IDF vectorizer object
├── tfidf_matrix.pkl       # Pre-computed TF-IDF matrix
└── README.md              # Project documentation
```

## 📊 Dataset

The project uses pre-processed movie data stored in pickle format:
- **df.pkl**: Contains the movie dataframe with titles and metadata
- **tfidf_matrix.pkl**: Pre-computed TF-IDF matrix for fast similarity calculations
- **indices.pkl**: Mapping of movie titles to their indices in the dataset

## 🎯 Use Cases

- Discover new movies similar to ones you've enjoyed
- Find hidden gems in your favorite genres
- Get personalized recommendations instantly
- Explore the movie database interactively

## ⚠️ Error Handling

The application includes robust error handling:
- **Movie Not Found**: Returns a message if the selected movie isn't in the database
- **Invalid Indices**: Filters out invalid recommendations gracefully
- **No Results**: Displays a message if no valid recommendations can be found

## 🔮 Future Enhancements

Potential improvements for the system:
- Hybrid recommendation system (content + collaborative filtering)
- User rating-based recommendations
- Genre-specific filters
- Movie metadata display (year, genre, rating)
- Search autocomplete suggestions
- User preferences and personalization
- More detailed similarity scores
- Movie ratings and reviews integration

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open-source and available under the MIT License. See the LICENSE file for more details.

## 👤 Author

**Prashant Kumar**
- GitHub: [@Prashant123-svg](https://github.com/Prashant123-svg)
- Project: [Movie-Recommender-System](https://github.com/Prashant123-svg/Movie-Recommender-System)

## 🙏 Acknowledgments

- **Streamlit** - For making it easy to build data applications
- **scikit-learn** - For powerful machine learning tools
- **Movie Database** - For the movie data
- All contributors and supporters

## 📧 Support

If you encounter any issues or have suggestions, please:
- Open an issue on GitHub
- Contact the author directly
- Check the Streamlit documentation for troubleshooting

## 🎓 Learning Resources

If you want to learn more about the concepts used:
- [Streamlit Documentation](https://docs.streamlit.io/)
- [scikit-learn TF-IDF](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
- [Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity)
- [Content-Based Recommendation Systems](https://en.wikipedia.org/wiki/Recommender_system#Content-based_filtering)

---

**Made with ❤️ by the Movie Recommender Team**
image of my project
<img width="1916" height="917" alt="image" src="https://github.com/user-attachments/assets/5ced4d09-212b-46de-8374-f79383d55087" />
