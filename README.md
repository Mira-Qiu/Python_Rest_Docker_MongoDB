# Python create rest using Docker and MongoDB as databas

## To run 
```
sudo docker-compose build

sudo docker-compose up

```

## Environment
```
python : 3
flask, flask_restful

MongDB : 3.6.16

Ubuntu 18.04
```

## Test Get Method
```
localhost:5000/show
localhost:5000/{id}
localhost:5000/{id}/books
localhost:5000/{id}/books/{bid}
```

## Test Similaryty Test
```
localhost:5000/detect
```

### Test Post Json file
```
"test1": "This is a cute dog"
"test2": "It is a beautiful dog"

//get result of the similarity of these two sentence.
```

