<?php
/* Принимаем данные из формы */
  $name = $_POST["sirname"]; 
  $email = $_POST["email"];
  $text_message = $_POST["message"];

/* Подключаемся к базе данных */
  $link = mysqli_connect("localhost", "root", "");
  mysqli_select_db($link, "praktika");

/* Записывает данные */ 
$sql = "INSERT INTO baa(name, email, message) VALUES ('$name', '$email', '$text_message')";
$result=mysqli_query($link, $sql);

/* Делаем редирект обратно */
header("Location: ".$_SERVER["HTTP_REFERER"]); 
exit;
?>
