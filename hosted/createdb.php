<?php
$host = 'localhost';
$username = 'tvstudios';
$password = 'mlP$6n113gvsdfvreeeGBN';

// Create connection
$mysqli = new mysqli($host, $username, $password);

// Check connection
if ($mysqli->connect_error) {
    die("Connection failed: " . $mysqli->connect_error);
}

// Create database
$sql = "CREATE DATABASE IF NOT EXISTS concept_bms";
if ($mysqli->query($sql) === TRUE) {
    echo "Database created successfully\n";
} else {
    echo "Error creating database: " . $mysqli->error . "\n";
}

// Select the database
$mysqli->select_db("concept_bms");

// SQL to create table
$sql = "CREATE TABLE IF NOT EXISTS signals (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    signal_trigger INT(11) NOT NULL,
    states INT(11) NOT NULL
)";

if ($mysqli->query($sql) === TRUE) {
    echo "Table signals created successfully";
} else {
    echo "Error creating table: " . $mysqli->error;
}

$mysqli->close();
?>
