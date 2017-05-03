#!/bin/bash

read x

firstname=`echo $x | cut -d'&' -f1 | cut -d'=' -f2 | tr '+' ' '`
lastname=`echo $x | cut -d'&' -f2 | cut -d'=' -f2 | tr '+' ' '`

whatisfound=`grep -w "$firstname	$lastname" /home/andrew/Developer/CIS345/homework1/customers_and_contacts`

if (( ${#whatisfound} > 0 ))
then
	# Cut out the "private" information.
	while read line
	do
		private=`cut -d'	' -f1-7 <<< "$line"`
		valuetosend+="$private<br>"
	done <<< "$whatisfound"
else
	valuetosend="Nothing was found!"
fi

echo "Content-type: text/html"
echo ""
echo "<html><head><title>Results</title></head>
<body>
<center><h3>Lookup for $firstname $lastname in customers and contacts:</h3></center>
<br>
<center>$valuetosend</center>
<br>
</body></html>"
