<?php
// Get form data
$name = $_POST['name'];
$profession = $_POST['profession'];
$email = $_POST['email'];
$phone_number = $_POST['phone_number'];
$option_selected = $_POST['option_selected'];

// Write data to Excel file
$file = 'form_data.csv';
$data = array($name, $profession, $email, $phone_number, $option_selected);

// Append data to the file
file_put_contents($file, implode(',', $data) . PHP_EOL, FILE_APPEND);

// Redirect to a thank you page or back to the form
header("Location: checkout.html");
exit();
?>
