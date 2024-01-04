<?php
// Checker called by remote alarms to check for an alarm state.

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

// SQL query to fetch the most recent entry's state
$sql = "SELECT states FROM signals ORDER BY id DESC LIMIT 1";

$result = $mysqli->query($sql);

if ($result) {
    // Fetch the row
    $row = $result->fetch_assoc();
    if ($row) {
        echo $row['states'];
    } else {
        echo "x";
    }
    $result->free();
} else {
    echo "Error: " . $mysqli->error;
}

// Close the connection
$mysqli->close();
?>
