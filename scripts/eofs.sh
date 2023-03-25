#!/bin/bash

echo "This Line would execute"

<< EOF

	echo "sdfsdfsdfds"
	echo "dfssfsfsdfsdd"
	echo "sdaasdadssadasdas"

	sleep 10

EOF


echo "This line would again execute"
