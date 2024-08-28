# API Docs

---

- **`[GET]`**
    - **`[GET]` Lists Articles**
        
        
        | Description | Returns all articles in the database or one article if ID is passed. Works only with published  articles |
        | --- | --- |
        | URL | [domain/api/v1/articles/ID](API%20Docs%20a3ab83c49bee49f5aaa08f4b512f1b08.md) |
        | Auth Required | Yes |
        
        - **✅ Response 200 - Without ID**
            
            ```python
            {
                "articles": [
                    {
                        "Author": "fake2",
                        "Content": "Some text1",
                        "Created at": "2024-08-27T19:52:38.316000",
                        "Language": "en",
                        "Rank": 1,
                        "Status": "published",
                        "Tags": [
                            "new",
                            "test",
                            "username"
                        ],
                        "Title": "Title with auther1",
                        "Updated_at": "2024-08-27T19:52:38.316000",
                        "db ID": "66ce2e867b8a7dd2fa0b89d0"
                    },
                    {
                        "Author": "fake2",
                        "Content": "Some text5",
                        "Created at": "2024-08-27T19:52:38.305000",
                        "Language": "en",
                        "Rank": 1,
                        "Status": "published",
                        "Tags": [
                            "new",
                            "test",
                            "username"
                        ],
                        "Title": "Title with auther5",
                        "Updated_at": "2024-08-27T19:52:38.305000",
                        "db ID": "66ce2e867b8a7dd2fa0b89cf"
                    },
                    {
                        "Author": "fake2",
                        "Content": "some new text",
                        "Created at": "2024-08-27T21:56:26.704000",
                        "Language": "en",
                        "Rank": 0,
                        "Status": "published",
                        "Tags": [
                            "fake2",
                            "ranke"
                        ],
                        "Title": "create new",
                        "Updated_at": "2024-08-27T21:56:26.704000",
                        "db ID": "66ce4b8a7b8a7dd2fa0b89d2"
                    }
                ]
            }
            ```
            
        - **✅ Response 200 - With ID**
            
            ```python
            {
                "_id": {
                    "$oid": "66ce4b8a7b8a7dd2fa0b89d2"
                },
                "author": "fake2",
                "content": "some new text",
                "created_at": {
                    "$date": "2024-08-27T21:56:26.704Z"
                },
                "language": "en",
                "rank": 0,
                "status": "published",
                "tags": [
                    "fake2",
                    "ranke"
                ],
                "title": "create new",
                "updated_at": {
                    "$date": "2024-08-27T21:56:26.704Z"
                }
            }
            ```
            
        - **✅ Response 404 - Without ID**
            
            ```python
            {
            		"Error": "Article not found"
            }
            ```
            
    - **`[GET]` Searches Articles**
        
        
        | Description | Returns all articles in the database based on the name and if the article is published |
        | --- | --- |
        | URL | [domain/api/v1/search_articles](API%20Docs%20a3ab83c49bee49f5aaa08f4b512f1b08.md) |
        | Auth Required | Yes |
        
        | Paramater | Type  | Required | Description |
        | --- | --- | --- | --- |
        | `url params` |  |  |  |
        | q | String | Yes | Holds the title the user intends to search with |
        - **✅ Response 200**
            
            ```python
            {
                "_id": {
                    "$oid": "66ce4b8a7b8a7dd2fa0b89d2"
                },
                "author": "fake2",
                "content": "some new text",
                "created_at": {
                    "$date": "2024-08-27T21:56:26.704Z"
                },
                "language": "en",
                "rank": 0,
                "status": "published",
                "tags": [
                    "fake2",
                    "ranke"
                ],
                "title": "create new",
                "updated_at": {
                    "$date": "2024-08-27T21:56:26.704Z"
                }
            }
            ```
            
        - **✅ Response 400**
            
            ```python
            {
                "Error": "No search query provided"
            }
            ```
            
        - **✅ Response 404**
            
            ```python
            {
            		"Error": "Article not found"
            }
            ```
            
    - **`[GET]` API status**
        
        
        | Description | Returns the status of the API |
        | --- | --- |
        | URL | [domain/api/v1/status](API%20Docs%20a3ab83c49bee49f5aaa08f4b512f1b08.md) |
        | Auth Required | No |
        
        - **✅ Response 200**
            
            ```python
            {
              "Status": "API running!"
            }
            ```
            
    - **`[GET]` Database statistics**
        
        
        | Description | Returns statistics about the database |
        | --- | --- |
        | URL | [domain/api/v1/stats](API%20Docs%20a3ab83c49bee49f5aaa08f4b512f1b08.md) |
        | Auth Required | No |
        
        - **✅ Response 200**
            
            ```python
            {
                "Articles": 5,
                "Users": 1
            }
            ```
            
    - **`[GET]` Session Check**
        
        
        | Description | Returns information about user’s session |
        | --- | --- |
        | URL | [domain/api/v1/check_session](API%20Docs%20a3ab83c49bee49f5aaa08f4b512f1b08.md) |
        | Auth Required | Yes |
        
        - **✅ Response 200 - Session available**
            
            ```python
            {
                "Status": "Session is active",
                "User": temp
            }
            ```
            
        - **✅ Response 200 - Session unavailable**
            
            ```python
            {
                "Status": "No active session",
            		"cookie": "Auth cookie"
            }
            ```
            
    - **`[GET]` User logout**
        
        
        | Description | Logs out a user |
        | --- | --- |
        | URL | [domain/api/v1/logout](API%20Docs%20a3ab83c49bee49f5aaa08f4b512f1b08.md) |
        | Auth Required | Yes |
        
        - **✅ Response 200**
            
            ```python
            {
            		"Status": "Logged out! Please Sign in again"
            }
            ```
            
    - **`[GET]` List users**
        
        
        | Description | Returns all users in the database or one user if ID is passed |
        | --- | --- |
        | URL | [domain/api/v1/users/ID](API%20Docs%20a3ab83c49bee49f5aaa08f4b512f1b08.md) |
        | Auth Required | Yes |
        
        | Paramater | Type  | Required | Description |
        | --- | --- | --- | --- |
        | `url params` |  |  |  |
        | ID | ID object - String | No | Holds the user’s id in the database |
        - **✅ Response 200 - Without ID**
            
            ```python
            {
                "All users": [
                    {
                        "Email": "fake2",
                        "User name": "fake2",
                        "db ID": "66ce2e5e7b8a7dd2fa0b89cc"
                    },
                    {
                        "Email": "temp",
                        "User name": "temp",
                        "db ID": "66ce5d4d7b8a7dd2fa0b89d3"
                    }
                ]
            }
            ```
            
        - **✅ Response 200 - With ID**
            
            ```python
            {
                "Email": "temp",
                "User name": "temp",
                "db ID": "66ce5d4d7b8a7dd2fa0b89d3"
            }
            ```
            
        - **✅ Response 404 - With ID**
            
            ```python
            {
                "Error": "User not found"
            }
            ```
            
    

---

- **`[DELETE]`**
    - **`[DELETE]` Delete user**
        
        
        | Description | Deletes a user from database |
        | --- | --- |
        | URL | [domain/api/v1/delete_users/ID](API%20Docs%20a3ab83c49bee49f5aaa08f4b512f1b08.md) |
        | Auth Required | Yes |
        
        | Paramater | Type  | Required | Description |
        | --- | --- | --- | --- |
        | `url params` |  |  |  |
        | ID | ID object - String | No | Holds the user’s id in the database |
        - **✅ Response 200**
            
            ```python
            {
            		"Status": "Deletion done"
            }
            ```
            
        - **✅ Response 404**
            
            ```python
            {
            		"Error": "User not found"
            }
            ```
            
        - **✅ Response 400**
            
            ```python
            {
            		"Status": "Failed",
            		"Reason": "No ID passed"
            }
            ```
            
    

---

- **`[PUT]`**
    - **`[PUT]` Edits an article**
        
        
        | Description | Edit an article as long as it is the original author making the changes |
        | --- | --- |
        | URL | [domain/api/v1/edit_articles/ID](API%20Docs%20a3ab83c49bee49f5aaa08f4b512f1b08.md) |
        | Auth Required | Yes |
        
        | Paramater | Type  | Required | Description |
        | --- | --- | --- | --- |
        | `Body params` |  |  |  |
        | Title | String | Yes | Title of the added article |
        | Content | String | Yes | Text for the added article |
        | Tags | List of string | No | Key-words  in the added article |
        | Author | String | No | Name of the added article writer |
        
        | Paramater | Type  | Required | Description |
        | --- | --- | --- | --- |
        | `url params` |  |  |  |
        | ID | ID object - String | Yes | Holds the database ID of the article the user intends to edit  |
        - **✅ Response 403**
            
            ```python
            {
            		"Error": "You are not the author of this article"
            }
            ```
            
        - **✅ Response 201**
            
            ```python
            {
            		"Status": "Success"
            }
            ```
            
        - **✅ Response 404**
            
            ```python
            {
            		"Error": "Article not found"
            }
            ```
            
    - **`[PUT]` Rank an article**
        
        
        | Description | Add one point to the rank of an article |
        | --- | --- |
        | URL | [domain/api/v1/article/ID/rank](API%20Docs%20a3ab83c49bee49f5aaa08f4b512f1b08.md) |
        | Auth Required | Yes |
        
        | Paramater | Type  | Required | Description |
        | --- | --- | --- | --- |
        | `url params` |  |  |  |
        | ID | ID object - String | Yes | Holds the database ID of the article the user intends to rank up |
        - **✅ Response 200**
            
            ```python
            {
            		"Status": "Article ranked up by one"
            }
            ```
            
        - **✅ Response 404**
            
            ```python
            {
            		"Error": "Article not found"
            }
            ```
            
    - **`[PUT]` Edit the user’s information**
        
        
        | Description | Updates a user’s information |
        | --- | --- |
        | URL | [domain/api/v1/edit_user/ID](API%20Docs%20a3ab83c49bee49f5aaa08f4b512f1b08.md) |
        | Auth Required | Yes |
        
        | Paramater | Type  | Required | Description |
        | --- | --- | --- | --- |
        | `url params` |  |  |  |
        | ID | ID object - String | Yes | Holds the database ID of the user in question |
        - **✅ Response 200**
            
            ```python
            {
            		"Status": "User edited"
            }
            ```
            
        - **✅ Response 400**
            
            ```python
            {
            		"Error": "Not a JSON"
            }
            ```
            
        - **✅ Response 404**
            
            ```python
            {
            		"Error": "User not found"
            }
            ```
            

---

- **`[POST]`**
    - **`[POST]` Add article**
        
        
        | Description | Updates the database by adding an article to it |
        | --- | --- |
        | URL | [domain/api/v1/add_article](API%20Docs%20a3ab83c49bee49f5aaa08f4b512f1b08.md) |
        | Auth Required | Yes |
        
        | Paramater | Type  | Required | Description |
        | --- | --- | --- | --- |
        | `Body params` |  |  |  |
        | Title | String | Yes | Title of the added article |
        | Content | String | Yes | Text for the added article |
        | Tags | List of string | No | Key-words  in the added article |
        | Author | String | No | Name of the added article writer |
        
        - **✅ Response 201**
            
            ```python
            {
                "_id": {
                    "$oid": "66ce4b8a7b8a7dd2fa0b89d2"
                },
                "author": "fake2",
                "content": "some new text",
                "created_at": {
                    "$date": "2024-08-27T21:56:26.704Z"
                },
                "language": "en",
                "rank": 0,
                "status": "published",
                "tags": [
                    "fake2",
                    "ranke"
                ],
                "title": "create new",
                "updated_at": {
                    "$date": "2024-08-27T21:56:26.704Z"
                }
            }
            ```
            
        - **✅ Response 400**
            
            ```python
            {
            		"Error": "Plese add a tile, content and language"
            }
            ```
            
        - **✅ Response 400**
            
            ```python
            {
            		"Error": "Request must be JSON"
            }
            ```
            
    - **`[POST]` Log user**
        
        
        | Description | Logs in a user |
        | --- | --- |
        | URL | [domain/api/v1/login](API%20Docs%20a3ab83c49bee49f5aaa08f4b512f1b08.md) |
        | Auth Required | Yes |
        
        - **✅ Response 201**
            
            ```python
            {
                "Status": "Logged in!"
            }
            ```
            
        - **✅ Response 400**
            
            ```python
            {
            		"Error": "Not a JSON"
            }
            ```
            
        - **✅ Response 400**
            
            ```python
            {
            		"Error": "Missing data"
            }
            ```
            
    - **`[POST]` Translate**
        
        
        | Description | Translate article to selected language and adds the translation to the database as new article |
        | --- | --- |
        | URL | [domain/api/v1/translate/ID/LAN](API%20Docs%20a3ab83c49bee49f5aaa08f4b512f1b08.md) |
        | Auth Required | Yes |
        
        | Paramater | Type  | Required | Description |
        | --- | --- | --- | --- |
        | `url params` |  |  |  |
        | ID | ID object - String | Yes | Holds the database ID of the article in question |
        | LAN | Two letters - String | Yes | Determines the language to translate the article to |
        - **✅ Response 201**
            
            ```python
            {
                "_id": {
                    "$oid": "66ce4b8a7b8a7dd2fa0b89d2"
                },
                "author": "fake2",
                "content": "some new text",
                "created_at": {
                    "$date": "2024-08-27T21:56:26.704Z"
                },
                "language": "en",
                "rank": 0,
                "status": "published",
                "tags": [
                    "fake2",
                    "ranke"
                ],
                "title": "create new",
                "updated_at": {
                    "$date": "2024-08-27T21:56:26.704Z"
                }
            }
            ```
            
        - **✅ Response 404**
            
            ```python
            {
            		"Error": "Article not found"
            }
            ```
            
    - **`[POST]` Add user**
        
        
        | Description | Updates the database by adding a user to it |
        | --- | --- |
        | URL | [domain/api/v1/add_users](API%20Docs%20a3ab83c49bee49f5aaa08f4b512f1b08.md) |
        | Auth Required | No |
        
        | Paramater | Type  | Required | Description |
        | --- | --- | --- | --- |
        | `Body params` |  |  |  |
        | Username | String | Yes | Name of the new user |
        | Email | String | Yes | Email of the new user |
        | Password | String | Yes | Password for the new user |
        - **✅ Response 201**
            
            ```python
            {
                "Email": "temp",
                "User name": "temp",
                "db ID": "66ce5d4d7b8a7dd2fa0b89d3"
            }
            ```
            
        - **✅ Response 400**
            
            ```python
            {
            		"Error": "Missing data"
            }
            ```
            
        - **✅ Response 400**
            
            ```python
            {
            		"Error": "Request must be JSON"
            }
            ```
            

---