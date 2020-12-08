import axios from 'axios';

const instance = axios.create({
  baseURL: process.env.VUE_APP_API_URL,
});

// function GET_RESULT(params) {
//   return instance.get(
//     `getResult/?img_path=${params.img_path}&p1=${params.p1}&p2=${params.p2}&relationship=${params.relationship}`,
//     params
//   );
// }

function GET_RESULT(params) {
  console.log(params);
  return instance.post(`getResult/`, params);
}
export { GET_RESULT };
