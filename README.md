# mf-some
The Social Network Test

# Run the solution
Use docker-compose and run

`docker-compose build`
`docker-compose up`

After this, the site is avaiable on https://localhost:5000/

# Loading data
An initial fixture is provided and can be loaded with


`
docker-compose run django ./manage.py loaddata initial.json
`
