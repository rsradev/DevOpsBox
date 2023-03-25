BEGIN {
	# substitute space with a tab
	FS=",";
	OFS="\t\t";
	print "Date\t\tPrice\t\tVolume";
	print "-----\t\t----\t\t------";
};
NR > 1 {
	print $1, $2, $7
};



