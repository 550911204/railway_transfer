<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>铁路转车系统</title>
  <style>
    /**搜索框顶部图片***/
    .search_img {
      clear: both;
      text-align: center;
      margin: 250px auto 50px;
    }

    .search_img img {
      height: 100px;
    }


  </style>
</head>

<body>
  <div style="width:50%;height:40vh;background:#F0F0F0;margin:auto;text-align:center">
	<div class="search_img">
		<a href="http://localhost:8080/index">
		    <img src="img/logo.png">
	    </a>
	</div>
	<label style="font-size:30px">很抱歉，{{fromCity}}至{{toCity}}暂无中转列车</label>
  </div>

</body>
</html>