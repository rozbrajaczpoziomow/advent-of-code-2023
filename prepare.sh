for i in $(seq 1 25)
do
	name=$(printf '%02d' $i)
	[ -d $name ] || mkdir $name

	if [ -n "$1" ]; then
		if [ "$1" = "$(sha256sum $name/$i.py | awk '{ print $1 }')" ]; then
			cp template.py $name/$i.py
			echo "Overwritten day $i (checksums matched)"
		fi
	else
		cp --no-clobber template.py $name/$i.py
	fi
	echo "Checksum for $name/$i.py: $(sha256sum $name/$i.py | awk '{ print $1 }')"
	touch $name/test.txt
	touch $name/input.txt
done