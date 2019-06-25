<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="https://unpkg.com/element-ui/lib/theme-chalk/index.css">
  <title>铁路转车系统</title>
  <style>
	.blockH{
		width:75%;
		height:24.5vh;
		border:1px solid #000;
		background:transparent;
		margin:2vh auto auto 12.5vw;
	}

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
      margin: 20px auto auto 15%;
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
  <div id="radio_1">
  <div class="search_img">
	<a href="http://localhost:8080/index">
		<img src="img/logo.png">
	</a>
  </div>
  <hr style ="width:75%">
  <div style="margin:2vh auto auto 14vw">
	<div id="from_to">
	    <span>出发城市：</span>
	    <span style="font-size:18px;font-weight:800;">{{fromCity}}</span>

        <el-button icon="el-icon-refresh"  onClick="exchangeCity()" size="small" style="margin:auto 3vw"></el-button>

		<span>到达城市：</span>
		<span style="font-size:18px;font-weight:800;">{{toCity}}</span>
	</div>
  </div>
  <div style="margin:3vh auto auto 14vw">
	<div>
	<span style="display: inline-block">中转城市：</span>
    <el-select v-model="newMid" name="from_city" filterable placeholder="指定城市"  style="width:6vw">
        <el-option  v-for="item in currentCityList" :key="item.name_chinese" :label="item.name_chinese" :value="item.name_chinese">
        </el-option>
    </el-select>
    <el-button type="primary" icon="el-icon-search"  onClick="newMidCity()" size="small">搜索</el-button>
	</div>
  </div>

  <div style="margin:3vh auto auto 14vw">
	<div>
	  <span>车次类型：</span>
      <el-radio-group v-model="trainTypeFirst" @change="changeFirst">
            <el-radio-button label="全部"></el-radio-button>
            <el-radio-button label="GC-高铁/城际"></el-radio-button>
            <el-radio-button label="D-动车"></el-radio-button>
            <el-radio-button label="Z-直达"></el-radio-button>
            <el-radio-button label="T-特快"></el-radio-button>
            <el-radio-button label="K-快速"></el-radio-button>
      </el-radio-group>
	  <span style="margin:auto 4vw">转</span>
      <el-radio-group v-model="trainTypeSecond" @change="changeSecond">
            <el-radio-button label="全部"></el-radio-button>
            <el-radio-button label="GC-高铁/城际"></el-radio-button>
            <el-radio-button label="D-动车"></el-radio-button>
            <el-radio-button label="Z-直达"></el-radio-button>
            <el-radio-button label="T-特快"></el-radio-button>
            <el-radio-button label="K-快速"></el-radio-button>
       </el-radio-group>
	</div>
  </div>

  <div style="margin:3vh auto auto 14vw">
	<div id="radio_2">
	  <span>排序方式：</span>
      <el-radio-group v-model="radio2" @change="changeResult">
      <el-radio-button label="综合排序"></el-radio-button>
      <el-radio-button label="耗时优先"></el-radio-button>
      <el-radio-button label="价格优先"></el-radio-button>
      <el-radio-button label="率先到达"></el-radio-button>
    </el-radio-group>
	</div>
  </div>

  <hr style ="width:75%;margin:3vh auto auto 12.4vw">

  <div style="width:75%;background:#F0F0F0;margin:auto;line-height:4vh">
	<label style="margin-left: 7vw;">车次编号</label>
	<label style="margin-left: 6vw;">出发/到达时间</label>
	<label style="margin-left: 6vw;">出发/到达车站</label>
	<label style="margin-left: 7.5vw;">运行时间</label>
	<label style="margin-left: 8.5vw;">参考价（硬座/二等座）</label>
  </div>
  <hr style ="width:75%;margin:auto auto auto 12.4vw">

  <template v-if="lists != null && lists.length != 0">
  <template v-for="item1 in lists">
  <div class="blockH" id="blockList">
   <table style="border-collapse:separate; border-spacing:7.5vw 2vh;">
		<tr style="position:relative">
			<td style="width:3vw">{[{item1[0].number}]}</td>
			<td style="font-weight:700;font-size:20px">{[{item1[0].start_time}]}</td>
			<td style="width:5vw"><span style="border:1px solid;width:20px;height:20px;color:#39f">始</span>&nbsp;&nbsp;{[{item1[0].from_station}]}</td>
			<td style="position:relative;top: 2.4vh;width:5vw">{[{item1[0].cost}]}</td>
			<td style="position:relative;top: 2.4vh;">票价：{[{item1[0].price}]}</td>
		</tr>
		<tr>
			<td></td>
			<td>{[{item1[0].to_time}]}</td>
			<td style="width:5vw"><span style="border:1px solid;width:20px;height:20px;color:#67C23A">过</span>&nbsp;&nbsp;{[{item1[0].to_station}]}</td>
		</tr>
	</table>

	<span style="border:1px dotted;width:52%;display:inline-block"></span>
	<span style="display:inline-block;width:28vw;border:1px solid;color:#E6A23C;text-align:center">&nbsp;&nbsp;&nbsp;停留：{[{item1[2].stay_time}]}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;全程：{[{item1[2].whole_cost}]}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;总价格：{[{item1[2].whole_price}]}</span>
	<span style="border:1px dotted;width:8.9%;display:inline-block"></span>

	<table style="border-collapse:separate; border-spacing:7.5vw 2vh;">
		<tr style="position:relative">
			<td style="width:3vw">{[{item1[1].number}]}</td>
			<td style="font-weight:700;font-size:20px">{[{item1[1].start_time}]}</td>
			<td style="width:5vw"><span style="border:1px solid;width:20px;height:20px;color:#67C23A">过</span>&nbsp;&nbsp;{[{item1[1].from_station}]}</td>
			<td style="position:relative;top: 2.4vh;width:5vw">{[{item1[1].cost}]}</td>
			<td style="position:relative;top: 2.4vh;">票价：{[{item1[1].price}]}</td>
		</tr>
		<tr>
			<td></td>
			<td>{[{item1[1].to_time}]}</td>
			<td style="width:5vw"><span style="border:1px solid;width:20px;height:20px;color:#F56C6C">终</span>&nbsp;&nbsp;{[{item1[1].to_station}]}</td>
		</tr>
	</table>
  </template>
  </template>
  <template v-else >
  <div style="padding: 10vh;font-size: 25px;margin-left: 15vw;">
    <span>很抱歉，按您的查询条件，当前未找到从{{fromCity}} 经{{midCity}} 中转到{{toCity}} 的列车，建议您更改查询条件。</span>
  </div>
  </template>

  </div>
  </div>
</body>
  <script src="https://unpkg.com/vue/dist/vue.js"></script>
  <script src="https://unpkg.com/element-ui/lib/index.js"></script>
  <script>
	var midCity = new Vue({
	    delimiters:["{[{","}]}"],
        el: '#radio_1',
        data: function () {
          return {
            radio2:'综合排序',
            radio4: '',
            trainTypeFirst:'全部',
            trainTypeSecond:'全部',
            lists:[],
            newMid: '',
            currentCityList: []
          }
        },
        methods: {
            changeResult() {
                url = "http://localhost:8080/resuList?from_city={{fromCity}}&to_city={{toCity}}&mid_city={{midCity}}&type="+this.radio2+"&typeFirst="+this.trainTypeFirst+"&typeSecond="+this.trainTypeSecond;
                console.log(url);
                xmlFun(url,getTime);
            },
            changeFirst(){
                url = "http://localhost:8080/resuList?from_city={{fromCity}}&to_city={{toCity}}&mid_city={{midCity}}&type="+this.radio2+"&typeFirst="+this.trainTypeFirst+"&typeSecond="+this.trainTypeSecond;
                console.log(url);
                xmlFun(url,getTime);
            },
            changeSecond(){
                url = "http://localhost:8080/resuList?from_city={{fromCity}}&to_city={{toCity}}&mid_city={{midCity}}&type="+this.radio2+"&typeFirst="+this.trainTypeFirst+"&typeSecond="+this.trainTypeSecond;
                console.log(url);
                xmlFun(url,getTime);
            }
        }
	});
    var xmlHttpReq = null; //声明一个空对象用来装入XMLHttpRequest
    function xmlFun(url,handleCB) {
        if (window.ActiveXObject) {//IE5 IE6是以ActiveXObject的方式引入XMLHttpRequest的
            xmlHttpReq = new ActiveXObject("Microsoft.XMLHTTP");
        } else if (window.XMLHttpRequest) {//除IE5 IE6 以外的浏览器XMLHttpRequest是window的子对象
            xmlHttpReq = new XMLHttpRequest();//实例化一个XMLHttpRequest
        }
        if (xmlHttpReq != null) { //如果对象实例化成功
            xmlHttpReq.open("get", url, false); //调用open()方法并采用异步方式
            xmlHttpReq.onreadystatechange = function RequestCallBack() {//一旦readyState值改变，将会调用这个函数
                if (xmlHttpReq.readyState == 4) {
                    if (xmlHttpReq.status == 200) {
                        //将xmlHttpReq.responseText的值赋给ID为 resText 的元素
                        let res = JSON.parse(xmlHttpReq.responseText);
                        handleCB(res);
                    }
                }
            }; //设置回调函数
            //如果以post方式请求，必须要添加
            xmlHttpReq.setRequestHeader("Content-type", "application/json");
            xmlHttpReq.send(null); //因为使用get方式提交，所以可以使用null参调用
        }
    }
    function getTime(res){
        //请求默认综合方案
        midCity.lists = res;
    }
    function getAllCity(res){
        midCity.currentCityList = res;
    }
    function newMidCity(){
        if(midCity.newMid!=''){
            url = "http://localhost:8080/appoint?from_city={{fromCity}}&to_city={{toCity}}&mid_city="+midCity.newMid;
            window.location.href = url;
        }
    }
    function exchangeCity(){
        url = "http://localhost:8080/search?from_city={{toCity}}&to_city={{fromCity}}";
        window.location.href = url;
    }

    xmlFun("http://localhost:8080/rail",getAllCity);
	xmlFun("http://localhost:8080/resuList?from_city={{fromCity}}&to_city={{toCity}}&mid_city={{midCity}}&type=综合排序",getTime);
  </script>

</html>