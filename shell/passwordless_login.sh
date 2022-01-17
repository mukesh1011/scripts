#!/usr/bin/expect

spawn ssh cloud_user@52.56.93.52
expect "Password:"
send "12shroot\r"
interact
