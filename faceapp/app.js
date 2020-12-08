var express = require('express');
var app = express();
var client_id = 'RpYaXW3aRGDGIULrJFp0';
var client_secret = 'b_wlvEmiVP';
var fs = require('fs');
var cors = require('cors');

app.use(cors());

app.get('/face', function (req, res) {
  const { img_path } = req.query;
  var request = require('request');
  //   var api_url = 'https://openapi.naver.com/v1/vision/celebrity'; // 유명인 인식
  var api_url = 'https://openapi.naver.com/v1/vision/face'; // 얼굴 감지
  var _formData = {
    image: 'image',
    image: fs.createReadStream(__dirname + '/young-couple.jpg'), // FILE 이름
    // image: fs.createReadStream(img_path), // FILE 이름
  };
  //   console.log('asdfasdfasdfasdfasdfasdfasdfasdfasdf', _formData);
  var _req = request
    .post({
      url: api_url,
      formData: _formData,
      headers: {
        'X-Naver-Client-Id': client_id,
        'X-Naver-Client-Secret': client_secret,
      },
    })
    .on('response', function (response) {
      //   console.log(response.statusCode); // 200
      //   console.log(response.headers['content-type']);
      if (response.statusCode === 200) {
        console.log(response);
      }
    });
  //   console.log(request.head);
  _req.pipe(res);
});

app.listen(8080, function () {
  console.log('http://localhost:8080/face app listening on port 8080!');
});
