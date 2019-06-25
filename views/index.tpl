<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="https://unpkg.com/element-ui/lib/theme-chalk/index.css">
  <title>铁路转车系统</title>
  <style>
    a {
      color: #333;
      font-weight: 700;
      font-size: 13px;
    }

    /*浮动样式**/
    .f_r {
      float: right;
    }

    .clear {
      clear: both;
    }

    /*居中样式**/
    .center {
      margin: 0 auto;
      text-align: center;
    }

    /**搜索框顶部图片***/
    .search_img {
      clear: both;
      text-align: center;
      margin: 250px auto 50px;
    }

    .search_img img {
      height: 100px;
    }

    /*搜索框样式**/
    .search_form {
      position: relative;
      margin: 0 auto;
      /*min-height: 200px; */
      height: 150px;
      width: 50%;
      margin-left:30%;
    }

    .search_form form {
      height: 100%;
    }

    .search_form form div {
      display: inline-block;
    }

    .search_form form div {
      width: 300px;
      height: 40px;
      position: relative;
    }

    .search_form form div img {
      position: absolute;
      top: 50%;
      left: 0px;
      transform: translateY(-50%);
      width: 11px;
      height: 10px;
      z-index: 11;
    }

    .search_form input[type="text"],
    .search_form select {
      width: 100%;
      height: 40px;
      box-sizing: border-box;
      font-size: 14px;
      padding: 3px 10px 3px 30px;
      border: 0;
      border-bottom: 1px solid #ccc;
      outline: none;
    }

    .search_form input[type="submit"] {
      width: 100px;
      height: 40px;
      background: #3385FF;
      color: #fff;
      border-bottom: 1px solid #2d78f4;
      -webkit-appearance: none;
      -webkit-border-radius: 0;
      outline: medium;
      margin-left: -6px;
      border: none;
    }

    .submit-button {
      position: absolute;
      right: 0;
      top: 50%;
      transform: translateY(-50%);
    }

    #form-citys {
      width: 100%;
    }

    #address-box-1,
    #address-box-2 {
      display: none;
      width: 100%;
      position: absolute;
      z-index: 10;
    }
  </style>
</head>

<body>
  <div class="search_img">
    <img src="img/logo.png">
  </div>
  <div class="search_form">
    <form action="/search" method="get">
      <div id="form-citys">
        <div class="from_city">
          <img src="img/green_icon.png" />
          <div>
            <el-select v-model="fromCity" name="from_city" filterable :filter-method="filter" placeholder="出发城市">
              <el-option v-for="item in currentCityList" :key="item.name_code" :label="item.name_chinese" :value="item.name_code">
              </el-option>
            </el-select>
          </div>
        </div>
        <span style="display: inline-block;margin: 0 10px;">到</span>
        <div class="to_city">
          <img src="img/red_icon.png" />
		  <el-select v-model="toCity" name="to_city" filterable :filter-method="filter2" placeholder="到达城市">
            <el-option v-for="item in currentCityList2" :key="item.name_code" :label="item.name_chinese" :value="item.name_code">
            </el-option>
          </el-select>
        </div>
        <input style="display: inline-block;margin-left: 10px;" type="submit" value="搜索">
      </div>
    </form>
  </div>
</body>
<script src="https://unpkg.com/vue/dist/vue.js"></script>
<script src="https://unpkg.com/element-ui/lib/index.js"></script>
<script>
    var xmlHttpReq = null; //声明一个空对象用来装入XMLHttpRequest
    function getCityList() {
        if (window.ActiveXObject) {//IE5 IE6是以ActiveXObject的方式引入XMLHttpRequest的
            xmlHttpReq = new ActiveXObject("Microsoft.XMLHTTP");
        } else if (window.XMLHttpRequest) {//除IE5 IE6 以外的浏览器XMLHttpRequest是window的子对象
            xmlHttpReq = new XMLHttpRequest();//实例化一个XMLHttpRequest
        }
        if (xmlHttpReq != null) { //如果对象实例化成功
            xmlHttpReq.open("get", "http://localhost:8080/rail", true); //调用open()方法并采用异步方式
            xmlHttpReq.onreadystatechange = RequestCallBack; //设置回调函数
            //如果以post方式请求，必须要添加
            xmlHttpReq.setRequestHeader("Content-type", "application/json");
            xmlHttpReq.send(null); //因为使用get方式提交，所以可以使用null参调用
        }
    }
    function RequestCallBack() {//一旦readyState值改变，将会调用这个函数
        if (xmlHttpReq.readyState == 4) {
            if (xmlHttpReq.status == 200) {
                //将xmlHttpReq.responseText的值赋给ID为 resText 的元素
                let res = JSON.parse(xmlHttpReq.responseText);
                form.citys = res;
                form.currentCityList = res;
				form.currentCityList2 = res;
            }
        }
    }
	getCityList();

  let form = new Vue({
    el: '#form-citys',
    data: function () {
      return {
        fromCity: '',
        toCity: '',
        citys: [],
        currentCityList: [],
        currentCityList2: []
      }
    },
    methods: {
        filter (key) {
            if (!key) {
                this.currentCityList = this.citys;
                return;
            }
            this.currentCityList = this.citys.filter(val => {
                if (val.name_code.toLowerCase().indexOf(key.toLowerCase())) {
                    if(!val.name_chinese.includes(key)){
                        return false;
                    }else{
                        return true;
                    }
                }
                return true;
            });
        },
		filter2 (key) {
            if (!key) {
                this.currentCityList2 = this.citys;
                return;
            }
            this.currentCityList2 = this.citys.filter(val => {
                if (val.name_code.toLowerCase().indexOf(key.toLowerCase())) {
                    if(!val.name_chinese.includes(key)){
                        return false;
                    }else{
                        return true;
                    }
                }
                return true;
            });
        }
    }
  });

</script>

</html>