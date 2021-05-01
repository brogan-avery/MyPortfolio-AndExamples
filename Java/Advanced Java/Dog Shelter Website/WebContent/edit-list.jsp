<!--Brogan Avery  -->
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
     <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Edit An Existing List</title>
</head>
<body>
<form action = "editListDetailsServlet" method="post">
<input type ="hidden" name = "id" value= "${listToEdit.id}">
List Name (breed): <input type ="text" name = "listName" value= "${listToEdit.listName}"><br />
Vaccination date: <input type ="text" name = "month" placeholder="mm" size="4" value= "${month}"> <input type ="text" name = "day" placeholder="dd" size="4" value= "${date}">, <input type ="text" name = "year" placeholder="yyyy" size="4" value= "${year}">
Worker Name: <input type = "text" name = "workerName" value= "${listToEdit.worker.workerName}"><br />

Available Dog Entries:<br />

<select name="allDogEntriesToAdd" multiple size="6">
<c:forEach items="${requestScope.allDogEntries}" var="currentDogEntry">
   <option value = "${currentDogEntry.id}">${currentDogEntry.name} | ${currentDogEntry.breed} | ${currentDogEntry.age}</option>
</c:forEach>
</select>
<br />
<input type = "submit" value="Edit List and Add Dog Entry">
</form>
<a href = "index.html">Go add new dog entry instead.</a>
</body>
</html>
