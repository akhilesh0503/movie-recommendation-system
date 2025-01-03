# **Movie Recommendation System**

A web-based **Movie Recommendation System** leveraging similarity metrics to suggest movies similar to a user's favorite. This project uses a combination of machine learning techniques, precomputed similarity scores, and a **Streamlit** interface for an interactive user experience.

---

## **Table of Contents**
1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [How It Works](#how-it-works)
5. [Installation and Setup](#installation-and-setup)
6. [Usage](#usage)
7. [Directory Structure](#directory-structure)
8. [Demo](#demo)
9. [Contributing](#contributing)
10. [License](#license)

---

## **Overview**

This recommendation system:
- Suggests movies similar to a user-provided movie title.
- Uses precomputed similarity scores saved in a `.pkl` file for efficiency.
- Employs a visually appealing and user-friendly web interface powered by **Streamlit**.

---

## **Features**
- **Movie Similarity Calculation:** Utilizes cosine similarity to determine closeness between movies based on:
  - Genres
  - Cast
  - Directors
  - Keywords
- **Efficient Recommendation:** Precomputed similarity scores ensure fast recommendations.
- **Interactive UI:** Built using **Streamlit**, featuring dropdowns, buttons, and a clean design.
- **Background Customization:** Supports dynamic background images for enhanced visual appeal.

---

## **Technologies Used**
- **Python Libraries:**
  - `streamlit`: Web application framework.
  - `pickle`: To save and load precomputed similarity scores.
  - `scipy.spatial`: For calculating cosine similarity.
- **Machine Learning Techniques:** Similarity-based recommendation using preprocessed data.
- **Frontend Styling:** CSS integrated into Streamlit for a polished UI.

---

## **How It Works**
1. **Precomputing Similarity Scores:**
   - A `.pkl` file (`movies.pkl`) stores precomputed cosine similarity scores.
2. **Streamlit Application:**
   - Users select a movie title from a dropdown.
   - Upon clicking the **Recommend** button, the system suggests 10 similar movies.
3. **Similarity Metrics:**
   - Features such as genres, cast, directors, and keywords are vectorized and compared using cosine similarity.

---

## **Installation and Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system
