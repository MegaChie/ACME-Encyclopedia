import React, {useState, useEffect} from 'react'
import axios from 'axios';
import './Homepage.css';
import {Link} from "react-router-dom";


const Homepage = () => {
    const [articles, setArticles] = useState([]);
    const [searchQuery, setSearchQuery] = useState('');
    const [searchResults, setSearchResults] = useState([]);
    const [showResults, setShowResults] = useState(false);

    useEffect(() => {
        const fetchArticles = async () => {
            try {
                const response = await axios.get('/api/v1/articles',
                    {withCredentials: true});
                setArticles(response.data.articles);
                console.log(response.data.articles);
            } catch (e) {
                console.error("Error fetching articles", e);

            }
        };
        fetchArticles();
        }, []);
   const filteredArticles = articles.filter((article) =>
  article.Title && article.Title.toLowerCase().includes(searchQuery.toLowerCase()));
    const handleSearch = async (e) => {
    const query = e.target.value;
    setSearchQuery(query);

    if (query.length > 0) {
      try {
        const response = await axios.get(`/api/v1/search_articles`, {
          params: { q: query },
          withCredentials: true,
        });
        setSearchResults(response.data.articles);
        setShowResults(true);
      } catch (error) {
        console.error('Error searching articles:', error);
        setShowResults(false);
      }
    } else {
      setShowResults(false);
    }
  };
  const handleResultClick = (Title) => {
      setSearchQuery(Title);
      setShowResults(false);
  };


    return (
        <div className="homepage-container">
            <h1>Articles</h1>
            <input
                type="text"
                placeholder="Search articles by title..."
                value={searchQuery}
                onChange={handleSearch}
                className="search-bar"
            />
             {showResults && (
        <div className="search-results">
          {searchResults.map(article => (
            <div
              key={article._id}
              className="search-result-item"
              onClick={() => handleResultClick(article.Title)}
            >
              {article.Title}
            </div>
          ))}
        </div>
      )}
            <ul className="article-list">
                {filteredArticles.map(article => (
                    <li key={article['db ID']} className="article-item">
                        <Link to={`/article/${article['db ID']}`}>{article.Title}</Link>
                        <p>{article.content}</p>
                    </li>
                ))}
            </ul>
        </div>


    );

};

export default Homepage;

