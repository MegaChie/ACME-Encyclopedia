import React, {useState, useEffect} from 'react'
import axios from 'axios';
import './Homepage.css';


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
            } catch (e) {
                console.error("Error fetching articles", e);

            }
        };
        fetchArticles();
        }, []);
    const filteredArticles = articles.filter((article) =>
        article.title.toLowerCase().includes(searchQuery.toLowerCase()) > -1);
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
  const handleResultClick = (title) => {
      setSearchQuery(title);
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
              onClick={() => handleResultClick(article.title)}
            >
              {article.title}
            </div>
          ))}
        </div>
      )}
            <ul className="article-list">
                {filteredArticles.map(article => (
                    <li key={article.id} className="article-item">
                        <h3>{article.title}</h3>
                        <p>{article.content}</p>
                    </li>
                ))}
            </ul>
        </div>


    );

};

export default Homepage;

