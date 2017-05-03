#!/bin/bash

read x

range=`echo $x | cut -d'&' -f1 | cut -d'=' -f2 | tr '+' ' '`

firstNumber=`cut -d'-' -f1 <<< "$range"`
secondNumber=`cut -d'-' -f2 <<< "$range"`

cp /home/andrew/Developer/CIS345/homework1/customers_and_contacts /test/hw5prb1solution

while ((i++)); read p; do
	year=`cut -d'-' -f6 <<< $p`
	currentYear=`date +"%Y"`
	difference=`expr $currentYear - $year`
	if (( difference < firstNumber ))
	then
		sed -i "/$p/d" /test/hw5prb1solution
	elif (( difference > secondNumber ))
	then
		sed -i "/$p/d" /test/hw5prb1solution
	fi
done < /home/andrew/Developer/CIS345/homework1/customers_and_contacts

if [ -s "/test/hw5prb1solution" ]
then
	# Cut out the "private" information.
	while read line
	do
		private=`cut -d'	' -f1-7 <<< "$line"`
		valuetosend+="$private<br>"
	done < /test/hw5prb1solution
else
	valuetosend="Nothing was found!"
fi

echo "Content-type: text/html"
echo ""
echo "<html><head><title>Results</title></head>
<body>
<center><h3>Lookup for $range age range in customers and contacts:</h3></center>
<br>
<center>$valuetosend</center>
<br>
</body></html>"
