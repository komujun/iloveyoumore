<template>
  <div class="container">
    <div v-if="isLoading">
      <Spinner :progress="progress"></Spinner>
    </div>
    <div v-else class="wrapper">
      <div class="title">내가 더 좋아해!</div>
      <div class="logo"></div>
      <div class="form">
        <div>
          <mdb-input label="사람 1" v-model="value1" />
        </div>
        <div>
          <mdb-input label="사람 2" v-model="value2" />
        </div>
        <div class="inputfield">
          <div class="custom_select">
            <select v-model="relationship">
              <option value="" disabled selected>relationship</option>
              <option value="Lover">Lover</option>
              <option value="Friend">Friend</option>
              <option value="Family">Family</option>
            </select>
          </div>
        </div>
        <div>
          <mdb-input label="memo" v-model="memo" />
        </div>
        <div class="input-group">
          <div class="input-group-prepend">
            <span class="input-group-text" id="inputGroupFileAddon01"
              >Upload</span
            >
          </div>
          <div class="custom-file">
            <input
              type="file"
              class="custom-file-input"
              id="inputGroupFile01"
              aria-describedby="inputGroupFileAddon01"
              @change="uploadFile"
            />
            <label class="custom-file-label" for="inputGroupFile01">{{
              img_path.substr(0, 20)
            }}</label>
          </div>
        </div>
        <div class="inputfield">
          <mdb-btn type="submit" class="result-btn" @click="getResult"
            >알아보기</mdb-btn
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import firebase from 'firebase';
import { mdbInput, mdbBtn } from 'mdbvue';
import { GET_RESULT } from '@/api/index';
import store from '@/store/index';
import Spinner from '@/components/Spinner.vue';

export default {
  components: { Spinner, mdbInput, mdbBtn },
  data() {
    return {
      img_path: 'Choose file',
      value1: '',
      value2: '',
      email: '',
      memo: '',
      relationship: '',
      isLoading: false,
      progress: 0,
    };
  },
  methods: {
    setImg_URL(url) {
      this.img_path = url;
    },
    uploadFile(event) {
      this.isLoading = true;
      // File or Blob named mountains.jpg
      const file = event.target.files[0];
      const storageRef = firebase.storage().ref();

      // Create the file metadata
      var metadata = {
        contentType: 'image/jpeg',
      };
      // Upload file and metadata to the object 'images/mountains.jpg'
      var uploadTask = storageRef
        .child('images/' + file.name)
        .put(file, metadata);

      // Listen for state changes, errors, and completion of the upload.
      uploadTask.on(
        firebase.storage.TaskEvent.STATE_CHANGED, // or 'state_changed'
        (snapshot) => {
          // Get task progress, including the number of bytes uploaded and the total number of bytes to be uploaded
          var progress =
            (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
          this.progress = progress;
          console.log('Upload is ' + progress + '% done');
          switch (snapshot.state) {
            case firebase.storage.TaskState.PAUSED: // or 'paused'
              console.log('Upload is paused');
              break;
            case firebase.storage.TaskState.RUNNING: // or 'running'
              console.log('Upload is running');
              break;
          }
        },
        (error) => {
          switch (error.code) {
            case 'storage/unauthorized':
              // User doesn't have permission to access the object
              break;

            case 'storage/canceled':
              // User canceled the upload
              break;

            case 'storage/unknown':
              // Unknown error occurred, inspect error.serverResponse
              break;
          }
        },
        () => {
          // Upload completed successfully, now we can get the download URL
          uploadTask.snapshot.ref.getDownloadURL().then((downloadURL) => {
            console.log('File available at', downloadURL);
            this.img_path = downloadURL;
            this.setImg_URL(downloadURL);
            this.isLoading = false;
          });
        }
      );
    },
    async getResult() {
      const params = {
        img_path: this.img_path,
        p1: this.value1,
        p2: this.value2,
        relationship: this.relationship,
      };
      store.commit('setReq', params);
      this.isLoading = true;
      const { data } = await GET_RESULT(params);
      store.commit('setRes', data);
      console.log(data);

      this.$router.push('result');
    },
  },
};
</script>

<style>
/* @import url('https://fonts.googleapis.com/css?family=Montserrat:400,700&display=swap'); */

* {
  box-sizing: border-box;
  /* font-family: 'Montserrat', sans-serif; */
}
/* * {
  font-family: 'MaplestoryOTFBold';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@2.1/MaplestoryOTFBold.woff')
    format('woff');
  font-weight: normal;
  font-style: normal;
} */
/* * {
  font-family: 'ImcreSoojin';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@2.3/ImcreSoojin.woff')
    format('woff');
  font-weight: normal;
  font-style: normal;
} */
.wrapper {
  max-width: 500px;
  width: 100%;
  background: #fff;
  box-shadow: 1px 1px 2px rgba(0, 0, 0, 0.125);
  padding: 30px;
  margin: 10px auto;
}

@keyframes logo {
  100% {
    background-position: -150px 0;
  }
}

.logo {
  width: 60px;
  height: 60px;
  background: url('../assets/logo.jpg') no-repeat 0 bottom;
  background-size: 145px 40px;
  animation: logo 2000ms infinite steps(3);
  margin: 10px auto;
  border-radius: 50%;
  border: 5px solid #f2b3e1;
  padding-top: 10px;
}

.wrapper .title {
  font-size: 24px;
  font-weight: 700;
  margin-bottom: 25px;
  color: #f2059f;
  text-transform: uppercase;
  text-align: center;
}

.wrapper .form {
  width: 100%;
}

.wrapper .form .inputfield {
  margin-bottom: 15px;
  display: flex;
  align-items: center;
}

.wrapper .form .inputfield label {
  width: 200px;
  color: #757575;
  margin-right: 10px;
  font-size: 14px;
}

.wrapper .form .inputfield .input,
.wrapper .form .inputfield .textarea {
  width: 100%;
  outline: none;
  border: 1px solid #d5dbd9;
  font-size: 15px;
  padding: 8px 10px;
  border-radius: 3px;
  transition: all 0.3s ease;
}

.wrapper .form .inputfield .textarea {
  width: 100%;
  height: 125px;
  resize: none;
}

.wrapper .form .inputfield .custom_select {
  position: relative;
  width: 100%;
  height: 37px;
}

.wrapper .form .inputfield .custom_select:before {
  content: '';
  position: absolute;
  top: 12px;
  right: 10px;
  border: 8px solid;
  border-color: #d5dbd9 transparent transparent transparent;
  pointer-events: none;
}

.wrapper .form .inputfield .custom_select select {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  outline: none;
  width: 100%;
  height: 100%;
  border: 0px;
  padding: 8px 10px;
  font-size: 15px;
  border: 1px solid #d5dbd9;
  border-radius: 3px;
}

.wrapper .form .inputfield .input:focus,
.wrapper .form .inputfield .textarea:focus,
.wrapper .form .inputfield .custom_select select:focus {
  border: 1px solid #f2059f;
}

.wrapper .form .inputfield p {
  font-size: 14px;
  color: #757575;
}
.wrapper .form .inputfield .result-btn {
  width: 100%;
  padding: 8px 10px;
  font-size: 15px;
  border: 0px;
  background: #f2b3e1;
  color: #fff;
  cursor: pointer;
  border-radius: 3px;
  outline: none;
}

.wrapper .form .inputfield .result-btn:hover {
  background: #f2059f;
}

.wrapper .form .inputfield:last-child {
  margin-bottom: 0;
}
.result-btn {
  font-size: 3rem;
}
</style>
