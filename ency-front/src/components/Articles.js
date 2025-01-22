import React, { useEffect, useState } from "react";

const fetchAuthed = async () => {
  const res = await fetch("api/v1/auth_check");
  const logs = await res.json();
  return logs;
}

function Articles() {
  const [isAuthed, setIsAuthed] = useState("Nope...");
  const [userName, setUserName] = useState(null);

  useEffect(() => {
    fetchAuthed().then((condition) => {
      setIsAuthed(condition.is_logged);
    });
  }, []);

  useEffect(() => {
    fetchAuthed().then((name) => {
      setUserName(name.user);
    });
  }, []);
  return (
    <div className="userCheck">
      {
        isAuthed ? (<p>name is {userName}</p>) : (<p>please signup or login</p>)
      }
    </div>
  );
}

export default Articles;
