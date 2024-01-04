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

// SQL query to fetch all rows and columns
$sql = "SELECT * FROM signals ORDER BY id DESC";

$result = $mysqli->query($sql);

// HTML output with styles
echo "<h1 style='text-align: center;'>Studio BMS Trigger Events</h1><br/><br/>";
echo "<style>table { width: 100%; border-collapse: collapse; } th, td { text-align: center; padding: 8px; }</style>";
echo "<table border='1'><tr><th>Event ID</th><th>Timestamp</th><th>Trigger</th><th>Status</th></tr>";

if ($result) {
    // Iterate over each row
    while ($row = $result->fetch_assoc()) {
        echo "<tr>";
        echo "<td>" . $row['id'] . "</td>";
        echo "<td>" . $row['timestamp'] . "</td>";
        echo "<td>" . $row['signal_trigger'] . "</td>";
        echo "<td>" . $row['states'] . "</td>";
        echo "</tr>";
    }
    echo "</table>";
    $result->free();
} else {
    echo "Error: " . $mysqli->error;
}

// Close the connection
$mysqli->close();
?>
