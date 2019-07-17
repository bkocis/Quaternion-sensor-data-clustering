#!/bin/bash

var_sec=8

echo "Calibration starting."
sleep 1


echo "Put me to your LOWER LEFT side of teeth" 
echo "2"
sleep 1
echo "1"
sleep 1
echo "Recording..."
echo "time x y z qx qy qz qw" > test_data_LL_2_.txt
`python3 UDP_with_pySocket_01.py >> test_data_LL_2_.txt &`
secs=$(($var_sec))
while [ $secs -gt 0 ]; do
	echo " ... hold me"
	echo -ne "$secs\033[0K\r"
	sleep 1 
	: $((secs--))
done
kill -9 `ps -ef | grep 'UDP' | grep -v 'grep' | awk '{print $2}'`
`vi -c ":%s/b'//g" -c ":%s/ '//g" -c ":wq" test_data_LL_2_.txt`


echo "Put me to your LOwER RIGHT side of teeth" 
echo "2"
sleep 1
echo "1"
sleep 1
echo "Recording..."
echo "time x y z qx qy qz qw" > test_data_LR_2_.txt
`python3 UDP_with_pySocket_01.py >> test_data_LR_2_.txt &`
secs=$(($var_sec))
while [ $secs -gt 0 ]; do
	echo " ... hold me"
	echo -ne "$secs\033[0K\r"
	sleep 1
	: $((secs--))
done
kill -9 `ps -ef | grep 'UDP' | grep -v 'grep' | awk '{print $2}'`
`vi -c ":%s/b'//g" -c ":%s/ '//g" -c ":wq" test_data_LR_2_.txt`


echo "Put me to your UPPER RIGHT side of teeth" 
echo "2"
sleep 1
echo "1"
sleep 1
echo "Recording..."
echo "time x y z qx qy qz qw" > test_data_UR_2_.txt
`python3 UDP_with_pySocket_01.py >> test_data_UR_2_.txt &`
secs=$(($var_sec))
while [ $secs -gt 0 ]; do
	echo " ... hold me"
	echo -ne "$secs\033[0K\r"
	sleep 1
	: $((secs--))
done
kill -9 `ps -ef | grep 'UDP' | grep -v 'grep' | awk '{print $2}'`
`vi -c ":%s/b'//g" -c ":%s/ '//g" -c ":wq" test_data_UR_2_.txt`


echo "Put me to your UPPER LEFT side of teeth" 
echo "2"
sleep 1
echo "1"
sleep 1
echo "Recording..."
echo "time x y z qx qy qz qw" > test_data_UL_2_.txt
`python3 UDP_with_pySocket_01.py >> test_data_UL_2_.txt &`
secs=$(($var_sec))
while [ $secs -gt 0 ]; do
	echo " ... hold me"
	echo -ne "$secs\033[0K\r"
	sleep 1
	: $((secs--))
done
kill -9 `ps -ef | grep 'UDP' | grep -v 'grep' | awk '{print $2}'`
`vi -c ":%s/b'//g" -c ":%s/ '//g" -c ":wq" test_data_UL_2_.txt`

sleep 1
echo "Data labeling done!"
sleep 2
echo "You can start brushing your teeth now"

# run the brushing classifier live 
python3 UDP_with_pySocket_01__live_prediciton.py
