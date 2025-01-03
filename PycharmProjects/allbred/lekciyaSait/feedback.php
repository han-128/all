<html>

<head>
<title>Моя первая веб-страничка</title>
<link rel="stylesheet" type="text/css" href="style.css"> 
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
</head>

<body>
<header>
	<img src="log_AiVT.jpg" width="200" align="left" hspace="20">
	<h1 align="center">Факультет Автоматики и вычислительной техники</h1><br>
	<h3 align="center">Факультет автоматики и вычислительной техники (АиВТ) готовит специалистов в области математического и компьютерного моделирования, проектирования и эффективного применения средств вычислительной техники, информационно-измерительных и электротехнических систем и комплексов, средств и систем автоматизации и управления. 
	Учебный процесс связан с решением задач развития нефтегазовой отрасли.</h3>
</header>

<div id="menu">
<ul>
	<li><a href="index.html">Главная</a></li>
	<li><a href="about.html">О факультете</a></li>
	<li><a href="contacts.html">Контакты</a></li>
	<li><a href="feedback.php">Задать вопрос</a></li>

</div>


<main>
<h2><i>ОБРАТНАЯ СВЯЗЬ:</i></h2>
<form name="form1" method="post" action="test.php"><p> 
Имя: <input type="text" name="sirname"></p><p> 
Ваш Email: <input  type="text" name="email"></p>
<p> Сообщение 
<textarea name="message"></textarea> (поле сообщения) </p>
<p><input type="submit" name="send" value="Отправить"></p>
</form>

<?php
/* Подключаемся к базе данных */
  $link = mysqli_connect("localhost", "root", "");
  mysqli_select_db($link, "praktika");

/* Выбираем данные */
$sql="SELECT name, email, message FROM baa";
$result=mysqli_query($link, $sql);

while ($line=mysqli_fetch_row($result)) {
echo "<b>Имя:</b>".$line[0]."<br>";
echo "<b>Email:</b>".$line[1]."<br>";
echo "<b>Сообщение:</b>".$line[2]."<br><br>";
}
?>

</main>

<footer>
@ Лекция 03.07.2024 Учебная практика - 2024
</footer>
</body>
</html> 