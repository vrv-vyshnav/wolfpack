# wolfpack

## setup
clone the repo `git clone https://github.com/vrv-vyshnav/wolfpack.git`

install dependencies `pip install -r requrirements.txt`

start sever `python manage.py runserver`

## Details about end points
POST  register - /api/register/ 

request body
``` json
{
  "name" : "Vaishnav"
  "email" : "vrv.VaishnavP@gmail.com"
  "password" : "None"
}
```

POST  login - /api/login/ 

request body
``` json
{
  "email" : "vrv.VaishnavP@gmail.com"
  "password" : "None"
}
```
response 
``` json
 {
    "jwt" : "token"
 }
```


POST  Image Transformation - /api/img/ 

request body
``` 
  form_field : image
```
response 
``` json
{
  "msg": "success",
  "gray_image": "http://localhost:8000/media/gray_image.png",
  "thumbnail": "http://localhost:8000/media/thumbnail.png",
  "medium": "http://localhost:8000/media/medium.png",
  "large": "http://localhost:8000/media/large.png"
}
```


