## JSON Web Token

compact, url safe string that represents claims(data about the users).

### structure

header.payload.signature

#### header

algorithm + type (HS256, jwt)

#### payload

 claims (user info, role, expiry e.t.c)

 #### signature

 ensure the token hasn't been tampered with (signed using your secret key)