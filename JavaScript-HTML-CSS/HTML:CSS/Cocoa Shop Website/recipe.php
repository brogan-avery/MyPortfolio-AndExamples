<!DOCTYPE html>
<html>
<head>
  <link href = "cocoa_layout.css" rel = "stylesheet" type = "text/css"/>


<title> cocoa project recipe </title>
  <meta name = "discription" content = "Sally's Skinny Sweet Shop">
  <meta name = "keywords" content = "healthy chocolate, environmently friendly chocolate,cocoa">
  <meta name = "author" content= "Brogan Avery Oct 23 2019">
</head>



<body>
<h1> Sallly's Skinny Sweet Shop</h1>
      <div class = "topnav">
        <a class = "active" href = "Index.html"> Home </a>
        <a href = "handb.html"> History and Health </a>
        <a href = "ourprocess.html"> Our Process </a>
        <a href = "moreinfo.html"> Learn More </a>
        <a href = "recipe.html"> Share your Recipes </a>
      </div>
<br>
<div class="form">

  <?php

  echo "<p class='colorRed'>This page was created by PHP on the server and sent back to your browser. </p>";

  //It will create a table and display one set of name value pairs per row
  	echo "<table border='1'>";
  	echo "<tr><th>Field Name</th><th>Value of field</th></tr>";
  	foreach($_POST as $key => $value)
  	{
  		echo '<tr class=colorRow>';
  		echo '<td>',$key,'</td>';
  		echo '<td>',$value,'</td>';
  		echo "</tr>";
  	}
  	echo "</table>";
  	echo "<p>&nbsp;</p>";

  //This code pulls the field name and value attributes from the Post file
  //The Post file was created by the form page when it gathered all the name value pairs from the form.
  //It is building a string of data that will become the body of the email

  //          CHANGE THE FOLLOWING INFORMATION TO SEND EMAIL FOR YOU //

  	$toEmail = "broganaveryinfo@cisbam.com";		//CHANGE within the quotes. Place email address where you wish to send the form data.
  										//Use your DMACC email address for testing.
  										//Example: $toEmail = "jhgullion@dmacc.edu";

  	$subject = "cocoa info";	//CHANGE within the quotes. Place your own message.  For the assignment use "WDV101 Email Example"

  	$fromEmail = "bmavery@dmacc.com";		//CHANGE within the quotes.  Use your DMACC email address for testing OR
  										//use your domain email address if you have Heartland-Webhosting as your provider.
  										//Example:  $fromEmail = "contact@jhgullion.org";

  //   DO NOT CHANGE THE FOLLOWING LINES  //

  	$emailBody = "Form Data\n\n ";			//stores the content of the email
  	foreach($_POST as $key => $value)		//Reads through all the name-value pairs. 	$key: field name   $value: value from the form
  	{
  		$emailBody.= $key."=".$value."\n";	//Adds the name value pairs to the body of the email, each one on their own line
  	}

  	$headers = "From: $fromEmail" . "\r\n";				//Creates the From header with the appropriate address

   	if (mail($toEmail,$subject,$emailBody,$headers)) 	//puts pieces together and sends the email to your hosting account's smtp (email) server
  	{
     		echo("<p>Message successfully sent!</p>");
    	}
  	else
  	{
     		echo("<p>Message delivery failed...</p>");
    	}

  ?>
</div>

</body>
</html>
