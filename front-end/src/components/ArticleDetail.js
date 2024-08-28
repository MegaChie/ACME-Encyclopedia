import React, {useState, useEffect} from 'react';
import {useParams, useNavigate} from 'react-router-dom';
import axios from 'axios';
import './ArticleDetail.css';

const ArticleDetail = () => {
    /*
    * Getting Article Details from the Backend
    * Renders the Article component
    * */
    const {id} = useParams();
   // console.log('id: ', id);
    const [article, setArticle] = useState(null);
    const [showLanguages, setShowLanguages] = useState(false)
    const navigate = useNavigate();


    useEffect(() => {
        const fetchArticle = async () => {
            try {
                const response = await axios.get(`/api/v1/articles/${id}`, {withCredentials: true,});
                setArticle(response.data);

                console.log('RESPONSE: ',response.data);


            } catch (e) {
                console.error("Error fetching article", e);
            }
        }
        fetchArticle();
    }, [id]);

    const handleTranslate = async (lan) =>
    {
        try
        {
            const response = await axios.post(`/api/v1/translate/${id}/${lan}`,{}, {withCredentials: true,});
            console.log(`ID: ${id}, LANGUAGE: ${lan}`);
            setArticle(response.data);
        } catch (e)
        {
            console.error("Error translating article", e);
        }
    }
    if (!article) {
        return <div>Loading...</div>;
    }

    return (
        <div className="article-detail-container">
            <h1>{article.title}</h1>
            <p>{article.content}</p>
            <button onClick={() => navigate('/home')}>Back to Homepage</button>

            <div className="translate-button-container">
                <button onClick={() => setShowLanguages(!showLanguages)}>Translate</button>
                {showLanguages && (
                    <div className="language-menu">
                        <button onClick={() => handleTranslate('en')}>English</button>
                        <button onClick={() => handleTranslate('fr')}>French</button>
                        <button onClick={() => handleTranslate('gr')}>German</button>
                    </div>
                )}
            </div>
        </div>

    );


};

export default ArticleDetail;