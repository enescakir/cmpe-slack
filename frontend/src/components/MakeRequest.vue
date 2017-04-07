<template>
  <div class="container">
    <div class="col-md-12">
      <h1><img src="../assets/slack-chat.png" />Boun - CmpE Slack Katılma İsteği</h1>
      <p>
        Bölüm öğrencilerinin dersleri tartışıp muhabbet edebileceği, teknoloji
        konuşup oyun arkadaşı bulabileceği bir slack grubu.
      </p>
    </div>
    <div class="col-md-12">
      <div class="alert alert-success" v-if="success">
        <strong>Başarılı!</strong> {{ success }}
      </div>
    </div>
    <div v-if="!success">
      <div class="clearfix">
      </div>
      <div class="col-md-3">
        <div class="input-container">
          <label for="name">Ad</label><br  />
          <input type="text" name="name" v-model="firstName"/>
        </div>
      </div>
      <div class="col-md-3">
        <div class="input-container">
          <label for="surname">Soyad</label><br  />
          <input type="text" name="surname" v-model="lastName" />
        </div>
      </div>
      <div class="clearfix"></div>
      <div class="col-md-6">
        <div class="input-container">
          <label for="email">Email</label><br  />
          <input type="email" name="email" v-model="email" />
        </div>
      </div>
      <div class="clearfix">
      </div>
      <div class="col-md-3">
        <div class="input-container">
          <label for="years">Giriş yılın</label><br  />
          <select name="years" v-model="entrance">
            <option v-for="year in years">{{ year }}</option>
          </select>
        </div>
      </div>
      <div class="clearfix"></div>
      <div class="col-md-6">
        <div class="input-container">
          <label>
            <input type="checkbox" name="who" value="yes" v-model="isCmpe"/>
            Bilgisayar Mühendisliği Öğrencisiyim
        </label>
        </div>
      </div>
      <div class="clearfix"></div>
      <div class="col-md-4 error__container" v-if="error">
        <p>
          Hata! {{error}}
        </p>
      </div>
      <div class="clearfix">
      </div>
      <div class="col-md-3">
        <button v-on:click="postRequest">Davet İsteği Gönder</button>
      </div>
    </div>
  </div>
</template>

<script>


export default {
  name: 'MakeRequest',
  data() {
    return {
      firstName: '',
      lastName: '',
      email: '',
      isCmpe: '',
      entrance: 2016,
      error: '',
      success: '',
      years: this.getYears(),
    };
  },

  methods: {
    getYears: function getYears() {
      const years = [];
      const startYear = new Date().getFullYear() - 1;
      const endYear = 1990;
      for (let i = startYear; i > endYear; i -= 1) {
        years.push(i);
      }
      return years;
    },

    validateInputs: function validateInputs() {
      this.$set(this, 'error', '');
      if (this.firstName === '') {
        this.$set(this, 'error', 'Ad boş bırakılamaz.');
        return false;
      }

      if (this.lastName === '') {
        this.$set(this, 'error', 'Soyad boş bırakılamaz.');
        return false;
      }

      if (this.email === '') {
        this.$set(this, 'error', 'Email boş bırakılamaz');
        return false;
      }

      if (!this.isCmpe) {
        this.$set(this, 'error', 'Bu slack grubuna katılmak için CMPE olmalısınız.');
        return false;
      }

      return true;
    },

    invalidateInputs: function invalidate() {
      this.$set(this, 'firstName', '');
      this.$set(this, 'lastName', '');
      this.$set(this, 'email', '');
      this.$set(this, 'isCmpe', '');
    },

    postRequest: function postRequest() {
      if (!this.validateInputs()) return;

      const requestBody = {
        firstName: this.firstName,
        lastName: this.lastName,
        email: this.email,
        entrance: this.entrance,
      };

      this.$http.post('/request', requestBody)
      .then(() => {
        this.$set(this, 'success', 'İsteğin alındı, en kısa zamanda vermiş olduğun email adresine davet gönderilecek.');
        this.invalidateInputs();
      },
      () => {
        this.$set(this, 'error', 'Bir hata oluştu, daha sonra tekrar dene.');
      });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
* {
  color: #727272;
}

img {
  width: 55px;
  margin-right: 10px;
}

.input-container{
  margin-top: 20px;
}

.error__container{
  margin-top: 15px;
}

.error__container p{
  font-size: 16px;
  color: red;
}

.alert{
  margin-top: 15px;
  color: #4A7443;
}

.alert strong{
  color: #4A7443;
}

input[type='text'], input[type='email'] {
  border-radius: 5px;
  border: 1px solid rgba(0, 0, 0, 0.2);
  width: 100%;
  height: 40px;
  padding: 0 10px;
  margin-top: 5px;
  font-size: 17px;
}

input[type='text']{
  text-transform: capitalize;
}

input[type='checkbox']{
  margin-right: 10px;
}

select{
  border-radius: 5px;
  border: 1px solid rgba(0, 0, 0, 0.2);
  width: 100%;
  height: 40px;
  padding: 0 10px;
  margin-top: 5px;
  background: #fff;
}

label{
  font-size: 16px;
  color: #000000;
  font-weight: normal;
}

button{
    margin-top: 10px;
    width: 100%;
    border: 0;
    border-radius: 4px;
    padding: 14px 32px;
    cursor: pointer;
    height: 53px;
    display: inline-block;
    font-size: 17px;
    font-weight: 700;
    background-color: #42c299;
    color: #fff!important;
    text-shadow: none;
    box-shadow: 0 3px 10px rgba(0,0,0,.2);
}

button:hover{
      background-color: #3dbd94;
}

h1, h2 {
  color: #E32072;
}

p {
  color: #000000;
  font-size: 18px;
}

a {
  color: #42b983;
}
</style>
