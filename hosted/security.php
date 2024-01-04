<?php
// Database configuration
$host = 'localhost';
$dbname = 'concept_bms';
$username = 'tvstudios';
$password = 'mlP$6n113gvsdfvreeeGBN';

// Create a MySQLi connection
$mysqli = new mysqli($host, $username, $password, $dbname);

// Check connection
if ($mysqli->connect_error) {
    die("Connection failed: " . $mysqli->connect_error);
}

// Get and sanitize the 's' parameter from the URL
$s = isset($_GET['s']) ? intval($_GET['s']) : 0;

// Get and sanitize the 'k' parameter from the URL
$k = isset($_GET['k']) ? intval($_GET['k']) : 0;

// Prepare an INSERT statement
$stmt = $mysqli->prepare("INSERT INTO signals (timestamp, signal_trigger, states) VALUES (NOW(), ?, ?)");
$stmt->bind_param("ii", $s, $k);

// Execute the query
if ($stmt->execute()) {
    echo "Record created successfully";
} else {
    echo "Error: " . $stmt->error;
}

// Close statement and connection
$stmt->close();
$mysqli->close();
?>
