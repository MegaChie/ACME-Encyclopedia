import { useEffect, useState } from "react";
import useDetectUser from "./Hooks/useDetectUser";
import "./css/Articles.css";

// Graps the articles from the database
const fetchArticles = async () => {
  try {
    const res = await fetch("api/v1/articles");
    const data = await res.json();
    return data;
  } catch (err) {
    console.error(err);
  }
}

const Articles = async () => {
  // Checks if a user logged in
  const fetchAuthed = useDetectUser();

  const [isAuthed, setIsAuthed] = useState(false);
  // const [userName, setUserName] = useState(null);
  const [articlesList, setArticlesList] = useState([]);

  // Uses the value from the user checking
  useEffect(() => {
    try {
      setIsAuthed(fetchAuthed.is_logged);
    } catch (err) {
      console.error(err);
    }
  }, []);

  // Gets the user name
  // useEffect(() => {
  //   try {
  //     fetchAuthed().then((name) => {
  //       setUserName(name.user);
  //     });
  //   } catch (err) {
  //     console.error(err);
  //   }
  // }, []);

  // Prepares the article list to be used
  useEffect(() => {
    try {
      fetchArticles().then((listOfArticles) => {
        setArticlesList(listOfArticles.articles);
      });
    } catch (err) {
      console.error(err);
    }
  }, []);

  const articleList = articlesList.map((article) => (
    <li key={article["db ID"]}>{article.Title}</li>
  ))

  return (
    <div className="articleLayout">
      {
        isAuthed ? (
          <ul>{articleList}</ul>
        ) : (
          <p>signup or login popup</p>
        )
      }
    </div>
  );
}

export default Articles;
